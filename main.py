from utils.file_handler import process_files
import argparse

def parse_arguments():
    """
    Configura y devuelve los argumentos de la línea de comandos.
    """
    parser = argparse.ArgumentParser(description="ChismePress: Un Generador de Sitios Estáticos.")
    parser.add_argument("directorio_markdown", help="Ruta al directorio que contiene los archivos Markdown.")
    parser.add_argument("-o", "--output", default="output", help="Directorio de salida para los archivos HTML generados.")
    parser.add_argument("-t", "--template", help="Ruta a un archivo de plantilla Jinja2.")
    return parser.parse_args()

if __name__ == "__main__":
    # Obtener argumentos
    args = parse_arguments()

    # Determinar la ruta de la plantilla
    template_path = args.template or "templates/default.html"

    # Procesar todos los archivos Markdown en el directorio especificado
    process_files(args.directorio_markdown, args.output, template_path)
