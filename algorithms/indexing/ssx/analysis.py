import math
from typing import List

import numpy as np
from jinja2 import ChoiceLoader, Environment, PackageLoader

from scitbx.array_family import flex
from xfel.clustering.cluster import Cluster

from dials.algorithms.clustering import plots as cluster_plotter
from dials.util import tabulate


def generate_html_report(plots: dict, filename: str) -> None:
    loader = ChoiceLoader(
        [
            PackageLoader("dials", "templates"),
            PackageLoader("dials", "static", encoding="utf-8"),
        ]
    )
    env = Environment(loader=loader)
    template = env.get_template("simple_report.html")
    html = template.render(
        page_title="DIALS SSX indexing report",
        panel_title="Indexing plots",
        graphs=plots,
    )
    with open(filename, "wb") as f:
        f.write(html.encode("utf-8", "xmlcharrefreplace"))


def make_summary_table(results_summary: dict) -> tabulate:
    # make a summary table
    overall_summary_header = [
        "Image",
        "expt_id",
        "n_indexed",
        "RMSD X",
        "RMSD Y",
        "RMSD dPsi",
    ]

    rows = []
    total = 0
    if any(len(v) > 1 for v in results_summary.values()):
        show_lattices = True
        overall_summary_header.insert(1, "lattice")
    else:
        show_lattices = False
    for k in sorted(results_summary.keys()):
        for j, cryst in enumerate(results_summary[k]):
            if not cryst["n_indexed"]:
                continue
            n_idx, n_strong = (cryst["n_indexed"], cryst["n_strong"])
            frac_idx = f"{n_idx}/{n_strong} ({100*n_idx/n_strong:2.1f}%)"
            row = [
                cryst["Image"],
                str(total),
                frac_idx,
                cryst["RMSD_X"],
                cryst["RMSD_Y"],
                cryst["RMSD_dPsi"],
            ]
            if show_lattices:
                row.insert(1, j + 1)
            rows.append(row)
            total += 1

    summary_table = tabulate(rows, overall_summary_header)
    return summary_table


def combine_results_dicts(results_summaries: List[dict]) -> dict:
    """For a list of dictionaries, each with keys 0..n-1,
    combine into a single dictionary with keys 0..ntot-1"""
    combined_summary = {}
    n_overall = 0
    for d in results_summaries:
        n_this = len(d)
        for i in range(n_this):
            combined_summary[i + n_overall] = d.pop(i)
        n_overall += n_this
    return combined_summary


def make_cluster_plots(large_clusters: List[Cluster]) -> dict:
    cluster_plots = {}
    for n, cluster in enumerate(large_clusters):
        uc_params = [flex.double() for i in range(6)]
        for c in cluster.members:
            ucp = c.crystal_symmetry.unit_cell().parameters()
            for i in range(6):
                uc_params[i].append(ucp[i])
        d_this = cluster_plotter.plot_uc_histograms(uc_params)
        d_this["uc_scatter"]["layout"]["title"] += f" cluster {n+1}"
        d_this["uc_hist"]["layout"]["title"] += f" cluster {n+1}"
        d_this[f"uc_scatter_{n}"] = d_this.pop("uc_scatter")
        d_this[f"uc_hist_{n}"] = d_this.pop("uc_hist")
        cluster_plots.update(d_this)
    return cluster_plots


def generate_plots(summary_data: dict) -> dict:
    """Generate indexing plots from the summary data from index_all_concurrent"""
    # n_indexed_arrays are cumulative n_indexed for nth lattice
    n_indexed_arrays = [np.zeros(len(summary_data))]
    rmsd_x_arrays = [np.zeros(len(summary_data))]
    rmsd_y_arrays = [np.zeros(len(summary_data))]
    rmsd_z_arrays = [np.zeros(len(summary_data))]
    n_total_indexed = np.zeros(len(summary_data))
    n_strong_array = np.zeros(len(summary_data))
    images = np.arange(1, len(summary_data) + 1)
    n_lattices = 1

    for k in sorted(summary_data.keys()):
        n_lattices_this = len(summary_data[k])
        n_strong_array[k] = summary_data[k][0]["n_strong"]
        for j, cryst in enumerate(summary_data[k]):
            if not cryst["n_indexed"]:
                continue
            if n_lattices_this > n_lattices:
                for _ in range(n_lattices_this - n_lattices):
                    n_indexed_arrays.append(np.zeros(len(summary_data)))
                    rmsd_x_arrays.append(np.zeros(len(summary_data)))
                    rmsd_y_arrays.append(np.zeros(len(summary_data)))
                    rmsd_z_arrays.append(np.zeros(len(summary_data)))
                n_lattices = n_lattices_this
            n_indexed_arrays[j][k] = cryst["n_indexed"]
            rmsd_x_arrays[j][k] = cryst["RMSD_X"]
            rmsd_y_arrays[j][k] = cryst["RMSD_Y"]
            rmsd_z_arrays[j][k] = cryst["RMSD_dPsi"]
            n_total_indexed[k] += cryst["n_indexed"]

    n_indexed_data = [
        {
            "x": images.tolist(),
            "y": n_indexed_arrays[0].tolist(),
            "type": "scatter",
            "mode": "markers",
            "name": "N indexed",
        },
    ]
    rmsd_data = [
        {
            "x": images[rmsd_x_arrays[0] > 0].tolist(),
            "y": rmsd_x_arrays[0][rmsd_x_arrays[0] > 0].tolist(),
            "type": "scatter",
            "mode": "markers",
            "name": "RMSD X",
        },
        {
            "x": images[rmsd_y_arrays[0] > 0].tolist(),
            "y": rmsd_y_arrays[0][rmsd_y_arrays[0] > 0].tolist(),
            "type": "scatter",
            "mode": "markers",
            "name": "RMSD Y",
        },
    ]
    rmsdz_data = [
        {
            "x": images[rmsd_z_arrays[0] > 0].tolist(),
            "y": rmsd_z_arrays[0][rmsd_z_arrays[0] > 0].tolist(),
            "type": "scatter",
            "mode": "markers",
            "name": "RMSD dPsi",
        },
    ]
    if n_lattices > 1:
        n_indexed_data[0]["name"] += " (lattice 1)"
        rmsd_data[0]["name"] += " (lattice 1)"
        rmsd_data[1]["name"] += " (lattice 1)"
        rmsdz_data[0]["name"] += " (lattice 1)"
        for i, arr in enumerate(n_indexed_arrays[1:]):
            sub_images = images[arr > 0]
            sub_data = arr[arr > 0]
            n_indexed_data.append(
                {
                    "x": sub_images.tolist(),
                    "y": sub_data.tolist(),
                    "type": "scatter",
                    "mode": "markers",
                    "name": f"N indexed (lattice {i+2})",
                }
            )
        for i, arr in enumerate(rmsd_x_arrays[1:]):
            sub_images = images[arr > 0]
            sub_data_x = arr[arr > 0]
            sub_data_y = rmsd_y_arrays[i + 1][arr > 0]
            rmsd_data.append(
                {
                    "x": sub_images.tolist(),
                    "y": sub_data_x.tolist(),
                    "type": "scatter",
                    "mode": "markers",
                    "name": f"RMSD X (lattice {i+2})",
                },
            )
            rmsd_data.append(
                {
                    "x": sub_images.tolist(),
                    "y": sub_data_y.tolist(),
                    "type": "scatter",
                    "mode": "markers",
                    "name": f"RMSD Y (lattice {i+2})",
                },
            )
        for i, arr in enumerate(rmsd_z_arrays[1:]):
            sub_images = images[arr > 0]
            sub_data = arr[arr > 0]
            rmsdz_data.append(
                {
                    "x": sub_images.tolist(),
                    "y": sub_data.tolist(),
                    "type": "scatter",
                    "mode": "markers",
                    "name": f"RMSD dPsi (lattice {i+2})",
                },
            )
    percent_indexed = 100 * n_total_indexed / n_strong_array
    images = images.tolist()
    n_indexed_data.append(
        {
            "x": images,
            "y": n_strong_array.tolist(),
            "type": "scatter",
            "mode": "markers",
            "name": "N strong",
        },
    )

    percent_bins = np.linspace(0, 100, 51)
    percent_hist = np.histogram(percent_indexed, percent_bins)[0]

    def _generate_hist_data(rmsd_arrays, step=0.01):
        all_rmsd = np.concatenate(rmsd_arrays)
        all_rmsd = all_rmsd[all_rmsd > 0]
        mult = int(1 / 0.01)
        start = math.floor(np.min(all_rmsd) * mult) / mult
        stop = math.ceil(np.max(all_rmsd) * mult) / mult
        nbins = int((stop - start) / step)
        hist, bin_edges = np.histogram(
            all_rmsd,
            bins=nbins,
            range=(start, stop),
        )
        bin_centers = bin_edges[:-1] + np.diff(bin_edges) / 2
        return hist, bin_centers

    hist_x, bin_centers_x = _generate_hist_data(rmsd_x_arrays)
    hist_y, bin_centers_y = _generate_hist_data(rmsd_y_arrays)
    hist_z, bin_centers_z = _generate_hist_data(rmsd_z_arrays, 0.001)

    plots = {
        "n_indexed": {
            "data": n_indexed_data,
            "layout": {
                "title": "Number of indexed reflections per image",
                "xaxis": {"title": "image number"},
                "yaxis": {"title": "N reflections"},
            },
        },
        "percent_indexed": {
            "data": [
                {
                    "x": images,
                    "y": percent_indexed.tolist(),
                    "type": "scatter",
                    "mode": "markers",
                    "name": "Percentage of strong spots indexed",
                }
            ],
            "layout": {
                "title": "Percentage of strong spots indexed per image",
                "xaxis": {"title": "image number"},
                "yaxis": {"title": "Percentage"},
            },
        },
        "percent_indexed_hist": {
            "data": [
                {
                    "x": percent_bins.tolist(),
                    "y": percent_hist.tolist(),
                    "type": "bar",
                }
            ],
            "layout": {
                "title": "Distribution of percentage indexed",
                "xaxis": {"title": "Percentage indexed"},
                "yaxis": {"title": "Number of images"},
                "bargap": 0,
            },
        },
        "rmsds": {
            "data": rmsd_data,
            "layout": {
                "title": "RMSDs (x, y) per image",
                "xaxis": {"title": "image number"},
                "yaxis": {"title": "RMSD (px)"},
            },
        },
        "rmsdz": {
            "data": rmsdz_data,
            "layout": {
                "title": "RMSD (dPsi) per image",
                "xaxis": {"title": "image number"},
                "yaxis": {"title": "RMSD dPsi (deg)"},
            },
        },
        "rmsdxy_hist": {
            "data": [
                {
                    "x": bin_centers_x.tolist(),
                    "y": hist_x.tolist(),
                    "type": "bar",
                    "name": "RMSD X",
                    "opacity": 0.6,
                },
                {
                    "x": bin_centers_y.tolist(),
                    "y": hist_y.tolist(),
                    "type": "bar",
                    "name": "RMSD Y",
                    "opacity": 0.6,
                },
            ],
            "layout": {
                "title": "Distribution of RMSDs (x, y)",
                "xaxis": {"title": "RMSD (px)"},
                "yaxis": {"title": "Number of images"},
                "bargap": 0,
                "barmode": "overlay",
            },
        },
        "rmsdz_hist": {
            "data": [
                {
                    "x": bin_centers_z.tolist(),
                    "y": hist_z.tolist(),
                    "type": "bar",
                    "name": "RMSD dPsi",
                },
            ],
            "layout": {
                "title": "Distribution of RMSDs (dPsi)",
                "xaxis": {"title": "RMSD dPsi (deg)"},
                "yaxis": {"title": "Number of images"},
                "bargap": 0,
            },
        },
    }
    return plots
