import unittest
import json
from app import extract_json

class TestAppFunctions(unittest.TestCase):
    def test_direct_json(self):
        sample = '{"title": "Test Title", "benefits": ["B1", "B2", "B3"], "description": "Short description"}'
        result = extract_json(sample)
        self.assertEqual(result["title"], "Test Title")
        self.assertEqual(len(result["benefits"]), 3)

    def test_markdown_code_block(self):
        sample = '```json\n{"title": "Bag", "benefits": ["Safe", "Waterproof", "Spacious"], "description": "A very great bag for daily commuting."}\n```'
        result = extract_json(sample)
        self.assertEqual(result["title"], "Bag")
        self.assertEqual(result["benefits"][0], "Safe")

    def test_surrounding_text_json(self):
        sample = 'Here is the response:\n{"title": "Earbuds", "benefits": ["Noise Cancelling", "Long Battery", "Eco-friendly"], "description": "Premium wireless audio."}\nHope this helps!'
        result = extract_json(sample)
        self.assertEqual(result["title"], "Earbuds")
        self.assertEqual(len(result["benefits"]), 3)

    def test_invalid_json(self):
        with self.assertRaises(ValueError):
            extract_json("Just random non-json text with no structure.")

if __name__ == "__main__":
    unittest.main()
