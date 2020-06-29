# pylint: disable=protected-access,missing-function-docstring, missing-class-docstring, missing-module-docstring
# -*- coding: utf-8 -*-
import unittest

from mystify.myst_contents_manager import MystContentsManager


class E2ETestSuite(unittest.TestCase):
    """E2e test cases."""

    @unittest.skip("NYI")
    def test_save(self):
        self.assertFalse(False, "Not yet implemented")


if __name__ == "__main__":
    unittest.main()
