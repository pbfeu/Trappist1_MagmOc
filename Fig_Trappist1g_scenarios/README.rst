Magma ocean evolution on TRAPPIST-1 g
===========

Overview
---------------

Solidification time of the magma ocean and desiccation time of the atmosphere
of TRAPPIST-1 g for initial water masses from 1-100 TO without CO2.
Evolution plots for three different scenarios are shown in a second plot.

Each subfolder contains the necessary files to run `VPLanet`/**MagmOc** for
TRAPPIST-1 g for different initial water masses.
To create the summary plot shown below, run the simulations and print the results
in each folder as follows:

To run this case:
---------------

.. code-block:: bash

    vplanet vpl.in
    python print_results.py

The results will be saved in a file `Results.dat` in each folders.
Do

.. code-block:: bash

    python combine_results.py
    python TR1_scenarios_g.py
    python TR1_scenarios_evolution.py

to combine all results in one file `Results_Trappist1_g.txt` and to print
the summary plot `Summary_Trappist1_scenarios_g.png` and the temperature and
pressure evolution for the three scenarios.




Expected output
---------------

.. figure:: Summary_Trappist1_scenarios_g.png
   :width: 600px
   :align: center

.. figure:: Plot_TR1_g_scenarios_evolution.png
  :width: 600px
  :align: center