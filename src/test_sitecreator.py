import unittest
from sitecreator import extract_title

class TestSiteCreator(unittest.TestCase):
    def test_extract_title(self):
        markdown = """
# This is the Title
"""
        self.assertEqual("This is the Title", extract_title(markdown))