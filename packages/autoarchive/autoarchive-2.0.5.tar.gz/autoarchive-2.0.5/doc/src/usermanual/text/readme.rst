.. readme.rst
.. 
.. Project: AutoArchive
.. License: GNU GPLv3
.. 
.. Copyright (C) 2003 - 2023 Róbert Čerňanský



.. User documentation - AutoArchive README file



==========================
AutoArchive ver. |release|
==========================

A simple backup utility.

Copyright (C) 2003 - 2023 Robert Cernansky



Program Description
===================

.. include:: ../general/description.rst
   :start-after: begin_description
   :end-before: end_description



Usage
=====

::

   aa [options] [command] [AA_SPEC ...]
   autoarchive [options] [command] [AA_SPEC ...]

For complete list of command line options please see the *aa*\(1) manual page or *AutoArchive User Manual*.

.. include:: ../general/description.rst
   :start-after: begin_usage
   :end-before: end_usage

*AA_SPEC* is the *archive specification file argument*.  It determines the `archive specification file` that shall be
processed.  None, single or multiple *AA_SPEC* arguments are allowed.  If option ``--all`` or command ``--list`` is
specified then no *AA_SPEC* argument is required.  Otherwise at least single *AA_SPEC* argument is required.  If it
contains the ".aa" extension then it is taken as the path to an archive specification file.  Otherwise, if specified
without the extension, the corresponding `.aa file` is searched in the `archive specifications directory`.



Contacting the Author
=====================

.. include:: ../general/general_information.rst
   :start-after: begin_author
   :end-before: end_author



.. |configs_reference_text| replace:: *aa.conf*\(5) and *aa_arch_spec*\(5) manual pages or *Configuration Files
   Description* and *Archive Specification File Description* sections in the *AutoArchive User Manual*

.. |tar_ref| replace:: 'tar'
