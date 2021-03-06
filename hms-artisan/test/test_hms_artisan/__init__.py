#!/usr/bin/env python

"""
Defines unit-tests for the module at .hms_artisan.
"""

#######################################
# Any needed from __future__ imports  #
# Create an "__all__" list to support #
#   "from module import member" use   #
#######################################

__all__ = [
    # Test-case classes
    # Child test-modules
]

#######################################
# Module metadata/dunder-names        #
#######################################

__author__ = 'Brian D. Allbee'
__copyright__ = 'Copyright 2018, all rights reserved'
__status__ = 'Development'

#######################################
# Standard library imports needed     #
#######################################

import os
import sys
import unittest

#######################################
# Third-party imports needed          #
#######################################

#######################################
# Local imports needed                #
#######################################

from idic.unit_testing import *

#######################################
# Initialization needed before member #
#   definition can take place         #
#######################################

#######################################
# Module-level Constants              #
#######################################

LocalSuite = unittest.TestSuite()

#######################################
# Import the module being tested      #
#######################################

import hms_artisan as hms_artisan
from hms_artisan import *

#######################################
# Code-coverage test-case and         #
# decorator-methods                   #
#######################################

class testhms_artisanCodeCoverage(ModuleCoverageTest):
    _testNamespace = ''
    _testModule = hms_artisan

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testhms_artisanCodeCoverage
   )
)

#######################################
# Test-cases in the module            #
#######################################

#######################################
# Child-module test-cases to execute  #
#######################################

import test_artisan_objects
LocalSuite.addTests(test_artisan_objects.LocalSuite._tests)

import test_data_storage
LocalSuite.addTests(test_data_storage.LocalSuite._tests)

# import child_module
# LocalSuite.addTests(child_module.LocalSuite._tests)

#######################################
# Imports to resolve circular         #
# dependencies. Avoid if possible.    #
#######################################

#######################################
# Initialization that needs to        #
# happen after member definition.     #
#######################################

#######################################
# Code to execute if file is called   #
# or run directly.                    #
#######################################

if __name__ == '__main__':
    import time
    results = unittest.TestResult()
    testStartTime = time.time()
    LocalSuite.run(results)
    results.runTime = time.time() - testStartTime
    PrintTestResults(results)
    if not results.errors and not results.failures:
        SaveTestReport(results, '.hms_artisan',
            '.hms_artisan.test-results')
