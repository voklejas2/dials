#!/usr/bin/env cctbx.python

# Copyright (C) (2012) David Waterman, STFC Rutherford Appleton Laboratory, UK.
# This code is developed as part of the DIALS project and is provided for
# testing purposes only

"""Investigate the convergence radius of refinement by multiple refinement runs
doing random sampling of parameter space."""

# Python and cctbx imports
from __future__ import division
import sys
from math import pi
from scitbx import matrix

# Get class to build experimental models
from setup_geometry import extract

# Model parameterisations
from dials.scratch.dgw.refinement.detector_parameters import \
    detector_parameterisation_single_sensor
from dials.scratch.dgw.refinement.source_parameters import \
    source_parameterisation_orientation
from dials.scratch.dgw.refinement.crystal_parameters import \
    crystal_orientation_parameterisation, crystal_unit_cell_parameterisation
from dials.scratch.dgw.refinement import random_param_shift

# Reflection prediction
from dials.scratch.dgw.prediction import angle_predictor, impact_predictor
from rstbx.diffraction import full_sphere_indices
from cctbx.sgtbx import space_group, space_group_symbols

# Parameterisation of the prediction equation
from dials.scratch.dgw.refinement.prediction_parameters import \
    detector_space_prediction_parameterisation

# Imports for the target function
from dials.scratch.dgw.refinement.target import \
    least_squares_positional_residual_with_rmsd_cutoff, reflection_manager

# Import the refinement engine
from dials.scratch.dgw.refinement.engine import simple_lbfgs, lbfgs_curvs

def setup_models(seed):

    #############################
    # Setup experimental models #
    #############################

    override = "geometry.parameters.random_seed=" + str(seed)
    print override
    models = extract(local_overrides=override)

    mydetector = models.detector
    mygonio = models.goniometer
    mycrystal = models.crystal
    mysource = models.source

    ###########################
    # Parameterise the models #
    ###########################

    det_param = detector_parameterisation_single_sensor(mydetector.sensors()[0])
    src_param = source_parameterisation_orientation(mysource)
    xlo_param = crystal_orientation_parameterisation(mycrystal)
    xluc_param = crystal_unit_cell_parameterisation(mycrystal) # dummy, does nothing

    # Fix source to the X-Z plane (imgCIF geometry)
    src_param.set_fixed([True, False])

    # Fix crystal parameters
    xluc_param.set_fixed([True, True, True, True, True, True])

    ########################################################################
    # Link model parameterisations together into a parameterisation of the #
    # prediction equation                                                  #
    ########################################################################

    pred_param = detector_space_prediction_parameterisation(
    mydetector, mysource, mycrystal, mygonio, [det_param], [src_param],
    [xlo_param], [xluc_param])

    print "The initial experimental geometry is:"
    print "beam s0 = (%.4f, %.4f, %.4f)" % mysource.get_s0().elems
    print "sensor origin = (%.4f, %.4f, %.4f)" % mydetector.sensors()[0].origin
    print "sensor dir1 = (%.4f, %.4f, %.4f)" % mydetector.sensors()[0].dir1
    print "sensor dir2 = (%.4f, %.4f, %.4f)" % mydetector.sensors()[0].dir2
    uc = mycrystal.get_unit_cell()
    print "crystal unit cell = %.4f, %.4f, %.4f, %.4f, %.4f, %.4f" % uc.parameters()
    print "crystal orientation matrix U ="
    print mycrystal.get_U().round(4)
    print "\nInitial values of parameters are"
    msg = "Parameters: " + "%.5f " * len(pred_param)
    print msg % tuple(pred_param.get_p())
    print

    return(mydetector, mygonio, mycrystal, mysource,
           det_param, src_param, xlo_param, xluc_param, pred_param)

def run(mydetector, mygonio, mycrystal, mysource,
     det_param, src_param, xlo_param, xluc_param,
     pred_param):

    #################################
    # Apply random parameter shifts #
    #################################

    # shift detector by normal deviate of sd 2.0 mm each translation and 4 mrad
    # each rotation
    det_p = det_param.get_p()
    shift_det_p = random_param_shift(det_p, [2.0, 2.0, 2.0, 4.0, 4.0, 4.0])
    det_param.set_p(shift_det_p)

    # rotate beam by normal deviate with sd 4 mrad. There is only one free axis!
    src_p = src_param.get_p()
    shift_src_p = random_param_shift(src_p, [4.0])
    src_param.set_p(shift_src_p)

    # rotate crystal by normal deviates with sd 4 mrad for each rotation.
    xlo_p = xlo_param.get_p()
    shift_xlo_p = random_param_shift(xlo_p, [4.0, 4.0, 4.0])
    xlo_param.set_p(shift_xlo_p)

    target_param_values = tuple(pred_param.get_p())

    #############################
    # Generate some reflections #
    #############################

    # All indices in a 2.0 Angstrom sphere
    resolution = 2.0
    indices = full_sphere_indices(
        unit_cell = mycrystal.get_unit_cell(),
        resolution_limit = resolution,
        space_group = space_group(space_group_symbols(1).hall()))

    # Select those that are excited in a 180 degree sweep and get their angles
    UB = mycrystal.get_U() * mycrystal.get_B()
    ap = angle_predictor(mycrystal, mysource, mygonio, resolution)
    obs_indices, obs_angles = ap.observed_indices_and_angles_from_angle_range(
        phi_start_rad = 0.0, phi_end_rad = pi, indices = indices)

    # Project positions on camera
    ip = impact_predictor(mydetector, mygonio, mysource, mycrystal)
    #rp = reflection_prediction(mygonio.get_axis(), mysource.get_s0(), UB,
    #                           mydetector.sensors()[0])
    #hkls, d1s, d2s, angles, s_dirs = rp.predict(obs_indices.as_vec3_double(),
    #                                       obs_angles)
    hkls, d1s, d2s, angles, svecs = ip.predict(obs_indices.as_vec3_double(),
                                           obs_angles)

    # Invent some uncertainties
    im_width = 0.1 * pi / 180.
    sigd1s = [mydetector.px_size_fast() / 2.] * len(hkls)
    sigd2s = [mydetector.px_size_slow() / 2.] * len(hkls)
    sigangles = [im_width / 2.] * len(hkls)

    ###############################
    # Undo known parameter shifts #
    ###############################

    src_param.set_p(src_p)
    det_param.set_p(det_p)
    xlo_param.set_p(xlo_p)

    #####################################
    # Select reflections for refinement #
    #####################################

    rm = reflection_manager(hkls, svecs,
                            d1s, sigd1s,
                            d2s, sigd2s,
                            angles, sigangles,
                            mysource, mygonio)

    ##############################
    # Set up the target function #
    ##############################

    # The current 'achieved' criterion compares RMSD against 1/3 the pixel size and
    # 1/3 the image width in radians. For the simulated data, these are just made up
    mytarget = least_squares_positional_residual_with_rmsd_cutoff(
        rm, ap, ip, pred_param, mydetector.px_size_fast(), im_width)

    #TODO need to accept px_size_slow separately and have a separate RMSD criterion
    #for each direction

    ################################
    # Set up the refinement engine #
    ################################

    #refiner = simple_lbfgs(mytarget, pred_param)
    refiner = lbfgs_curvs(mytarget, pred_param)
    refiner.run()

    msg = "%d %s " + "%.5f " * len(pred_param)
    subs = ((refiner._step, str(refiner._target_achieved)) +
            target_param_values)
    print msg % subs

    ##########################
    # Reset parameter values #
    ##########################

    src_param.set_p(src_p)
    det_param.set_p(det_p)
    xlo_param.set_p(xlo_p)

    return refiner

if __name__ == "__main__":
    args = sys.argv[1:]
    try:
        seed = int(args[0])
    except IndexError:
        seed = 1
    if len(args) != 1: print "Usage:",sys.argv[0],"seed"

    (mydetector, mygonio, mycrystal, mysource,
        det_param, src_param, xlo_param, xluc_param,
        pred_param) = setup_models(seed)

    header = "Nsteps Completed " + "Param_%02d " * len(pred_param)
    print header % tuple(range(1, len(pred_param) + 1))

    for i in xrange(1000):
        sys.stdout.flush()
        output = run(mydetector, mygonio, mycrystal, mysource,
            det_param, src_param, xlo_param, xluc_param,
            pred_param)
