#!/usr/bin/env python3
"""
To run these tests: set the Pythonpath to both the parent dir
(where the module 'game' is found), and to this dir -
(so that the "game"  imports our mocked-up "browser" module)
Run this file with (c)Python >= 3.3 
"""

import unittest
from unittest.mock import Mock
import sys

class TestGame(unittest.TestCase):
    def setUp(self):
        self.stdout = sys.stdout
        sys.stdout = open("/tmp/testoutput", "at")

    def tearDown(self):
        sys.stdout.close()
        sys.stdout = self.stdout
        sys.modules.pop("game", "")

    def test_game_module_is_loaded_with_no_syntax_error(self):
        import game

    def test_screen_is_created(self):
        import game
        self.assertIsInstance(game.SCREEN, Mock)
        self.assertIsInstance(game.SCREEN.getContext, Mock)
        game.SCREEN.getContext.assert_called_with("2d")

if __name__ == "__main__":
    unittest.main()


