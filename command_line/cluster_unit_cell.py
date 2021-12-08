# LIBTBX_PRE_DISPATCHER_INCLUDE_SH export PHENIX_GUI_ENVIRONMENT=1


import functools
import os

import iotbx.mtz
import iotbx.phil
from cctbx import crystal
from dxtbx.model import ExperimentList
from xfel.clustering.cluster import Cluster
from xfel.clustering.cluster_groups import unit_cell_info

import dials.util
from dials.util.multi_dataset_handling import assign_unique_identifiers
from dials.util.options import ArgumentParser, reflections_and_experiments_from_files

help_message = """
"""

phil_scope = iotbx.phil.parse(
    """
threshold = 5000
  .type = float(value_min=0)
  .help = 'Threshold value for the clustering'
plot {
  show = False
    .type = bool
  name = 'cluster_unit_cell.png'
    .type = path
  log = False
    .type = bool
    .help = 'Display the dendrogram with a log scale'
}
output.clusters = False
    .type = bool
    .help = "If True, the data will be split at the threshold value and a pair"
            "of output files will be created for each cluster"
"""
)


@dials.util.show_mail_handle_errors()
def run(args=None):
    usage = "dials.cluster_unit_cell [options] models.expt"

    parser = ArgumentParser(
        usage=usage,
        phil=phil_scope,
        read_experiments=True,
        read_reflections=True,
        check_format=False,
        epilog=help_message,
    )

    params, _, args = parser.parse_args(
        args, show_diff_phil=True, return_unhandled=True
    )
    reflections, experiments = reflections_and_experiments_from_files(
        params.input.reflections, params.input.experiments
    )
    crystal_symmetries = []

    if len(experiments) == 0:
        if not args:
            parser.print_help()
            exit(0)
        for arg in args:
            assert os.path.isfile(arg), arg
            mtz_object = iotbx.mtz.object(file_name=arg)
            arrays = mtz_object.as_miller_arrays(
                merge_equivalents=False, anomalous=False
            )
            crystal_symmetries.append(arrays[0].crystal_symmetry())
    else:
        crystal_symmetries = [
            crystal.symmetry(
                unit_cell=expt.crystal.get_unit_cell(),
                space_group=expt.crystal.get_space_group(),
            )
            for expt in experiments
        ]

    clusters = do_cluster_analysis(crystal_symmetries, params)
    if params.output.clusters:
        assert (
            len(reflections) == 1
        ), "To output split data, input must be a single reflection file"
        reflections = reflections[0]
        if not experiments.identifiers():
            experiments, reflections = assign_unique_identifiers(
                experiments, reflections
            )
        template = "{prefix}_{index:0{maxindexlength:d}d}.{extension}"
        experiments_template = functools.partial(
            template.format,
            prefix="cluster",
            maxindexlength=len(str(len(clusters) - 1)),
            extension="expt",
        )
        reflections_template = functools.partial(
            template.format,
            prefix="cluster",
            maxindexlength=len(str(len(clusters) - 1)),
            extension="refl",
        )
        clusters.sort(key=lambda x: len(x.members), reverse=True)
        for j, cluster in enumerate(clusters):
            ids = [m.lattice_id for m in cluster.members]
            sub_expt = ExperimentList([experiments[i] for i in ids])
            identifiers = sub_expt.identifiers()
            sub_refl = reflections.select_on_experiment_identifiers(identifiers)
            # renumber the ids to go from 0->n-1
            sub_refl.reset_ids()
            expt_filename = experiments_template(index=j)
            refl_filename = reflections_template(index=j)
            n = len(ids)
            print(f"Saving {n} lattices from cluster {j+1} to {expt_filename}")
            sub_expt.as_file(f"split_{j}.expt")
            print(f"Saving reflections from cluster {j+1} to {refl_filename}")
            sub_refl.as_file(f"split_{j}.refl")


def do_cluster_analysis(crystal_symmetries, params):
    lattice_ids = list(range(len(crystal_symmetries)))
    ucs = Cluster.from_crystal_symmetries(crystal_symmetries, lattice_ids=lattice_ids)

    if params.plot.show or params.plot.name is not None:
        if not params.plot.show:
            import matplotlib

            # http://matplotlib.org/faq/howto_faq.html#generate-images-without-having-a-window-appear
            matplotlib.use("Agg")  # use a non-interactive backend
        import matplotlib.pyplot as plt

        plt.figure("Andrews-Bernstein distance dendogram", figsize=(12, 8))
        ax = plt.gca()
        clusters, cluster_axes = ucs.ab_cluster(
            params.threshold,
            log=params.plot.log,
            ax=ax,
            write_file_lists=False,
            doplot=True,
        )
        print(unit_cell_info(clusters))
        plt.tight_layout()
        if params.plot.name is not None:
            plt.savefig(params.plot.name)
        if params.plot.show:
            plt.show()

    else:
        clusters, cluster_axes = ucs.ab_cluster(
            params.threshold, log=params.plot.log, write_file_lists=False, doplot=False
        )
        print(unit_cell_info(clusters))

    return clusters


if __name__ == "__main__":
    run()
