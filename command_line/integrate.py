#!/usr/bin/env python
#
# dials.integrate.py
#
#  Copyright (C) 2013 Diamond Light Source
#
#  Author: James Parkhurst
#
#  This code is distributed under the BSD license, a copy of which is
#  included in the root directory of this package.

from __future__ import division
from dials.util.script import ScriptRunner


class Script(ScriptRunner):
    '''A class for running the script.'''

    def __init__(self):
        '''Initialise the script.'''

        # The script usage
        usage  = "usage: %prog [options] [param.phil] " \
                 "sweep.json crystal.json [reference.pickle]"

        # Initialise the base class
        ScriptRunner.__init__(self, usage=usage)

        # Output filename option
        self.config().add_option(
            '-o', '--output-filename',
            dest = 'output_filename',
            type = 'string', default = 'integrated.pickle',
            help = 'Set the filename for integrated reflections.')

        # Option to save profiles with reflection data
        self.config().add_option(
            '-p', '--save-profiles',
            dest = 'save_profiles',
            action = 'store_true', default = False,
            help = 'Output profiles with reflection data.')

    def main(self, params, options, args):
        '''Execute the script.'''
        from dials.algorithms.integration import IntegratorFactory
        from dials.algorithms import shoebox
        from dials.model.serialize import load, dump
        from dials.util.command_line import Command
        from time import time

        # Check the number of arguments is correct
        start_time = time()
        if len(args) != 2 and len(args) != 3:
            self.config().print_help()
            return

        # Get the integrator from the input parameters
        print 'Configurating integrator from input parameters'
        integrate = IntegratorFactory.from_parameters(params)

        # Try to load the models
        print 'Loading models from {0} and {1}'.format(args[0], args[1])
        sweep = load.sweep(args[0])
        crystal = load.crystal(args[1])

        # Load the reference profiles
        if len(args) == 3:
#            reference = load.reflections(args[2])
            reference = load.reference(args[2])
        else:
            reference = None

        # Intregate the sweep's reflections
        print 'Integrating reflections'
        reflections = integrate(sweep, crystal, reference=reference)

        # Save the reflections to file
        nvalid = len([r for r in reflections if r.is_valid()])
        Command.start('Saving {0} reflections to {1}'.format(
            nvalid, options.output_filename))
        if options.save_profiles == False:
            shoebox.deallocate(reflections)
        dump.reflections(reflections, options.output_filename)
        Command.end('Saved {0} reflections to {1}'.format(
            nvalid, options.output_filename))

        # Print the total time taken
        print "\nTotal time taken: ", time() - start_time

if __name__ == '__main__':
    script = Script()
    script.run()
