DIALS 3.7.0 (2021-11-01)
========================

Features
--------

- Bootstrap support for MacOS M1 platforms. (`#1841 <https://github.com/dials/dials/issues/1841>`_)
- New ``dials.find_rotation_axis`` program optimises the rotation axis from strong spot positions prior to indexing. (`#1884 <https://github.com/dials/dials/issues/1884>`_)
- ``dials.import``: Allow importing templates with no template characters. (`#1840 <https://github.com/dials/dials/issues/1840>`_)
- ``dials.stills_process``: Performance improvements in Kapton absorption correction and in rare cases of highly mosaic crystals. (`#1846 <https://github.com/dials/dials/issues/1846>`_)
- ``dials.image_viewer`` Coordinates are now given in fast, slow order. (`#1849 <https://github.com/dials/dials/issues/1849>`_)
- ``dials.image_viewer``: Crystal basis vectors are now shown in the same colour as their predictions. (`#1855 <https://github.com/dials/dials/issues/1855>`_)
- ``dials.image_viewer``: Add the option to display the rotation axis (`#1856 <https://github.com/dials/dials/issues/1856>`_)
- ``dials.image_viewer``: Draw resolution rings for curved detectors. (`#1899 <https://github.com/dials/dials/issues/1899>`_)
- ``dials.import``: Unhandled files are now by default ignored. This means that e.g. ``*.log`` files alongside images will no longer prevent a successful import. Set ``ignore_unhandled=False`` to restore the previous behaviour. (`#1881 <https://github.com/dials/dials/issues/1881>`_)
- ``dials.scale``: Allow fixing of a particular correction with e.g. ``physical.correction.fix=absorption``. (`#1883 <https://github.com/dials/dials/issues/1883>`_)
- Installer now accepts a ``--raw-prefix`` option to use the target destination directly, instead of in a ``dials-X.Y`` subdirectory. (`#1896 <https://github.com/dials/dials/issues/1896>`_)


Bugfixes
--------

- ``dials.compute_delta_cchalf``: Fix crash when only using passing dataset/group. (`#1892 <https://github.com/dials/dials/issues/1892>`_)
- ``dials.find_bad_pixels``: Pixel coordinates are now reported in row-major order, and mask value is now set to 16, which corresponds internally to "noisy pixel". (`#1876 <https://github.com/dials/dials/issues/1876>`_)
- ``dials.find_rotation_axis``: removed unused parameter ``optimise={True|False}``. (`#1898 <https://github.com/dials/dials/issues/1898>`_)
- ``dials.report``: Don't show otherwise empty sections. (`#1875 <https://github.com/dials/dials/issues/1875>`_)


Improved Documentation
----------------------

- Improvements to 3DED tutorials. (`#1850 <https://github.com/dials/dials/issues/1850>`_)
- SARS-CoV-2 main protease tutorial: process in C2 rather than I2 setting for consistency with published structures. (`#1854 <https://github.com/dials/dials/issues/1854>`_)
- Removed outdated lysozyme nanocrystals tutorial. (`#1877 <https://github.com/dials/dials/issues/1877>`_)
- Add an associated projects page to the website. (`#1893 <https://github.com/dials/dials/issues/1893>`_)


Deprecations and Removals
-------------------------

- Bootstrap no longer allows creating Python 3.6 environments. (`#1852 <https://github.com/dials/dials/issues/1852>`_)
- ``dials.util.mp``: deprecate ``parallel_map()`` function and remove previously deprecated ``preserve_exception_message=`` parameters. (`#1860 <https://github.com/dials/dials/issues/1860>`_)


Misc
----

- `#1851 <https://github.com/dials/dials/issues/1851>`_, `#1853 <https://github.com/dials/dials/issues/1853>`_, `#1862 <https://github.com/dials/dials/issues/1862>`_, `#1865 <https://github.com/dials/dials/issues/1865>`_, `#1867 <https://github.com/dials/dials/issues/1867>`_, `#1869 <https://github.com/dials/dials/issues/1869>`_, `#1882 <https://github.com/dials/dials/issues/1882>`_, `#1887 <https://github.com/dials/dials/issues/1887>`_, `#1888 <https://github.com/dials/dials/issues/1888>`_, `#1889 <https://github.com/dials/dials/issues/1889>`_, `#1891 <https://github.com/dials/dials/issues/1891>`_, `#1894 <https://github.com/dials/dials/issues/1894>`_, `#1902 <https://github.com/dials/dials/issues/1902>`_


DIALS 3.6.2 (2021-09-21)
========================

Bugfixes
--------

- ``dials.reciprocal_lattice_viewer``: In cases with multiple lattices, "Crystal Frame" now aligns all crystal frames, rather than just the first. Unindexed reflections are no longer shown in this mode. (`#1868 <https://github.com/dials/dials/issues/1868>`_)


DIALS 3.6.1 (2021-09-06)
========================

No significant changes.


DIALS 3.6.0 (2021-08-16)
========================

This is the last release to support Python 3.6. Future releases will require a
minimum of Python 3.7.

Features
--------

- DIALS bootstrap now creates a Python 3.9 environment by default (`#1735 <https://github.com/dials/dials/issues/1735>`_)
- New program: ``dials.reference_profile_viewer`` for viewing reference profiles dumped by ``dials.integrate`` when using the ``debug.reference.output=True`` option. (`#1759 <https://github.com/dials/dials/issues/1759>`_)
- ``dials.combine_experiments``: Unindexed reflections are now included in the combined output (`#1760 <https://github.com/dials/dials/issues/1760>`_)
- ``dials.image_viewer``: Image overlays are now accumulated over stacks of images (`#1750 <https://github.com/dials/dials/issues/1750>`_)
- ``dials.image_viewer``: Allow control of the basis vector scale from the settings window (`#1780 <https://github.com/dials/dials/issues/1780>`_)
- ``dials.image_viewer``: Better colour choice for text overlays. Labels will now be light grey on Black, or Dark grey on White. The previous settings were sometimes hard to read on narrow-contrast images. (`#1781 <https://github.com/dials/dials/issues/1781>`_)
- ``dials.merge``: Include DANO/SIGDANO columns in output .mtz when ``anomalous=True`` and ``truncate=True`` (`#1809 <https://github.com/dials/dials/issues/1809>`_)
- ``dials.reciprocal_lattice_viewer``: Show resolution on the "nearest point" label (`#1770 <https://github.com/dials/dials/issues/1770>`_)
- ``dials.reciprocal_lattice_viewer`` now shows the path to the reflections in the title bar (`#1771 <https://github.com/dials/dials/issues/1771>`_)
- ``dials.reciprocal_lattice_viewer``: The default marker size now scaled automatically based on the data density (`#1773 <https://github.com/dials/dials/issues/1773>`_)
- ``dials.scale``: Always enable absorption correction if the ``absorption_level=`` parameter is set. Previously it was only enabled for sweeps >= 60° or if ``absorption_correction=True``. (`#1793 <https://github.com/dials/dials/issues/1793>`_)
- ``dials.scale``: Allow a shared absorption correction between sweeps if using the physical model, with the option ``share.absorption=True``. Extra absorption correction plots have also been added; and multiple sweeps are now aligned to the same reference frame. (`#1811 <https://github.com/dials/dials/issues/1811>`_)
- API: ``...scaling_library.scaled_data_as_miller_array`` now sets wavelength in the returned ``miller.array`` (`#1808 <https://github.com/dials/dials/issues/1808>`_)
- ``reflection_table.match()`` now returns ``flex.size_t`` index arrays, instead of ``flex.int``. (`#1784 <https://github.com/dials/dials/issues/1784>`_)
- New bootstrap option: ``--conda`` to install with miniconda instead of micromamba. (`#1730 <https://github.com/dials/dials/issues/1730>`_)


Bugfixes
--------

- ``dials.combine_experiments``: Correctly preserve mapping to images. This affects ``dials.image_viewer`` and ``dial.reciprocal_lattice_viewer``. (`#1093 <https://github.com/dials/dials/issues/1093>`_)
- ``dials.compute_delta_cchalf``: Unwarranted precision in the output has been reduced (`#1751 <https://github.com/dials/dials/issues/1751>`_)
- ``dials.find_spots``: Fix counting of imagesets in histogram output (`#1827 <https://github.com/dials/dials/issues/1827>`_)
- ``dials.image_viewer``: Add buttons to clear unit cell and generic ring display (`#1777 <https://github.com/dials/dials/issues/1777>`_)
- ``dials.image_viewer``: Fix various minor behavioural bugs in the spot-finding and image type controls. (`#1796 <https://github.com/dials/dials/issues/1796>`_)
- ``dials.import``: Fail gracefully when `#` is missing from template. (`#1840 <https://github.com/dials/dials/issues/1840>`_)
- ``dials.integrate``: change default filename of debug reference profile to ``reference_profiles.pickle``. (`#1747 <https://github.com/dials/dials/issues/1747>`_)
- ``dials.integrate``: Change default configuration so that unintegrated reflections are not retained. This helps reduce memory usage of downstream tools. Set ``output_unintegrated_reflections=True`` to restore the previous behaviour. (`#1753 <https://github.com/dials/dials/issues/1753>`_)
- ``dials.integrate``: ensure imageset_ids are always output. Affected use of image viewer, reciprocal lattice viewer on multi-sweep data. (`#1762 <https://github.com/dials/dials/issues/1762>`_)
- ``dials.reciprocal_lattice_viewer``: When starting with ``black_background=False``, ensure the rotation axis and beam vector are displayed in black. (`#1540 <https://github.com/dials/dials/issues/1540>`_)
- ``dials.reciprocal_lattice_viewer``: More robust beam centre control that works for multiple panel detectors (`#1842 <https://github.com/dials/dials/issues/1842>`_)
- ``dials.refine_bravais_settings``: correctly report mI Bravais settings (`#1825 <https://github.com/dials/dials/issues/1825>`_)
- ``dials.split_experiments``: Update the imageset_id column in the output reflection files. (`#1792 <https://github.com/dials/dials/issues/1792>`_)
- Don't fail ``bootstrap.py`` if a submodule is missing a reference (`#1834 <https://github.com/dials/dials/issues/1834>`_)

- Correctly handle reflection ``imageset_id`` column in ``dials.scale``, ``dials.cosym``, and ``dials.symmetry``. (`#1763 <https://github.com/dials/dials/issues/1763>`_)

Improved Documentation
----------------------

- ``dials.anvil_correction``: Made a small improvement to the developer documentation. (`#1788 <https://github.com/dials/dials/issues/1788>`_)
- Fix help string for ``best_monoclinic_beta=`` parameter (for ``dials.cosym``, ``dials.refine_bravais_settings`` and ``dials.symmetry``) (`#1833 <https://github.com/dials/dials/issues/1833>`_)
- Added a new tutorial on 3DED/MicroED data processing. (`#1837 <https://github.com/dials/dials/issues/1837>`_)
- Add a "Getting started" page to the documentation on the website. (`#1844 <https://github.com/dials/dials/issues/1844>`_)
- Add a tutorial on processing small molecule 3DED data. (`#1847 <https://github.com/dials/dials/issues/1847>`_)


Deprecations and Removals
-------------------------

- The previously deprecated ``dials.resolutionizer`` command has been removed. Please use ``dials.estimate_resolution`` instead. (`#1330 <https://github.com/dials/dials/issues/1330>`_)
- The previously deprecated ``dials.refine`` parameter ``trim_scan_edges`` has been removed. Please use ``scan_margin=...`` instead. (`#1374 <https://github.com/dials/dials/issues/1374>`_)
- The previously deprecated ``Spotfinder()()`` interface has been removed. Please use ``Spotfinder().find_spots()`` instead. (`#1484 <https://github.com/dials/dials/issues/1484>`_)
- The previously deprecated ``dials.util.masking.MaskGenerator`` has been removed. Please use ``dials.util.masking.generate_mask`` instead. (`#1569 <https://github.com/dials/dials/issues/1569>`_)
- The bootstrap option ``--mamba`` has become the default and will be removed in the future. (`#1730 <https://github.com/dials/dials/issues/1730>`_)
- ``dials.anvil_correction``:  Drop compatibility support for SciPy < 1.4 (`#1787 <https://github.com/dials/dials/issues/1787>`_)


Misc
----

- `#1746 <https://github.com/dials/dials/issues/1746>`_, `#1733 <https://github.com/dials/dials/issues/1733>`_, `#1752 <https://github.com/dials/dials/issues/1752>`_, `#1755 <https://github.com/dials/dials/issues/1755>`_, `#1756 <https://github.com/dials/dials/issues/1756>`_, `#1764 <https://github.com/dials/dials/issues/1764>`_, `#1767 <https://github.com/dials/dials/issues/1767>`_, `#1772 <https://github.com/dials/dials/issues/1772>`_, `#1783 <https://github.com/dials/dials/issues/1783>`_, `#1789 <https://github.com/dials/dials/issues/1789>`_, `#1791 <https://github.com/dials/dials/issues/1791>`_, `#1794 <https://github.com/dials/dials/issues/1794>`_, `#1795 <https://github.com/dials/dials/issues/1795>`_, `#1799 <https://github.com/dials/dials/issues/1799>`_, `#1802 <https://github.com/dials/dials/issues/1802>`_, `#1804 <https://github.com/dials/dials/issues/1804>`_, `#1806 <https://github.com/dials/dials/issues/1806>`_, `#1807 <https://github.com/dials/dials/issues/1807>`_, `#1812 <https://github.com/dials/dials/issues/1812>`_, `#1816 <https://github.com/dials/dials/issues/1816>`_, `#1817 <https://github.com/dials/dials/issues/1817>`_, `#1823 <https://github.com/dials/dials/issues/1823>`_, `#1830 <https://github.com/dials/dials/issues/1830>`_, `#1835 <https://github.com/dials/dials/issues/1835>`_, `#1836 <https://github.com/dials/dials/issues/1836>`_, `#1839 <https://github.com/dials/dials/issues/1839>`_


DIALS 3.5.4 (2021-07-27)
========================

Bugfixes
--------

- ``dials.stills_process``: Fix case where imagesets and experiment filenames could potentially disagree (`#1814 <https://github.com/dials/dials/issues/1814>`_)
- ``dials.scale``: Fix incorrect output files, for targeted scaling with more than one target dataset. (`#1815 <https://github.com/dials/dials/issues/1815>`_)
- ``dials.image_viewer``: Fix opening datasets with ``load_models=False`` (`#1818 <https://github.com/dials/dials/issues/1818>`_)


DIALS 3.5.3 (2021-07-12)
========================

Bugfixes
--------

- ``dials.image_viewer``: Fix the ``basis_vector_scale=`` parameter. (`#1769 <https://github.com/dials/dials/issues/1769>`_)


DIALS 3.5.2 (2021-06-28)
========================

Bugfixes
--------

- ``dials.image_viewer``: Fix display of spotfinding intermediates (threshold, dispersion, etc) when viewing multiple still experiments (`#1734 <https://github.com/dials/dials/issues/1734>`_)
- ``dials.image_viewer``: Stacking images no longer gives incorrect results for multi-sweep data beyond the first sweep (`#1758 <https://github.com/dials/dials/issues/1758>`_)


DIALS 3.5.1 (2021-06-14)
========================

No significant changes.


DIALS 3.5.0 (2021-05-27)
========================

Features
--------

- ``dials.integrate``: Avoid crash when data is too large to process in memory, by splitting into subsets (`#1392 <https://github.com/dials/dials/issues/1392>`_)
- New bootstrap options: ``--mamba`` to install with `micromamba <https://github.com/mamba-org/mamba#micromamba>`_, and ``--clean`` to remove installation caches immediately after completion. (`#1676 <https://github.com/dials/dials/issues/1676>`_)
- ``dials.find_spots_server``: Faster filtering of reflections by resolution (`#1680 <https://github.com/dials/dials/issues/1680>`_)
- ``dials.scale``: Add option ``error_model.grouping=`` to control refinement of either individual or grouped error models during scaling (`#1684 <https://github.com/dials/dials/issues/1684>`_)
- ``dials.scale``: Added ``physical.absorption_level=[low|medium|high]`` option for automatic setting of suitable absorption correction parameters. (`#1688 <https://github.com/dials/dials/issues/1688>`_)
- ``dials.cosym``: Significantly faster calculation of Rij matrix of pairwise correlation coefficients (`#1693 <https://github.com/dials/dials/issues/1693>`_)
- ``dials.sort_reflections`` and ``dials.merge_reflection_lists`` are now available without a ``dev.`` prefix. (`#1703 <https://github.com/dials/dials/issues/1703>`_)
- New command: ``dials.find_bad_pixels`` to identify pixels which are identified as signal in >= 50% of images (`#1710 <https://github.com/dials/dials/issues/1710>`_)
- ``dials.image_viewer``: Add selector to choose between a new default "image" and traditional "lab" coordinate frames. "image" frame attempts to align the fast/slow axes of the detector panels to screen x and y coordinates, so overall detector rotations will mostly be invisible. "lab" frame is the previous projection, where rotated detectors will appear rotated.
  ``dials.export_bitmaps``: Gained this same ``projection=`` option. (`#1716 <https://github.com/dials/dials/issues/1716>`_)
- ``dials.find_spots`` and ``dials.integrate``: `nproc=` now works with N > 1 on Windows. (`#1724 <https://github.com/dials/dials/issues/1724>`_)


Bugfixes
--------

- Fix rare crash in symmetry calculations when no resolution limit could be calculated (`#1641 <https://github.com/dials/dials/issues/1641>`_)
- ``dials.report``: Add units of pixels / images to centroid difference histograms (`#1677 <https://github.com/dials/dials/issues/1677>`_)
- ``dials.refine``: Scan-varying refinement failed when ``trim_scan_to_observations=False`` was used. (`#1686 <https://github.com/dials/dials/issues/1686>`_)
- ``dials.spot_counts_per_image``: Show an explicit error if given data that isn't spotfinding output (i.e. unindexed reflections/experiments). (`#1690 <https://github.com/dials/dials/issues/1690>`_)
- ``dials.integrate``: Improved background model variance calculation for integrating detectors. (`#1692 <https://github.com/dials/dials/issues/1692>`_)
- ``dials.stills_process``: improve processing performance by preventing re-reading of image data (`#1705 <https://github.com/dials/dials/issues/1705>`_)
- ``dials.background``: Correctly identify signal pixels for integrating detectors, and respect pre-calculated masks. (`#1726 <https://github.com/dials/dials/issues/1726>`_)
- ``dials.integrate``: Fixed bug in memory-use calculation for multi-sweep integration runs (`#1728 <https://github.com/dials/dials/issues/1728>`_)


Improved Documentation
----------------------

- Remove remaining 'master' references in the documentation. (`#1632 <https://github.com/dials/dials/issues/1632>`_)


Deprecations and Removals
-------------------------

- The previously deprecated ``dials.util.masking.MaskGenerator`` now prints a user warning. Please use ``dials.util.masking.generate_mask`` instead. (`#1643 <https://github.com/dials/dials/issues/1643>`_)
- ``dials.cosym``: Remove clustering code as this is no longer a necessary part of determination of symmetry or reindexing operations, and serves no useful purporse. (`#1647 <https://github.com/dials/dials/issues/1647>`_)
- ``dials.cosym``: ``nproc=`` parameter is deprecated. The algorithm is much faster on single cores. (`#1693 <https://github.com/dials/dials/issues/1693>`_)
- The pytest option ``--runslow`` was retired. The tests that it triggered will now always run. (`#1695 <https://github.com/dials/dials/issues/1695>`_)
- ``dev.dials.csv`` has been deprecated. Similar functionality is available with ``dials.export format=json``. (`#1708 <https://github.com/dials/dials/issues/1708>`_)
- ``dials.util.mp``: The ``preserve_exception_message`` argument has been deprecated. (`#1722 <https://github.com/dials/dials/issues/1722>`_)


Misc
----

- `#1631 <https://github.com/dials/dials/issues/1631>`_, `#1633 <https://github.com/dials/dials/issues/1633>`_, `#1648 <https://github.com/dials/dials/issues/1648>`_, `#1649 <https://github.com/dials/dials/issues/1649>`_, `#1652 <https://github.com/dials/dials/issues/1652>`_, `#1661 <https://github.com/dials/dials/issues/1661>`_, `#1672 <https://github.com/dials/dials/issues/1672>`_, `#1673 <https://github.com/dials/dials/issues/1673>`_, `#1674 <https://github.com/dials/dials/issues/1674>`_, `#1675 <https://github.com/dials/dials/issues/1675>`_, `#1676 <https://github.com/dials/dials/issues/1676>`_, `#1678 <https://github.com/dials/dials/issues/1678>`_, `#1679 <https://github.com/dials/dials/issues/1679>`_, `#1687 <https://github.com/dials/dials/issues/1687>`_, `#1696 <https://github.com/dials/dials/issues/1696>`_, `#1697 <https://github.com/dials/dials/issues/1697>`_, `#1698 <https://github.com/dials/dials/issues/1698>`_, `#1701 <https://github.com/dials/dials/issues/1701>`_, `#1706 <https://github.com/dials/dials/issues/1706>`_, `#1707 <https://github.com/dials/dials/issues/1707>`_, `#1711 <https://github.com/dials/dials/issues/1711>`_, `#1713 <https://github.com/dials/dials/issues/1713>`_, `#1717 <https://github.com/dials/dials/issues/1717>`_, `#1718 <https://github.com/dials/dials/issues/1718>`_, `#1720 <https://github.com/dials/dials/issues/1720>`_


DIALS 3.4.3 (2021-04-20)
========================

Bugfixes
--------

- ``dials.scale``: Fix crash when full-matrix minimisation is unsuccessful due to indeterminate normal equations. (`#1653 <https://github.com/dials/dials/issues/1653>`_)
- ``dials.scale``: Fix crash when no reflections remain after initial filtering. (`#1654 <https://github.com/dials/dials/issues/1654>`_)
- ``dials.export``: Fix error observed with ``format=mmcif`` for narrow sweeps with low symmetry (`#1656 <https://github.com/dials/dials/issues/1656>`_)
- Fix image numbering inconsistency in ascii histogram of per-image spot counts (`#1660 <https://github.com/dials/dials/issues/1660>`_)
- ``dials.find_spots_server``: Significant performance improvement for HDF5 grid scans. (`#1665 <https://github.com/dials/dials/issues/1665>`_)


DIALS 3.4.2 (2021-04-12)
========================

Bugfixes
--------

- Log messages from spot finding and integration no longer ignore logging level when using ``nproc > 1``. This mainly affects usage of dials from outside contexts. (`#1645 <https://github.com/dials/dials/issues/1645>`_)


DIALS 3.4.1 (2021-04-01)
========================

Features
--------

- ``dials.cosym``: Significantly faster via improved computation of functional, gradients and curvatures (`#1639 <https://github.com/dials/dials/issues/1639>`_)
- ``dials.integrate``: Added parameter ``valid_foreground_threshold=``, to require a minimum fraction of valid pixels before profile fitting is attempted (`#1640 <https://github.com/dials/dials/issues/1640>`_)


Bugfixes
--------

- ``dials.cosym``: Cache cases where Rij is undefined, rather than recalculating each time. This can have significant performance benefits when handling large numbers of sparse data sets. (`#1634 <https://github.com/dials/dials/issues/1634>`_)
- ``dials.cosym``: Fix factor of 2 error when calculating target weights (`#1635 <https://github.com/dials/dials/issues/1635>`_)
- ``dials.cosym``: Fix broken ``engine=scipy`` option (`#1636 <https://github.com/dials/dials/issues/1636>`_)
- ``dials.integrate``: Reject reflections with a high number of invalid pixels, which were being integrated since 3.4.0. This restores better merging statistics, and prevents many reflections being incorrect profiled as zero-intensity. (`#1640 <https://github.com/dials/dials/issues/1640>`_)


DIALS 3.4.0 (2021-03-15)
========================

Features
--------

- ``dials.integrate``: Profile-fitting improvements; Profile fitting will now be attempted on
  reflections with masked pixels, and the number of reflections qualifying for profile-fitting on
  multi-panel detectors has dramatically increased. (`#1297 <https://github.com/dials/dials/issues/1297>`_)
- ``dials.import``: When using ``reference_models=``, individual components of the model can be excluded with ``use_beam_reference=``, ``use_gonio_reference=`` and ``use_detector_reference=``. (`#1371 <https://github.com/dials/dials/issues/1371>`_)
- ``flex.reflection_table.match`` can now match reflections with configurable
  distance and scaling between any 3-vector column in the reflection tables. The
  default is still ``"xyzobs.px.value"``. (`#1398 <https://github.com/dials/dials/issues/1398>`_)
- ``dials.background``: Add option ``output.plot=`` to save an image to
  disk, instead of displaying interactively. Image files can now also be
  used directly. (`#1537 <https://github.com/dials/dials/issues/1537>`_)
- ``dials.import``: The default ``tolerance.scan.oscillation=`` is increased to
  3% of the image width, in order to accommodate electron diffraction datasets
  with poor rotation stages. (`#1543 <https://github.com/dials/dials/issues/1543>`_)
- ``dials.background``: Add support for multiple imagesets (`#1554 <https://github.com/dials/dials/issues/1554>`_)
- dials.estimate_resolution: reject Wilson outliers to minimise effect of spurious observations from e.g. ice rings on the resulting resolution estimates (`#1580 <https://github.com/dials/dials/issues/1580>`_)
- ``dials.cosym``: Use numpy in place of flex for large parts of cosym analysis (`#1581 <https://github.com/dials/dials/issues/1581>`_)
- ``dials.cosym``: Add option to use scipy `L-BFGS-B <https://docs.scipy.org/doc/scipy/reference/optimize.minimize-lbfgsb.html>` minimization engine (``minimization.engine=scipy``) (`#1581 <https://github.com/dials/dials/issues/1581>`_)
- New masking parameter ``disable_parallax_correction=False``. Set to ``True`` to speed up generation of resolution masks by disabling parallax correction (this is only likely to have significant effect when spotfinding is spread across many independent processes). (`#1590 <https://github.com/dials/dials/issues/1590>`_)
- ``dials.image_viewer``: New parameter ``basis_vector_scale=`` to adjust the length of the basis vector overlay (`#1598 <https://github.com/dials/dials/issues/1598>`_)
- ``dials.merge``: add option to set wavelength_tolerance for MAD datasets (`#1609 <https://github.com/dials/dials/issues/1609>`_)
- ``dials.reciprocal_lattice_viewer``: Added an option to label the reciprocal lattice point nearest the centre (`#1614 <https://github.com/dials/dials/issues/1614>`_)
- ``dials.scale``: An additional outlier rejection based on normalised intensities has been added (`#1627 <https://github.com/dials/dials/issues/1627>`_)


Bugfixes
--------

- ``dials.image_viewer``: Fix various display issues relating to viewing still images (`#1463 <https://github.com/dials/dials/issues/1463>`_)
- ``dials.background``: Fix crash when writing output plot with bad display configuration (`#1550 <https://github.com/dials/dials/issues/1550>`_)
- ``dials.scale``: Fix issue of error model not always being carried through after
  the profile/summation intensity combination step. (`#1566 <https://github.com/dials/dials/issues/1566>`_)
- Fail bootstrap step if the git checkout fails in a non-interactive or non-posix environment (`#1572 <https://github.com/dials/dials/issues/1572>`_)
- Fixes working towards direct support of Windows builds:

  * Fix build errors by ensuring conda environment is correctly set up. (`#1575 <https://github.com/dials/dials/issues/1575>`_)
  * Fix importing using paths with wildcards (`#1583 <https://github.com/dials/dials/issues/1583>`_)
  * Fix ``dials.*`` commands crashing when unicode output is directed to a file (`#1602 <https://github.com/dials/dials/issues/1602>`_)
  * Fix some type-related test failures (`#1608 <https://github.com/dials/dials/issues/1608>`_)


Improved Documentation
----------------------

- Describe how to fix gltbx build failures for development installations on non-RHEL distributions (`#1561 <https://github.com/dials/dials/issues/1561>`_)
- Replace references to ``.pickle`` with reflections / ``.refl`` in docstrings (`#1619 <https://github.com/dials/dials/issues/1619>`_)
- Add documentation for ``dials.filter_reflections`` to the website. (`#1625 <https://github.com/dials/dials/issues/1625>`_)


Deprecations and Removals
-------------------------

- Remove previously deprecated ``use_trusted_range=`` parameter from masking configuration (`#1156 <https://github.com/dials/dials/issues/1156>`_)
- The main development branch of dials was renamed from 'master' to 'main'. (`#1546 <https://github.com/dials/dials/issues/1546>`_)
- ``dials.background``: The ``plot=`` parameter to interactively display the background plot has
  been removed. Use ``output.plot=`` to save to file instead. (`#1554 <https://github.com/dials/dials/issues/1554>`_)
- Remove ``*.o`` files from the DIALS installer package (`#1564 <https://github.com/dials/dials/issues/1564>`_)
- ``dials.util.masking.MaskGenerator`` is deprecated in favour of ``dials.util.masking.generate_mask`` (`#1569 <https://github.com/dials/dials/issues/1569>`_)


Misc
----

- `#1530 <https://github.com/dials/dials/issues/1530>`_, `#1531 <https://github.com/dials/dials/issues/1531>`_, `#1532 <https://github.com/dials/dials/issues/1532>`_, `#1534 <https://github.com/dials/dials/issues/1534>`_, `#1535 <https://github.com/dials/dials/issues/1535>`_, `#1536 <https://github.com/dials/dials/issues/1536>`_, `#1542 <https://github.com/dials/dials/issues/1542>`_, `#1567 <https://github.com/dials/dials/issues/1567>`_, `#1570 <https://github.com/dials/dials/issues/1570>`_, `#1571 <https://github.com/dials/dials/issues/1571>`_, `#1588 <https://github.com/dials/dials/issues/1588>`_, `#1593 <https://github.com/dials/dials/issues/1593>`_, `#1597 <https://github.com/dials/dials/issues/1597>`_, `#1599 <https://github.com/dials/dials/issues/1599>`_, `#1600 <https://github.com/dials/dials/issues/1600>`_, `#1601 <https://github.com/dials/dials/issues/1601>`_, `#1603 <https://github.com/dials/dials/issues/1603>`_, `#1604 <https://github.com/dials/dials/issues/1604>`_, `#1613 <https://github.com/dials/dials/issues/1613>`_, `#1620 <https://github.com/dials/dials/issues/1620>`_, `#1621 <https://github.com/dials/dials/issues/1621>`_, `#1624 <https://github.com/dials/dials/issues/1624>`_, `#1626 <https://github.com/dials/dials/issues/1626>`_, `#1630 <https://github.com/dials/dials/issues/1630>`_


DIALS 3.3.4 (2021-03-05)
========================

Bugfixes
--------

- ``dials.import``: Selecting a subset of images with ``image_range=`` now works on stills (`#1592 <https://github.com/dials/dials/issues/1592>`_)
- `dials.search_beam_centre`: Dramatically improved execution time for large data sets (`#1612 <https://github.com/dials/dials/issues/1612>`_)
- ``dials.reindex``: Write ``.refl`` file output in the default
  "MessagePack" format for better compatibility with downstream programs (`#1616 <https://github.com/dials/dials/issues/1616>`_)
- ``dials.scale``: Fix rare memory crash from infinite loop, that could
  occur with very bad quality datasets (`#1622 <https://github.com/dials/dials/issues/1622>`_)


Improved Documentation
----------------------

- ``dials.refine``: More informative error message when reflections have weights of zero (`#1584 <https://github.com/dials/dials/issues/1584>`_)


DIALS 3.3.3 (2021-02-15)
========================

No changes to core DIALS in 3.3.3.


DIALS 3.3.2 (2021-02-01)
========================

Bugfixes
--------

- Remove unnecessary call to ``imageset.get_raw_data()`` while generating
  masks. This was causing performance issues when spotfinding. (`#1449 <https://github.com/dials/dials/issues/1449>`_)
- ``dials.export``: Allow data with either summation or profile fitted
  intensities to be exported. Previously, both were (erroneously)
  required to be present. (`#1556 <https://github.com/dials/dials/issues/1556>`_)
- ``dials.scale``: Fix crash if only summation intensities present and ``intensity_choice=combine`` (`#1557 <https://github.com/dials/dials/issues/1557>`_)
- Fix unicode logging errors on Windows (`#1565 <https://github.com/dials/dials/issues/1565>`_)


DIALS 3.3.1 (2021-01-18)
========================

Features
--------

- ``dials.index``: More verbose debug logs when rejecting crystal models that are inconsistent with input symmetry (`#1538 <https://github.com/dials/dials/issues/1538>`_)


Bugfixes
--------

- ``dials.stills_process``: Fix spotfinding error "Failed to remap experiment IDs" (`#1180 <https://github.com/dials/dials/issues/1180>`_)
- Improved spotfinding performance for HDF5 when using a single processor. (`#1539 <https://github.com/dials/dials/issues/1539>`_)


DIALS 3.3.0 (2021-01-04)
========================

Features
--------

- DIALS is now using `GEMMI <https://gemmi.readthedocs.io/>`_. (`#1266 <https://github.com/dials/dials/issues/1266>`_)
- Upgrade ``h5py`` requirement to 3.1+ for SWMR-related functionality. (`#1495 <https://github.com/dials/dials/issues/1495>`_)
- Added support for small integer types to DIALS flex arrays. (`#1488 <https://github.com/dials/dials/issues/1488>`_)
- ``dials.estimate_resolution``: Only use cc_half in default resolution analysis. (`#1492 <https://github.com/dials/dials/issues/1492>`_)
- ``dials.export``: Allow on-the-fly bzip2 or gzip compression for mmCIF
  output, because unmerged mmCIF reflection files are large. (`#1480 <https://github.com/dials/dials/issues/1480>`_)
- ``dials.find_spots`` and ``dials.integrate`` both now have ``nproc=Auto`` by
  default, which uses the number of allowed/available cores detected. (`#1441 <https://github.com/dials/dials/issues/1441>`_)
- ``dials.merge``: Report ``<dF/s(dF)>``, if ``anomalous=True``. An html report
  is also generated to plot this statistic. (`#1483 <https://github.com/dials/dials/issues/1483>`_)
- ``dials.scale``: Apply a more realistic initial error model, or load the
  existing error model, if rescaling. (`#1526 <https://github.com/dials/dials/issues/1526>`_)
- ``dials.stills_process``: allow using different saturation cutoffs for
  indexing and integration. Useful for using saturated reflections for indexing
  while still rejecting them during integration. (`#1473 <https://github.com/dials/dials/issues/1473>`_)


Bugfixes
--------

- Internal: Logging metadata is now preserved when running spotfinding and
  integration across multiple processes. (`#1484 <https://github.com/dials/dials/issues/1484>`_)
- Fix NXmx behaviour with h5py 3.1. (`#1523 <https://github.com/dials/dials/issues/1523>`_)
- ``dials.cosym``: Choose the cluster containing the most identity reindexing
  ops by default. Under some circumstances, particularly in the case of
  approximate pseudosymmetry, the previous behaviour could result in reindexing
  operators being chosen that weren't genuine indexing ambiguities, instead
  distorting the input unit cells. (`#1514 <https://github.com/dials/dials/issues/1514>`_)
- ``dials.estimate_resolution``: Handle very low multiplicity datasets without
  crashing, and better error handling. (`#1494 <https://github.com/dials/dials/issues/1494>`_)
- ``dials.export``,``dials.two_theta_refine``: Updates to mmcif output to
  conform to latest pdb dictionaries (v5). (`#1528 <https://github.com/dials/dials/issues/1528>`_)
- ``dials.find_spots``: fix crash when ``nproc=Auto``. (`#1019 <https://github.com/dials/dials/issues/1019>`_)
- ``dials.image_viewer``: Fix crash on newer wxPython versions. (`#1476 <https://github.com/dials/dials/issues/1476>`_)
- ``dials.index``: Fix configuration error when there is more than one lattice
  search indexing method. (`#1515 <https://github.com/dials/dials/issues/1515>`_)
- ``dials.merge``: Fix incorrect output of SigF, N+, N- in ``merged.mtz``. (`#1522 <https://github.com/dials/dials/issues/1522>`_)
- ``dials.reciprocal_lattice_viewer``: Fix error opening with wxPython 4.1+. (`#1511 <https://github.com/dials/dials/issues/1511>`_)
- ``dials.scale``: fix issues for some uses of multi-crystal rescaling if ``full_matrix=False``. (`#1479 <https://github.com/dials/dials/issues/1479>`_)


Improved Documentation
----------------------

- Update information on how to care for an existing development environment,
  and remove outdated information. (`#1472 <https://github.com/dials/dials/issues/1472>`_)
- Each of the available indexing strategies in ``dials.index`` now has some
  help text explaining how it works. You can view this help by calling
  ``dials.index -c -a1 -e1`` and looking for ``method`` under ``indexing``. (`#1519 <https://github.com/dials/dials/issues/1519>`_)
- Include ``__init__`` methods in autodoc generated library documentation. (`#1520 <https://github.com/dials/dials/issues/1520>`_)
- ``dials.estimate_resolution``: Improved documentation. (`#1493 <https://github.com/dials/dials/issues/1493>`_)


Deprecations and Removals
-------------------------

- ``dials.algorithms.spot_finding.finder.SpotFinder``: Use of ``__call__`` to
  run spotfinding has been deprecated in favor of ``SpotFinder.find_spots(experiments)``. (`#1484 <https://github.com/dials/dials/issues/1484>`_)


Misc
----

- `#1469 <https://github.com/dials/dials/issues/1469>`_, `#1481 <https://github.com/dials/dials/issues/1481>`_,
  `#1484 <https://github.com/dials/dials/issues/1484>`_, `#1487 <https://github.com/dials/dials/issues/1487>`_,
  `#1491 <https://github.com/dials/dials/issues/1491>`_, `#1496 <https://github.com/dials/dials/issues/1496>`_,
  `#1497 <https://github.com/dials/dials/issues/1497>`_, `#1498 <https://github.com/dials/dials/issues/1498>`_,
  `#1499 <https://github.com/dials/dials/issues/1499>`_, `#1500 <https://github.com/dials/dials/issues/1500>`_,
  `#1501 <https://github.com/dials/dials/issues/1501>`_, `#1514 <https://github.com/dials/dials/issues/1514>`_.


DIALS 3.2.3 (2020-12-07)
========================

Bugfixes
--------

- ``dials.slice_sequence``: Fix crash using ``block_size=`` option (`#1502 <https://github.com/dials/dials/issues/1502>`_)
- ``dials.scale``: Fix broken ``exclude_images=`` option (`#1509 <https://github.com/dials/dials/issues/1509>`_)


DIALS 3.2.2 (2020-11-23)
========================

Bugfixes
--------

- Fix case where ``dials.stills_process`` could swallow error messages
- ``dials.cosym``: Fix non-determinism. Repeat runs will now give identical results. (`#1490 <https://github.com/dials/dials/issues/1490>`_)
- Developers: Fix precommit installation failure on MacOS (`#1489 <https://github.com/dials/dials/issues/1490>`_)


DIALS 3.2.1 (2020-11-09)
========================

3.2 Branch releases will now use a fixed conda environment. This release
is the first to use the same versions of all dependencies as 3.2.0.

Bugfixes
--------

- ``dials.symmetry``, ``dials.cosym`` and ``dials.two_theta_refine``: Lowered
  default partiality_threshold from ``0.99`` to to ``0.4``. The previous
  default could occasionally result in too many reflections being rejected for
  particularly narrow wedges. (`#1470 <https://github.com/dials/dials/issues/1470>`_)
- ``dials.stills_process`` Improve performance when using MPI by avoiding
  unnecessary log file writing (`#1471 <https://github.com/dials/dials/issues/1471>`_)
- ``dials.scale``: Fix scaling statistics output of r_anom data. (`#1478 <https://github.com/dials/dials/issues/1478>`_)


DIALS 3.2.0 (2020-10-27)
========================

Features
--------

- DIALS development environments are now running Python 3.8 by default.  (`#1373 <https://github.com/dials/dials/issues/1373>`_)
- Add a scaled flag to the reflection table. Indicates which reflections are
  good after the scaling process.  (`#1377 <https://github.com/dials/dials/issues/1377>`_)
- Python warnings are now highlighted on the console log and written to log files  (`#1401 <https://github.com/dials/dials/issues/1401>`_)
- Exit error messages from commands will now be colourized  (`#1420 <https://github.com/dials/dials/issues/1420>`_)
- Change the way ``dials.integrate`` splits data into blocks, to reduce
  unnecessary data reads, increasing performance up to 35% in some cases  (`#1396 <https://github.com/dials/dials/issues/1396>`_)
- Add ``dials.util.mp.available_cores`` function  (`#1430 <https://github.com/dials/dials/issues/1430>`_)
- ``dials.refine``: Trimming scans to observations for scan-varying refinement can
  now be turned off, using the parameter ``trim_scan_to_observations=False``  (`#1374 <https://github.com/dials/dials/issues/1374>`_)
- ``dials.refine``: Change default to ``separate_panels=False``. This speeds up
  outlier rejection for multi-panel detectors. For metrology refinement this
  should be set to ``True``  (`#1424 <https://github.com/dials/dials/issues/1424>`_)
- ``dials.merge``: Add best_unit_cell option. If the best_unit_cell option is set
  in ``dials.scale``, this will now propagate to the merged mtz output file.  (`#1444 <https://github.com/dials/dials/issues/1444>`_)
- DIALS bootstrap now allow creating a Python 3.9 environment  (`#1452 <https://github.com/dials/dials/issues/1452>`_)
- DIALS now uses pytype for limited static type checking. We hope that this
  will, over time, improve code quality.  (`#1364 <https://github.com/dials/dials/issues/1364>`_)
- ``dials.stills_process``: Added ``process_percent=`` to restrict processing
  to a subset of data, sync reference geometry instead of overwriting it and
  handle composite spotfinding modes.  (`#1409 <https://github.com/dials/dials/issues/1409>`_)


Bugfixes
--------

- ``dials.stills_process``: Prevent memory usage getting too high by clearing the
  imageset cache during processing.  (`#1412 <https://github.com/dials/dials/issues/1412>`_)
- ``dials.find_spots_server``: Return HTTP 500 instead of 200 when running fails  (`#1443 <https://github.com/dials/dials/issues/1443>`_)
- ``dials.find_spots_server``: Fix multiprocessing-related crash on macOS with Python3.8  (`#1447 <https://github.com/dials/dials/issues/1447>`_)
- ``dials.integrate``: Fix failures when building with GCC 9  (`#1456 <https://github.com/dials/dials/issues/1456>`_)
- ``dials.image_viewer``: Fix deprecation warnings  (`#1462 <https://github.com/dials/dials/issues/1462>`_)
- ``dials.index``: When using local index assignment, take into account phi in
  nearest neighbour analysis. This can significantly improve indexing rates in
  some cases with scans > 360°  (`#1459 <https://github.com/dials/dials/issues/1459>`_)
- ``dials.reindex``: Show an error instead of crashing for bad reindex operations.  (`#1282 <https://github.com/dials/dials/issues/1282>`_)

Deprecations and Removals
-------------------------

- dials.refine: the parameter ``trim_scan_edges`` is renamed ``scan_margin``
  and the former name is deprecated  (`#1374 <https://github.com/dials/dials/issues/1374>`_)
- The developer command ``dev.dials.show_test_failure_reasons`` was removed.  (`#1436 <https://github.com/dials/dials/issues/1436>`_)
- Remove clipper sources from new development installations  (`#1437 <https://github.com/dials/dials/issues/1437>`_)


Misc
----

- `#1175 <https://github.com/dials/dials/issues/1175>`_, `#1337 <https://github.com/dials/dials/issues/1337>`_,
  `#1354 <https://github.com/dials/dials/issues/1354>`_, `#1379 <https://github.com/dials/dials/issues/1379>`_,
  `#1381 <https://github.com/dials/dials/issues/1381>`_, `#1400 <https://github.com/dials/dials/issues/1400>`_,
  `#1406 <https://github.com/dials/dials/issues/1406>`_, `#1416 <https://github.com/dials/dials/issues/1416>`_,
  `#1423 <https://github.com/dials/dials/issues/1423>`_, `#1426 <https://github.com/dials/dials/issues/1426>`_,
  `#1432 <https://github.com/dials/dials/issues/1432>`_, `#1433 <https://github.com/dials/dials/issues/1433>`_,
  `#1435 <https://github.com/dials/dials/issues/1435>`_, `#1446 <https://github.com/dials/dials/issues/1446>`_,
  `#1454 <https://github.com/dials/dials/issues/1454>`_, `#1466 <https://github.com/dials/dials/issues/1466>`_,
  `#1468 <https://github.com/dials/dials/issues/1468>`_


DIALS 3.1.4 (2020-10-12)
========================

No changes to core DIALS in 3.1.4.


DIALS 3.1.3 (2020-09-28)
========================

Bugfixes
--------

- ``dials.integrate``: fix integrator=3d_threaded crash if njobs > 1 (`#1410 <https://github.com/dials/dials/issues/1410>`_)
- ``dials.integrate``: Check for and show error message if shoebox data is missing (`#1421 <https://github.com/dials/dials/issues/1421>`_)
- ``dials.refine``: Avoid crash for experiments with zero reflections if the
  `auto_reduction.action=remove` option was active (`#1417 <https://github.com/dials/dials/issues/1417>`_)

Improved Documentation
----------------------

- ``dials.merge``: improve help message by adding usage examples (`#1413 <https://github.com/dials/dials/issues/1413>`_)
- ``dials.refine``: More helpful error message when too few reflections (`#1431 <https://github.com/dials/dials/issues/1431>`_)


DIALS 3.1.2 (2020-09-14)
========================

Features
--------

- ``dials.stills_process``: Add parameter ``max_images=`` to limit the number
  of processed images

Bugfixes
--------

- ``dials.integrate``: fix crash when run with integrator=3d_threaded (`#1404 <https://github.com/dials/dials/issues/1404>`_)
- ``dials.integrate``: Minor performance improvements (`#1399 <https://github.com/dials/dials/issues/1399>`_)
- ``dials.stills_process``: MPI performance improvements for large datasets
- ``dials.stills_process``: Fix error when using split logs


DIALS 3.1.1 (2020-09-01)
========================

Bugfixes
--------

- ``dials.scale``: Prevent discarding of resolution limits in rare cases, which
  could cause incorrect symmetry determination, and worse results. (`#1378 <https://github.com/dials/dials/issues/1378>`_)
- ``dials.cosym``: filter out experiments with inconsistent unit cells (`#1380 <https://github.com/dials/dials/issues/1380>`_)
- Internally slicing experiments now works if image range doesn't start at 1 (`#1383 <https://github.com/dials/dials/issues/1383>`_)
- Restore missing I/sigma(I) resolution estimate log output (`#1384 <https://github.com/dials/dials/issues/1384>`_)
- ``dials.image_viewer``: "Save As" button now works, for single panels
- Fix developer ``libtbx.precommit`` installation error (`#1375 <https://github.com/dials/dials/issues/1375>`_)


DIALS 3.1 (2020-08-17)
======================

Features
--------

- Supports Python 3.7 and 3.8. Python 3.6 remains the default. (`#1236 <https://github.com/dials/dials/issues/1236>`_)
- Switch DIALS environment to use conda compilers. For development environments,
  a new ``dials`` script, located above the build directory, replaces the
  existing 'setpaths'-family of scripts. This means that all commands within
  the conda environment will now be available. (`#1235 <https://github.com/dials/dials/issues/1235>`_)
- New command: ``dials.missing_reflections`` to identify connected regions of
  missing reflections in the asymmetric unit. (`#1285 <https://github.com/dials/dials/issues/1285>`_)
- Improvements to image stacking in ``dials.image_viewer``:
  - add pull-down selector for stacking mode
  - add modes for mean and max
  - add command-line selection for stacking mode
  - rename ``sum_images`` command-line option to ``stack_images`` (`#1302 <https://github.com/dials/dials/issues/1302>`_)
- Reduce volume of output in ``dials.integrate``; histograms and other less
  important information only shows in debug output. Pass the ``-vv`` option
  to restore the previous behaviour (`#1319 <https://github.com/dials/dials/issues/1319>`_)
- ``dials.integrate``: Experimental feature: Specifying
  ``output_unintegrated_reflections=False`` discards unintegrated data from
  output reflection file, for smaller output and faster post-processing (`#1343 <https://github.com/dials/dials/issues/1343>`_)
- Rename ``dials.resolutionizer`` command to ``dials.estimate_resolution``,
  and includes a html report. Writing png plot output is now turned off by
  default (passing ``plot=True`` will restore this behaviour). (`#1330 <https://github.com/dials/dials/issues/1330>`_)
- ``dials.scale`` now separates anomalous pairs during error model analysis (`#1332 <https://github.com/dials/dials/issues/1332>`_)
- ``dials.background``: Add parameter ``corrected=`` to optionally use
  pedestal-and-gain corrected data (`#1348 <https://github.com/dials/dials/issues/1348>`_)
- ``dials.combine_experiments``: Add option ``output.max_reflections_per_experiment=``,
  to reject experiments with too many reflections (`#1369 <https://github.com/dials/dials/issues/1369>`_)


Bugfixes
--------

- ``dials.image_viewer``: Shoeboxes are now shown rotated with rotated detector panels. (`#1189 <https://github.com/dials/dials/issues/1189>`_)
- ``dials.index``: In multi-lattice indexing, ensure that reflections where
  refinement fails are flagged as unindexed. (`#1350 <https://github.com/dials/dials/issues/1350>`_)
- ``dials.scale``: Reflections excluded from scaling are no longer permanently
  excluded from any subsequent ``dials.scale`` jobs. (`#1275 <https://github.com/dials/dials/issues/1275>`_)
- ``dials.scale``: When using ``intensity_choice=combine`` (the default), don't
  exclude reflections that only have one of summed or profiled intensities
  available, but not both. (`#1300 <https://github.com/dials/dials/issues/1300>`_)
- ``dials.split_experiments``: Don't generate extra leading zeros in the output
  filename when not required e.g. ``output_09.expt`` -> ``output_9.expt`` (`#1316 <https://github.com/dials/dials/issues/1316>`_)
- ``dials.plot_reflections``: Fix invisible white spots on white background. (`#1346 <https://github.com/dials/dials/issues/1346>`_)


Deprecations and Removals
-------------------------

- ``dials.find_spots``: Deprecate ``spotfinder.filter.use_trusted_range=`` (`#1156 <https://github.com/dials/dials/issues/1156>`_)
- ``setpaths.sh`` and related scripts in newly created DIALS development
  environments are made obsolete and will no longer work. (`#1235 <https://github.com/dials/dials/issues/1235>`_)
- ``dials.show``: Remove ``show_image_statistics=`` parameter. Use
  ``image_statistics.show_raw=`` for equivalent output (`#1306 <https://github.com/dials/dials/issues/1306>`_)
- Log files will omit timings unless the relevant dials program was run with ``-v`` (`#1313 <https://github.com/dials/dials/issues/1313>`_)

Misc
----

- `#1184 <https://github.com/dials/dials/issues/1184>`_, `#1216 <https://github.com/dials/dials/issues/1216>`_, `#1288 <https://github.com/dials/dials/issues/1288>`_, `#1312 <https://github.com/dials/dials/issues/1312>`_, `#1320 <https://github.com/dials/dials/issues/1320>`_, `#1322 <https://github.com/dials/dials/issues/1322>`_, `#1325 <https://github.com/dials/dials/issues/1325>`_, `#1328 <https://github.com/dials/dials/issues/1328>`_, `#1352 <https://github.com/dials/dials/issues/1352>`_, `#1365 <https://github.com/dials/dials/issues/1365>`_, `#1366 <https://github.com/dials/dials/issues/1366>`_, `#1370 <https://github.com/dials/dials/issues/1370>`_


DIALS 3.0.4 (2020-07-20)
========================

- ``dials.scale``: Allow usage of ``mode=image_group`` with ``filtering.method=deltacchalf`` when
  only providing a single data set (`#1334 <https://github.com/dials/dials/issues/1334>`_)
- ``dials.import``: When using a template and specifying an image_range, missing images outside of
  the range will not cause a failure (`#1333 <https://github.com/dials/dials/issues/1333>`_)
- ``dials.stills_process``: Show better error message in specific spotfinding failure case (`#1180 <https://github.com/dials/dials/issues/1180>`_)


DIALS 3.0.3 (2020-07-06)
========================

Features
--------

- Developer tool: On posix systems, sending SIGUSR2 to DIALS commands will now print a stack trace (`#1277 <https://github.com/dials/dials/issues/1277>`_)

Bugfixes
--------
- HTML reports: Plot bin centres instead bin minimum for d_min line plots vs. resolution (`#1323 <https://github.com/dials/dials/issues/1323>`_)
- ``dials.export``: Fix inconsistency in mtz export when given a non-reference (e.g. I2 or primitive) setting (`#1279 <https://github.com/dials/dials/issues/1279>`_)
- ``dials.refine_bravais_settings``: Fix crash with large (>2gb) reflection tables and reduce memory use (`#1274 <https://github.com/dials/dials/issues/1274>`_)
- ``dials.scale``: Fix bug in outlier rejection code causing misidentification of outliers (with outlier_rejection=standard).
- ``dials.scale``: Fix outlier rejection formula to avoid overconfidence in spuriously low values


DIALS 3.0.2 (2020-06-23)
========================

Bugfixes
--------

- Fix crash in scaling error model handling (`#1243 <https://github.com/dials/dials/issues/1243>`_)


DIALS 3.0.1 (2020-06-11)
========================

Features
--------

- dials.reciprocal_lattice_viewer: Add an option to show lattice(s) in the crystal rather than laboratory frame. (`#1259 <https://github.com/dials/dials/issues/1259>`_)
- Support for mtz project_name in export and scaling

Bugfixes
--------

- dials.reciprocal_lattice_viewer: fix multiple experiment view for integrated data (`#1284 <https://github.com/dials/dials/issues/1284>`_)


DIALS 3.0 (2020-05-22)
======================

Features
--------

- Show more useful output when crashing in C++ code (`#659 <https://github.com/dials/dials/issues/659>`_)
- dials.image_viewer: for the unit cell tool, rename parameters for consistency and add a new show_hkl option to filter displayed powder rings to select only those of interest. (`#1192 <https://github.com/dials/dials/issues/1192>`_)
- In dials.integrate: changed the background box size multiplier to be a parameter (sigma_b_multiplier) - setting to small values significantly reduces memory requirements. (`#1195 <https://github.com/dials/dials/issues/1195>`_)
- dials.image_viewer: add an overlaying showing pixels marked as strong by the spot-finding operations. That is, the pixels picked out by the "threshold" image. (`#1200 <https://github.com/dials/dials/issues/1200>`_)
- dials.scale report file was renamed from scaling.html to dials.scale.html
  dials.symmetry report file was renamed from dials-symmetry.html to dials.symmetry.html (`#1202 <https://github.com/dials/dials/issues/1202>`_)
- dials.report output file was renamed from dials-report.html to dials.report.html (`#1206 <https://github.com/dials/dials/issues/1206>`_)
- dials.image_viewer: faster navigation between different image types. (`#1213 <https://github.com/dials/dials/issues/1213>`_)
- Crystal model now has a new recalculated_unit_cell attribute. This allows it to store
  a post-refined unit cell (e.g. from dials.two_theta_refine) in addition to that from
  traditional geometry refinement (which was used for prediction). Downstream programs
  such as dials.scale and dials.export will now use the recalculated unit cell
  where appropriate. (`#1214 <https://github.com/dials/dials/issues/1214>`_)
- New best_monoclinic_beta parameter for dials.refine_bravais_settings and dials.symmetry.
  Setting this to False will ensure that C2 is selected in preference to I2, where I2
  would lead to a less oblique cell (i.e. smaller beta angle). (`#1226 <https://github.com/dials/dials/issues/1226>`_)
- New scaling model, model=dose_decay, implementing a shared exponential decay component for multicrystal experiments (`#1183 <https://github.com/dials/dials/issues/1183>`_)


Bugfixes
--------

- Avoid empty "Unable to handle" messages on failed dials.import (`#600 <https://github.com/dials/dials/issues/600>`_)
- Functions from dials.export now raise exceptions on errors rather than exit. This improves their use elsewhere (such as in dials.scale). (`#1205 <https://github.com/dials/dials/issues/1205>`_)
- Ensure dials.index chooses the C2 setting with the smallest beta angle (`#1217 <https://github.com/dials/dials/issues/1217>`_)
- Fix propagation of best_unit_cell and application of resolution cutoffs in dials.scale and export_mtz.
  Add a new mtz.best_unit_cell parameter to dials.export (`#1248 <https://github.com/dials/dials/issues/1248>`_)
- Make some of the DIALS tools furthest downstream (``dials.scale``, ``dials.symmetry``, ``dials.merge`` and ``dials.report``) more robust in the case of very few reflections. (`#1263 <https://github.com/dials/dials/issues/1263>`_)


Misc
----

- `#1221 <https://github.com/dials/dials/issues/1221>`_


DIALS 2.2 (2020-03-15)
======================

Features
--------

- dials.image_viewer: Add a choice between displaying the raw or the corrected image. (`#634 <https://github.com/dials/dials/issues/634>`_)
- Automatically choose between the `simple` and `glm` background determination
  algorithms, depending on whether the detector appears to be integrating or
  counting. (`#706 <https://github.com/dials/dials/issues/706>`_)
- Allow adjustment of font size for overlay text, such as Miller indices and
  resolution ring values. (`#1074 <https://github.com/dials/dials/issues/1074>`_)
- Keep goniometer and scan objects in indexing of still data, if provided in input (`#1076 <https://github.com/dials/dials/issues/1076>`_)
- Experimental: ``dials.image_viewer`` can be remotely controlled via a
  ZeroMQ endpoint with the ``zmq_endpoint`` PHIL parameter. Initially,
  the viewer can be commanded to load new images. This requires the
  (optional) ``pyzmq``package. (`#1085 <https://github.com/dials/dials/issues/1085>`_)
- Programs now generate a unique identifier for each experiment created, and reflection tables are linked via the experiment_identifiers map (`#1086 <https://github.com/dials/dials/issues/1086>`_)
- Introduce `dials.anvil_correction` to correct the absorption of the incident and diffracted X-ray beam by the diamond anvils in a pressure cell.
  Call `dials.anvil_correction` on the output of `dials.integrate` and then proceed to use post-integration tools as normal, just as though the sample had been measured in air. (`#1090 <https://github.com/dials/dials/issues/1090>`_)
- Map of detector efficiency for photon counting detectors as a function of
  detector position added to report, based on the qe value applied at the end
  of integration. (`#1108 <https://github.com/dials/dials/issues/1108>`_)
- Significantly reduce the amount of memory required to write .refl output files (`#1115 <https://github.com/dials/dials/issues/1115>`_)
- Add maximum_trusted_value=N option to spot finding to temporarily allow override of trusted range, e.g. to find overloaded spots in spot finding. (`#1157 <https://github.com/dials/dials/issues/1157>`_)
- array_family.flex interface has changed: background and centroid algorithms are
  set via public properties. Instead of flex.strategy use functools.partial with
  the same signature. as_miller_array() raises KeyError instead of Sorry.
  .extract_shoeboxes() lost its verbosity parameter, use log levels instead. (`#1158 <https://github.com/dials/dials/issues/1158>`_)
- dials.stills_process now supports imagesets of length > 1 (e.g. grid scans) (`#1174 <https://github.com/dials/dials/issues/1174>`_)


Bugfixes
--------

- Fixed prediction on images numbered zero, so integrating works correctly. (`#1128 <https://github.com/dials/dials/issues/1128>`_)
- Fix an issue (`#1097 <https://github.com/dials/dials/issues/1097>`_) whereby aggregating small numbers of reflections into resolution bins could sometimes result in empty bins and consequent errors. (`#1130 <https://github.com/dials/dials/issues/1130>`_)
- Ensure that restraints are ignored for parameterisations that are anyway fixed (`#1142 <https://github.com/dials/dials/issues/1142>`_)
- Fix dials.search_beam_centre to ensure that the correct detector models are
  output when multiple detector models are present in the input.
  Fix dials.search_beam_centre n_macro_cycles option (previously it was starting
  from the original geometry every macro cycle). (`#1145 <https://github.com/dials/dials/issues/1145>`_)
- dials.find_spots_server no longer slows down 3x when using resolution filters (`#1170 <https://github.com/dials/dials/issues/1170>`_)


Misc
----

- `#932 <https://github.com/dials/dials/issues/932>`_, `#1034 <https://github.com/dials/dials/issues/1034>`_, `#1050 <https://github.com/dials/dials/issues/1050>`_, `#1077 <https://github.com/dials/dials/issues/1077>`_


DIALS 2.1 (2019-12-12)
======================

Features
--------

- We now fully support Python 3 environments.
- MessagePack is now the default reflection table file format. Temporarily, the
  environment variable ``DIALS_USE_PICKLE`` can be used to revert to the previous
  pickle-based format, however this will be removed in a future version. (`#986 <https://github.com/dials/dials/issues/986>`_)
- new option for dials.show 'show_shared_models=True' displays which beam, crystal, and detector models are used across experiments (`#996 <https://github.com/dials/dials/issues/996>`_)
- Import still image sequence as N experiments dereferencing into one image set
  rather than one experiment. (`#1014 <https://github.com/dials/dials/issues/1014>`_)
- Add `reflection_table.get` method for defaulted column access (`#1031 <https://github.com/dials/dials/issues/1031>`_)


Bugfixes
--------

- Don't use -2 to indicate masked pixels, except for DECTRIS detectors where this
  is to be expected. (`#536 <https://github.com/dials/dials/issues/536>`_)
- No longer show pixels that are above the trusted range upper bound as
  "saturated" on the "variance" image. (`#846 <https://github.com/dials/dials/issues/846>`_)
- Correctly account for scan-varying crystals while providing a scan range to
  dials.integrate (`#962 <https://github.com/dials/dials/issues/962>`_)
- Ensure that generated masks do not include pixels that are overloaded on a few
  images, but only pixels that are always outside the trusted range. (`#978 <https://github.com/dials/dials/issues/978>`_)
- Rewritten parameter auto-reduction code for dials.refine provides finer-grained
  fixing of individual parameters rather than whole parameterisations and
  correctly takes constrained parameters into account (`#990 <https://github.com/dials/dials/issues/990>`_)
- Fix output of predictions in dials.refine.
  A recently-introduced bug meant that the updated predictions weren't
  being copied to the output reflections file. (`#991 <https://github.com/dials/dials/issues/991>`_)
- Allow scan-varying refinement where either the crystal cell or
  orientation is fixed. (`#999 <https://github.com/dials/dials/issues/999>`_)
- Respect batch= option to dials.symmetry - can reduce time taken for finding
  the symmetry for large data sets. (`#1000 <https://github.com/dials/dials/issues/1000>`_)
- Scan-varying refinement no longer fails when the scan is wider than the
  observed reflections (e.g. when the crystal has died). Instead, the scan
  is first trimmed to match the range of the diffraction. (`#1025 <https://github.com/dials/dials/issues/1025>`_)
- If convert_sequences_to_stills then delete the goniometer and scan. (`#1035 <https://github.com/dials/dials/issues/1035>`_)
- Correctly account for scan-varying crystals in dials.slice_sequence (`#1040 <https://github.com/dials/dials/issues/1040>`_)
- Eliminate systematic absences before applying change of basis op to minimum
  cell in dials.symmetry. (`#1064 <https://github.com/dials/dials/issues/1064>`_)


Improved Documentation
----------------------

- Add "Extending DIALS" page to developer documentation (`#893 <https://github.com/dials/dials/issues/893>`_)


Deprecations and Removals
-------------------------

- The command dials.analyse_output was removed.
  Its replacement, dials.report, will give you more useful output. (`#1009 <https://github.com/dials/dials/issues/1009>`_)


Misc
----

- `#983 <https://github.com/dials/dials/issues/983>`_, `#1004 <https://github.com/dials/dials/issues/1004>`_


DIALS 2.0 (2019-10-23)
======================

Features
--------

- Support exporting multi-dataset and still experiments to XDS_ASCII (`#637 <https://github.com/dials/dials/issues/637>`_)
- Replace default spotfinder with improved dispersion algorithm (`#758 <https://github.com/dials/dials/issues/758>`_)
- ``dials.report`` now displays oscillation data with units and more significant figures (`#896 <https://github.com/dials/dials/issues/896>`_)
- A new program, ``dials.sequence_to_stills`` to create split a sequence into a
  separate still Experiment for every scan point in the sequence, splitting
  reflections as necessary. (`#917 <https://github.com/dials/dials/issues/917>`_)
- Moved ``dials.export format=best`` to ``dials.export_best`` as that one needed
  access to the format object, the rest do not, and having ``dials.export`` work
  in the general case seems like a better idea... (`#921 <https://github.com/dials/dials/issues/921>`_)
- Unified logging output for dials programs - logs are no longer split into .log
  and .debug.log. Use -v to get debug output. (`#923 <https://github.com/dials/dials/issues/923>`_)
- New command ``dials.resolutionizer`` (replaces ``xia2.resolutionizer``). Add support for ``expt``/``refl``
  in ``dials.resolutionizer``. (`#933 <https://github.com/dials/dials/issues/933>`_)
- Changed the selection of reflections used for determination of the reflection
  profile parameters in integration. Now uses reflections which were previously
  used in refinement rather than all reflections, resulting in a speed
  improvement for large data sets and a negligible difference in the quality
  of the integrated results. (`#942 <https://github.com/dials/dials/issues/942>`_)
- ``dials.image_viewer`` now allows the choice between
  ``dispersion_extended`` (new default) and ``dispersion`` (old default)
  thresholding algorithms for investigating the effect of different
  spot-finding parameters. (`#948 <https://github.com/dials/dials/issues/948>`_)
- ``dials.rs_mapper`` now respects masked regions of images (including
  the trusted range mask). (`#955 <https://github.com/dials/dials/issues/955>`_)


Bugfixes
--------

- Fix and reinstate normalisation option in ``dials.option`` (`#919 <https://github.com/dials/dials/issues/919>`_)


Misc
----

- `#795 <https://github.com/dials/dials/issues/795>`_, `#862 <https://github.com/dials/dials/issues/862>`_, `#895 <https://github.com/dials/dials/issues/895>`_, `#915 <https://github.com/dials/dials/issues/915>`_, `#924 <https://github.com/dials/dials/issues/924>`_
