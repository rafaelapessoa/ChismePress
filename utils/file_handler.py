import markdown
from jinja2 import Environment, FileSystemLoader
import os

def convert_markdown_to_html(markdown_content):
   
    return markdown.markdown(markdown_content)

def render_html(template_path, title, content):
    
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    return template.render(title=title, content=content)

def process_files(markdown_dir, output_dir, template_path):
    os.makedirs(output_dir, exist_ok=True)

    for root, _, files in os.walk(markdown_dir):
        for file in files:
            if file.endswith(".md"):
                try:
                    input_path = os.path.join(root, file)
                    with open(input_path, 'r', encoding='utf-8') as f:
                        markdown_content = f.read()

                    html_content = convert_markdown_to_html(markdown_content)
                    title = os.path.splitext(file)[0]
                    rendered_html = render_html(template_path, title=title, content=html_content)

                    output_path = os.path.join(output_dir, file.replace(".md", ".html"))
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(rendered_html)
                    print(f"Archivo procesado: {file} -> {output_path}")
                except Exception as e:
                    print(f"Error procesando el archivo {file}: {e}")


