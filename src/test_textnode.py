import unittest

from textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TestTextNode(unittest.TestCase):
    def test_equal_nodes(self):
        node1 = TextNode("This is a text node", "bold", "https://www.example.com")
        node2 = TextNode("This is a text node", "bold", "https://www.example.com")
        self.assertEqual(node1, node2)

    def test_not_equal_nodes(self):
        node1 = TextNode("This is a text node 2", "bold", "https://www.example.com")
        node2 = TextNode("This is a text node 3", "bold", "https://www.example.com")
        self.assertNotEqual(node1, node2)

    def test_url_not_none(self):
        node = TextNode("This is a text node 2", "bold", "https://www.example.com")
        self.assertIsNotNone(node)

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        expected_repr = "TextNode('This is a text node', 'bold', 'https://www.boot.dev')"
        self.assertEqual(repr(node), expected_repr)




if __name__ == "__main__":
    unittest.main()
