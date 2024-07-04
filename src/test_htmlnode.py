import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        props = HTMLNode("h1","Hello world", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(props.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_leaf_node(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text.</p>")
    
    def test_leaf_node_with_props(self):
        leaf_props = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_props.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_parent_node(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")