import unittest

from textnode import TextNode, TextType, text_node_to_html_node

from markdown_ import extract_markdown_images, split_nodes_image, markdown_to_blocks

from blocktype import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is different", TextType.LINK)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is some anchor text", TextType.LINK, "https//www.boot.dev")
        html_node = text_node_to_html_node(node)
        html_node2 = text_node_to_html_node(node2)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node2.tag, "a")
        self.assertEqual(html_node2.value, "This is some anchor text")
        self.assertEqual(html_node2.props, "https//www.boot.dev")

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        line1 = "# This is a list\n- with items" 
        line2 = "```\nThis is a list\n- with items\n```"
        line3 = "> This is a list\n>- with items"
        line4 = "- This is a list\n- with items"
        line5 = "1. This is a list\n2. with items"
        line6 = "This is a list\n- with items"

        block_type1 = block_to_block_type(line1)
        block_type2 = block_to_block_type(line2)
        block_type3 = block_to_block_type(line3)
        block_type4 = block_to_block_type(line4)
        block_type5 = block_to_block_type(line5)
        block_type6 = block_to_block_type(line6)

        self.assertEqual(block_type1, BlockType.HEADING)
        self.assertEqual(block_type2, BlockType.CODE)
        self.assertEqual(block_type3, BlockType.QUOTE)
        self.assertEqual(block_type4, BlockType.UNORDERED_LIST)
        self.assertEqual(block_type5, BlockType.ORDERED_LIST)
        self.assertEqual(block_type6, BlockType.PARAGRAPH)


def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )


if __name__ == "__main__":
    unittest.main()
