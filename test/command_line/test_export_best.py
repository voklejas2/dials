from __future__ import absolute_import, division, print_function

import os
import procrunner

def test_export_best(dials_regression, tmpdir):
  tmpdir.chdir()
  path = os.path.join(
    dials_regression, "centroid_test_data", "centroid_####.cbf")

  result = procrunner.run(["dials.import", "template=" + path])
  assert not result['exitcode'] and not result['stderr']
  result = procrunner.run(["dials.find_spots", "datablock.json"])
  assert not result['exitcode'] and not result['stderr']
  result = procrunner.run(["dials.index", "datablock.json", "strong.pickle", "space_group=P422"])
  assert not result['exitcode'] and not result['stderr']
  result = procrunner.run([
      "dials.integrate",
      "experiments.json",
      "indexed.pickle",
      "prediction.padding=0",
      "sigma_m_algorithm=basic",
  ])
  assert not result['exitcode'] and not result['stderr']
  result = procrunner.run(["dials.export", "integrated_experiments.json", "integrated.pickle", "format=best"])
  assert not result['exitcode'] and not result['stderr']

  assert os.path.exists("best.dat")
  assert os.path.exists("best.hkl")
  assert os.path.exists("best.par")

  with open("best.dat", "r") as f:
    lines = ''.join(f.readlines()[:10])
  assert lines == """\
  191.5948       0.00       0.06
   63.8655       1.98       1.39
   38.3200       1.95       1.35
   27.3721       1.59       1.41
   21.2902       1.52       1.41
   17.4200       1.84       2.86
   14.7408       1.86       1.49
   12.7761       1.88       1.47
   11.2738       1.91       2.04
   10.0879       1.85       1.39
"""

  with open("best.hkl", "r") as f:
    lines = ''.join(f.readlines()[:10])
  assert lines == """\
 -20   27   -8      13.83      15.83
 -20   27   -7      84.99      17.93
 -20   27   -6      10.64      15.58
 -20   27   -5      -4.21      15.47
 -20   28  -10      23.96      15.17
 -20   28   -9      31.92      15.83
 -20   28   -7      31.47      16.59
 -20   28   -6      25.73      15.49
 -20   28   -4      -2.10      15.20
 -20   28   -2       7.77      15.53
"""

  with open("best.par", "r") as f:
    lines = f.read()
  assert lines == """\
# parameter file for BEST
TITLE          From DIALS
DETECTOR       PILA
SITE           Not set
DIAMETER       434.64
PIXEL          0.172
ROTAXIS        0.00 0.00 1.00 FAST
POLAXIS        0.00 1.00 0.00
GAIN               1.00
CMOSAIC            0.53
PHISTART           0.00
PHIWIDTH           0.20
DISTANCE         191.08
WAVELENGTH      0.97950
POLARISATION    0.99900
SYMMETRY       P422
UB             -0.012239 -0.020068  0.003150
               -0.004635 -0.000602 -0.024698
                0.019749 -0.012578 -0.003845
CELL              42.21    42.21    39.69  90.00  90.00  90.00
RASTER           7 7 5 3 3
SEPARATION      0.500  0.500
BEAM            219.861  212.607
# end of parameter file for BEST
"""
