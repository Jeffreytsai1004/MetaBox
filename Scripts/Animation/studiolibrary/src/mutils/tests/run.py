#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Example:
# RUN TEST SUITE
import mutils.tests
reload(mutils.tests)
mutils.tests.run()
"""
import unittest

import logging


logging.basicConfig(
    filemode='w',
    level=logging.DEBUG,
    format='%(levelname)s: %(funcName)s: %(message)s',
)


def testSuite():
    """
    Return a test suite containing all the tests.

    :rtype: unittest.TestSuite
    """
    import test_pose
    import test_anim
    import test_match
    import test_utils
    import test_attribute
    import test_mirrortable

    suite = unittest.TestSuite()

    s = unittest.makeSuite(test_pose.TestPose, 'test')
    suite.addTest(s)

    s = unittest.makeSuite(test_anim.TestAnim, 'test')
    suite.addTest(s)

    s = unittest.makeSuite(test_utils.TestUtils, 'test')
    suite.addTest(s)

    s = unittest.makeSuite(test_match.TestMatch, 'test')
    suite.addTest(s)

    s = unittest.makeSuite(test_attribute.TestAttribute, 'test')
    suite.addTest(s)

    s = unittest.makeSuite(test_mirrortable.TestMirrorTable, 'test')
    suite.addTest(s)

    return suite


def run():
    """
    Call from within Maya to run all valid tests.
    """
    import mutils.animation
    mutils.animation.FIX_SAVE_ANIM_REFERENCE_LOCKED_ERROR = True

    tests = unittest.TextTestRunner()
    tests.run(testSuite())
