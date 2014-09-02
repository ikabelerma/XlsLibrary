Xls Library for Robot Framework
===============================

Introduction
------------
XlsLibrary is a library for reading (and soon, writing) spreadsheets saved as .xls files.
If you're looking at reading .xlsx files, you might be looking for ExcelXLibrary_.

XlsLibrary is just a Robot Framework wrapper for the xlrd python package.

Installation
------------

Since this is not a complete python package yet, there is no installation needed. Although the xlrd package is a pre-requisite:

::

    pip install xlrd

Just import XlsLibrary as a normal user library in your project. More information on importing user libraries in the `Robot Framework User Guide`_.

::

    *** Settings ***
    Library    XlsLibrary.py

.. _ExcelXLibrary: https://github.com/ikabelerma/ExcelXLibrary
.. _Robot Framework User Guide: http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#using-physical-path-to-library
