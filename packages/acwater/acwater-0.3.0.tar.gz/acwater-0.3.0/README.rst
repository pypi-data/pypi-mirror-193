ACwater Polymer
===============

Atmospheric correction of EnMAP hyperspectral data for water surfaces

**ACwater Polymer** implements a class to load an EnMAP object and
execute atmospheric correction for water surfaces. ACwater Polymer
requires *EnPT* for the EnMAP data processing and *Polymer* for the
atmospheric correction algorithm.

**Operating system** for installation is **linux**, tested on Debian
GNU/Linux 9.9 (stretch) - Linux 4.9.0-9-amd64 x86_64.

**Requirements** are
`EnPT <https://gitext.gfz-potsdam.de/EnMAP/GFZ_Tools_EnMAP_BOX/EnPT>`__
and `polymer <https://www.hygeos.com/polymer>`__.

**Installation** of EnPT follows `EnPT
instructions <https://enmap.git-pages.gfz-potsdam.de/GFZ_Tools_EnMAP_BOX/EnPT/doc/installation.html>`__.

Installation
------------

`Instructions <https://gitlab.awi.de/phytooptics/acwater/-/blob/master/docs/installation.rst>`__
basically include cloning and installing the package and its
dependencies using a python package manager. However, ACwater Polymer
and Polymer must be installed with EnPT in the same environment.

Features
--------

-  Level 1 class for connecting EnPT and Polymer.
-  Integration with database of simulated water spectra.

License
-------

This software is under `GNU General Public License
v3 <https://gitlab.awi.de/phytooptics/acwater/-/blob/develop/LICENSE>`__

Credits
-------

Credits are with Phytooptics at AWI.

This package was created with
`Cookiecutter <https://github.com/audreyr/cookiecutter>`__ and the
`audreyr <https://github.com/audreyr/cookiecutter-pypackage>`__ project
template.
