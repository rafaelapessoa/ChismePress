import unittest
from utils.file_handler import convert_markdown_to_html, render_html

class TestChismePress(unittest.TestCase):
    def test_convert_markdown_to_html(self):
        markdown_content = "# Título\nTexto en **negrita**."
        html = convert_markdown_to_html(markdown_content)
        self.assertIn("<h1>Título</h1>", html)
        self.assertIn("<strong>negrita</strong>", html)

    def test_render_html(self):
        template_path = "templates/default.html"
        html = render_html(template_path, title="Prueba", content="<p>Contenido</p>")
        self.assertIn("<title>Prueba</title>", html)
        self.assertIn("<p>Contenido</p>", html)

if __name__ == "__main__":
    unittest.main()
