Validate MagmOc against `Schaefer et al. (2016) <http://stacks.iop.org/0004-637X/829/i=2/a=63?key=crossref.80f93f037970e1b0ba2e4e36e59ff5c1>`_
===========

Overview
--------

Results for Schaefer et al. 2016 taken from Fig. 4 (blue, solid line)
for GJ 1132b with 100 TO initial water content

This folder contains 2 subfolders for runs of **VPLanet**:

1) GJ_eps03_100TO_grey

    Planet name:               GJ1132b
    Initial water content:     100 TO
    Initial CO2 content:       0
    XUV absorption efficiency: 0.3
    Atmospheric flux model:    grey atmosphere

    To run this case:

    .. code-block:: bash

        vplanet vpl.in
        python plot_magmoc.py

    plot_magmoc.py will show individual
