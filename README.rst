Xls Library for Robot Framework
===============================

Introduction
------------
XlsLibrary is a library for reading (and soon, writing) spreadsheets saved as .xls files.
If you're looking at reading .xlsx files, you might be looking for XlsxLibrary_.

XlsLibrary is a Robot Framework wrapper for the Python-Excel_ packages (xlrd_ only at the moment) python package.

Installation
------------

Since this is not a complete python package yet, there is no installation needed. Although the xlrd package is a pre-requisite:

::

    pip install xlrd

Just import XlsLibrary as a normal user library in your project. More information on importing user libraries in the `Robot Framework User Guide`_.

::

    *** Settings ***
    Library    XlsLibrary.py


.. _xlrd: https://secure.simplistix.co.uk/svn/xlrd/trunk/xlrd/doc/xlrd.html?p=4966
.. _Python-Excel: http://www.python-excel.org
.. _XlsxLibrary: https://github.com/ikabelerma/XlsxLibrary
.. _Robot Framework User Guide: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#using-physical-path-to-library
