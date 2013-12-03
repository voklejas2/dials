from __future__ import division

class TestSimulated:

  def __init__(self):
    pass

  def run(self):
    self.tst_zero_intensity()

  def tst_zero_intensity(self):
    from math import sqrt
    from scitbx.array_family import flex
    counts = 0
    num = 1000
    rlist = self.generate_profiles(num, counts)
    I = []
    S = []
    for r in rlist:
      I.append(r.intensity)
      S.append(sqrt(r.intensity_variance))
    Z = [(i - counts) / s for i, s in zip(I, S)]
    mv = flex.mean_and_variance(flex.double(Z))
    meanz = mv.mean()
    varz = mv.unweighted_sample_variance()
    sdevz = sqrt(varz)
    print "Z: mean=%f, sdev=%f" % (meanz, sdevz)
    assert(abs(meanz - 0.0) < 1e-1)
    assert(abs(sdevz - 1.0) < 1e-1)
    print 'OK'

  def generate_profiles(self, num, counts):
    from dials.algorithms.simulation.generate_test_reflections import main
    from dials.algorithms.simulation.generate_test_reflections import \
      master_phil
    from libtbx.phil import command_line
    cmd = command_line.argument_interpreter(master_params = master_phil)
    working_phil = cmd.process_and_fetch(args = ["""
      nrefl = %d
      shoebox_size {
        x = 10
        y = 10
        z = 10
      }
      spot_size {
        x = 1
        y = 1
        z = 1
      }
      spot_offset {
        x = -0.5
        y = -0.5
        z = -0.5
      }
      mask_nsigma = 3.0
      counts = %d
      background = 10
      pixel_mask = all *static precise
      background_method = *xds mosflm
      integration_methpd = *xds mosflm
      output {
        over = None
        under = None
        all = all_refl.pickle
      }
      rotation {
        axis {
          x = 0
          y = 0
          z = 1
        }
        angle = 0
      }

      """ % (num, counts)])
    main(working_phil.extract())
    import cPickle as pickle
    return pickle.load(open("all_refl.pickle", "rb"))

if __name__ == '__main__':
  test = TestSimulated()
  test.run()
