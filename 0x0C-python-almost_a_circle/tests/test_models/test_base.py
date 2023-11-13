#!/usr/bin/python3
"""Defines unittests for base.py."""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):  #checks __init__() method of Base without any arguments
        #Test that the id attribute increments when no custom ID is provided
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        # Test that the id attribute increments correctly for three instances
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)
        self.assertEqual(b2.id, b3.id - 1)

    def test_id_incrementation(self):
        # Test that each instance gets a unique ID
        base1 = Base()
        base2 = Base()
        base3 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_custom_id(self):
        # Test that instances can be created with a custom ID
        base_custom_id = Base(10)

        self.assertEqual(base_custom_id.id, 10)

    def test_negative_custom_id(self):
        # Test that instances cannot be created with a negative custom ID
        with self.assertRaises(ValueError):
            base_negative_id = Base(-1)

    def test_None_id(self):
        # Test that the id attribute increments when None is provided as custom ID
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        # Test that the id attribute is set to the specified custom ID
        self.assertEqual(12, Base(12).id)
    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

if __name__ == '__main__':
    unittest.main()
