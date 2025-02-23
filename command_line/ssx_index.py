# LIBTBX_SET_DISPATCHER_NAME dev.dials.ssx_index
"""
This program is a script to run indexing on the spotfinding results from a
still sequence i.e. SSX data. This scripts wraps a call to the regular
indexing code, and so all parameters from dials.index can be set here.

Saves the indexed result into a single experiment list/reflection table
with a joint detector and beam model. Also generates a html output report
showing indexing statistics as well as clustering statistics.

Usage:
    dev.dials.ssx_index imported.expt strong.refl
"""

import json
import logging
import math
import sys
import time

from cctbx import crystal
from libtbx import phil
from xfel.clustering.cluster import Cluster
from xfel.clustering.cluster_groups import unit_cell_info

from dials.algorithms.indexing.ssx.analysis import (
    generate_html_report,
    generate_plots,
    make_cluster_plots,
    make_summary_table,
)
from dials.algorithms.indexing.ssx.processing import index
from dials.util import log, show_mail_handle_errors
from dials.util.options import ArgumentParser, reflections_and_experiments_from_files
from dials.util.version import dials_version

try:
    from typing import List
except ImportError:
    pass

logger = logging.getLogger("dials")

program_defaults_phil_str = """
indexing {
  method = fft1d
  stills {
    indexer = stills
  }
}
output.log = dials.ssx_index.log
refinement {
  parameterisation {
    auto_reduction {
      min_nref_per_parameter = 1
      action = fix
    }
    beam.fix = all
    detector.fix = all
    scan_varying = False
  }
  reflections {
    weighting_strategy.override = stills
    outlier.algorithm = null
  }
}
"""

phil_scope = phil.parse(
    """
method = *fft1d *real_space_grid_search
    .type = choice(multi=True)
output.html = dials.ssx_index.html
    .type = str
output.json = None
    .type = str
include scope dials.command_line.index.phil_scope
""",
    process_includes=True,
).fetch(phil.parse(program_defaults_phil_str))

phil_scope.adopt_scope(
    phil.parse(
        """
    individual_log_verbosity = 1
    .type =int
"""
    )
)


@show_mail_handle_errors()
def run(args: List[str] = None, phil: phil.scope = phil_scope) -> None:
    """
    Run dev.dials.ssx_index as from the command line.

    This program takes an imported experiment list and a reflection table
    of strong spots and performs parallelised indexing for synchrotron
    serial crystallography experiments. This is done by calling the regular
    dials indexing code and capturing output to provide a html report, and
    outputs a multi-image indexed.expt and indexed.refl file containing the
    indexed data.
    """

    parser = ArgumentParser(
        usage="dev.dials.ssx_index imported.expt strong.refl [options]",
        read_experiments=True,
        read_reflections=True,
        phil=phil_scope,
        check_format=False,
        epilog=__doc__,
    )
    params, options = parser.parse_args(args=args, show_diff_phil=False)

    if not params.input.experiments or not params.input.reflections:
        parser.print_help()
        sys.exit()

    reflections, experiments = reflections_and_experiments_from_files(
        params.input.reflections, params.input.experiments
    )
    log.config(verbosity=options.verbose, logfile=params.output.log)
    params.individual_log_verbosity = options.verbose
    logger.info(dials_version())

    diff_phil = parser.diff_phil.as_str()
    if diff_phil:
        logger.info("The following parameters have been modified:\n%s", diff_phil)

    st = time.time()
    indexed_experiments, indexed_reflections, summary_data = index(
        experiments, reflections[0], params
    )

    summary_table = make_summary_table(summary_data)
    logger.info("\nSummary of images sucessfully indexed\n" + summary_table)

    n_images = len({e.imageset.get_path(0) for e in indexed_experiments})
    logger.info(f"{indexed_reflections.size()} spots indexed on {n_images} images\n")

    # print some clustering information
    ucs = Cluster.from_crystal_symmetries(
        [
            crystal.symmetry(
                unit_cell=expt.crystal.get_unit_cell(),
                space_group=expt.crystal.get_space_group(),
            )
            for expt in indexed_experiments
        ]
    )
    clusters, _ = ucs.ab_cluster(5000, log=None, write_file_lists=False, doplot=False)
    cluster_plots = {}
    min_cluster_pc = 5
    threshold = math.floor((min_cluster_pc / 100) * len(indexed_experiments))
    large_clusters = [c for c in clusters if len(c.members) > threshold]
    large_clusters.sort(key=lambda x: len(x.members), reverse=True)

    if large_clusters:
        logger.info(
            f"""
Unit cell clustering analysis, clusters with >{min_cluster_pc}% of the number of crystals indexed
"""
            + unit_cell_info(large_clusters)
        )
        if params.output.html or params.output.json:
            cluster_plots = make_cluster_plots(large_clusters)
    else:
        logger.info(
            f"No clusters found with >{min_cluster_pc}% of the number of crystals."
        )

    logger.info(f"Saving indexed experiments to {params.output.experiments}")
    indexed_experiments.as_file(params.output.experiments)
    logger.info(f"Saving indexed reflections to {params.output.reflections}")
    indexed_reflections.as_file(params.output.reflections)

    if params.output.html or params.output.json:
        summary_plots = generate_plots(summary_data)
        if cluster_plots:
            summary_plots.update(cluster_plots)
        if params.output.html:
            generate_html_report(summary_plots, params.output.html)
        if params.output.json:
            with open(params.output.json, "w") as outfile:
                json.dump(summary_plots, outfile)

    logger.info(f"Total time: {time.time() - st:.2f}s")


if __name__ == "__main__":
    run()
