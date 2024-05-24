from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

# URL base de la página web
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# Función para obtener la información de los libros de una página específica
def obtener_info_libros(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    product_pods = soup.find_all('article', class_='product_pod')
    libros_html = ''  # Variable para almacenar el contenido HTML de todas las cajas de libros
    for pod in product_pods:
        star_rating = pod.find('p', class_='star-rating')
        if star_rating and 'Five' in star_rating['class']:
            image_container = pod.find('div', class_='image_container')
            image_url_relative = image_container.find('img')['src']
            image_url_absolute = urljoin(url, image_url_relative)
            price_container = pod.find('div', class_='product_price')
            if price_container:
                price = price_container.find('p', class_='price_color').text.strip()
                # Genera el contenido HTML de la caja del libro
                libro_html = f"""
                    <div class="book-card">
                        <img src="{image_url_absolute}" alt="Libro">
                        <p class="price">{price}</p>
                    </div>
                """
                libros_html += libro_html  # Agrega el contenido HTML de la caja del libro a la variable
    return libros_html

# URL de la primera página
page_url = base_url.format(1)

# Obtenemos la información de los libros de la primera página
contenido_html = obtener_info_libros(page_url)

# Escribir el contenido HTML en un archivo
with open('libros.html', 'w', encoding='utf-8') as f:
    f.write(f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Libros</title>
            <style>
                /* Estilos para las cajas de libros */
                .book-card {{
                    width: 200px; /* Ancho de la caja del libro */
                    border: 1px solid #ddd; /* Borde */
                    border-radius: 10px; /* Borde redondeado */
                    padding: 10px; /* Espacio interior */
                    text-align: center; /* Centrado del contenido */
                    margin: 10px; /* Margen exterior */
                    display: inline-block; /* Mostrar en línea */
                }}

                .book-card img {{
                    max-width: 100%; /* Ajustar imagen al contenedor */
                    height: auto; /* Evitar deformación de la imagen */
                    margin-bottom: 10px; /* Espacio inferior */
                }}

                .book-card p.price {{
                    font-size: 16px; /* Tamaño del texto del precio */
                    color: #555; /* Color del texto del precio */
                }}
            </style>
        </head>
        <body>
            {contenido_html}
        </body>
        </html>
    """)

# Abrir el archivo en un navegador
import webbrowser
webbrowser.open('libros.html')