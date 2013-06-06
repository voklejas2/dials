#!/usr/bin/env python
#
# dials.model.serialize.imageset.py
#
#  Copyright (C) 2013 Diamond Light Source
#
#  Author: James Parkhurst
#
#  This code is distributed under the BSD license, a copy of which is
#  included in the root directory of this package.

def imageset_to_dict(imageset):
    ''' Convert the imageset to a dictionary

    Params:
        sweep The imageset

    Returns:
        A dictionary of the parameters

    '''
    from collections import OrderedDict
    from dxtbx.imageset import ImageSet, ImageSweep

    # If this is an imageset then return a list of filenames
    if isinstance(imageset, ImageSet):
        d = OrderedDict([("filenames", imageset.paths())])

    # Otherwise return a template and the image range
    elif isinstance(imageset, ImageSweep):
        template = imageset.get_template()
        array_range = imageset.get_array_range()
        image_range = (array_range[0] + 1, array_range[1])
        d = OrderedDict([
            ("template", imageset.get_template()),
            ("image_range", imageset.get_array_range())])
    else:
        raise TypeError("Unknown ImageSet Type")

    # Return the dictionary
    return d

def template_string_to_glob_expr(template):
    '''Convert the template to a glob expression.'''
    pfx = template.split('#')[0]
    sfx = template.split('#')[-1]
    return '%s%s%s' % (pfx, '[0-9]'*template.count('#'), sfx)

def template_string_number_index(template):
    '''Get the number idex of the template.'''
    pfx = template.split('#')[0]
    sfx = template.split('#')[-1]
    return len(pfx), len(pfx) + template.count('#')

def locate_files_matching_template_string(template):
    '''Return all files matching template.'''
    from glob import glob
    return glob(template_string_to_glob_expr(template))

def template_image_range(template):
    '''Return the image range of files with this template.'''

    # Find the files matching the template
    filenames = locate_files_matching_template_string(template)
    filenames = sorted(filenames)

    # Check that the template matches some files
    if len(filenames) == 0:
        raise ValueError('Template doesn\'t match any files.')

    # Get the templete format
    index = slice(*template_string_number_index(template))

    # Get the first and last indices
    first = int(filenames[0][index])
    last  = int(filenames[-1][index])

    # Reutrn the image range
    return (first, last)

def imageset_from_dict(d):
    ''' Convert the dictionary to a sweep

    Params:
        d The dictionary of parameters

    Returns:
        The sweep

    '''
    from dxtbx.imageset import ImageSetFactory
    from dials.model.serialize.beam import beam_from_dict
    from dials.model.serialize.detector import detector_from_dict
    from dials.model.serialize.goniometer import goniometer_from_dict
    from dials.model.serialize.scan import scan_from_dict

    # If this is a generic imageset then construct as normal
    if "filenames" in d:
        filenames = map(str, d['filenames'])
        imageset = ImageSetFactory.new(filenames)[0]

        # Get the models
        beam = beam_from_dict(d.get('beam'))
        detector = detector_from_dict(d.get('detector'))

        # Set models
        imageset.set_beam(beam)
        imageset.set_detector(detector)

        # Return the imageset
        return imageset

    # If this is specifically a sweep then construct through the template
    else:

        # Get the template (required)
        template = str(d['template'])

        # Get the models
        beam = beam_from_dict(d.get('beam'))
        detector = detector_from_dict(d.get('detector'))
        goniometer = goniometer_from_dict(d.get('goniometer'))
        scan = scan_from_dict(d.get('scan'))

        # If the scan isn't set, find all available files
        if scan is None:
            image_range = template_image_range(template)
        else:
            image_range = scan.get_image_range()

        # Construct the sweep
        sweep = ImageSetFactory.from_template(template, image_range)[0]
        sweep.set_beam(beam)
        sweep.set_goniometer(goniometer)
        sweep.set_detector(detector)

        # Return the sweep
        return sweep
