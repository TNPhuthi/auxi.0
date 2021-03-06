#!/usr/bin/env python3
"""
This module contains all the code used to test the testee module.
"""


import unittest
from os import remove
from os.path import realpath, dirname, join, isfile

from matplotlib import pyplot as plt

from auxi.tools.transportphenomena.heattransfer import naturalconvection as testee
from auxi.tools.materialphysicalproperties.gases import air


__version__ = '0.3.6'
__license__ = 'LGPL v3'
__copyright__ = 'Copyright 2016, Ex Mente Technologies (Pty) Ltd'
__author__ = 'Johan Zietsman'
__credits__ = ['Johan Zietsman']
__maintainer__ = 'Johan Zietsman'
__email__ = 'johan.zietsman@ex-mente.co.za'
__status__ = 'Planning'


MODULE_PATH = dirname(realpath(__file__))


class DimensionlessQuantitiesTester(unittest.TestCase):

    def test_Gr(self):
        pass

    def test_Pr(self):
        pass

    def test_Re(self):
        pass

    def test_Ra(self):
        pass

    def test_Nu(self):
        pass

    def test_Sh(self):
        pass
