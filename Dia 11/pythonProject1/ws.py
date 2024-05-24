import requests
from bs4 import BeautifulSoup
import tempfile
import webbrowser
from urllib.parse import urljoin
import html

def obtener_informacion_wikipedia(url):
    # Realiza la solicitud GET a la página web
    response = requests.get(url)

    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsea el contenido HTML de la página web
        soup = BeautifulSoup(response.content, 'html.parser', from_encoding=response.encoding)

        # Encuentra la tabla de información personal
        tabla = soup.find('table', class_='infobox biography vcard')

        # Verifica si se encontró la tabla
        if tabla:
            # Encuentra la etiqueta de la imagen dentro de la tabla
            imagen = tabla.find('img')

            # Obtiene la URL completa de la imagen
            if imagen:
                # Construir la URL completa de la imagen
                url_imagen = urljoin(url, imagen['src'])
                imagen_html = f'<img src="{url_imagen}" style="max-width: 100%; height: auto;">'
            else:
                imagen_html = "No se encontró la imagen en la tabla."

            # Construye una cadena HTML para mostrar la imagen
            html_output = f'<div>{imagen_html}</div>'

            # Encuentra todas las filas de la tabla
            filas = tabla.find_all('tr')

            # Itera sobre las filas e imprime los datos
            for fila in filas:
                # Encuentra todas las celdas de la fila
                celdas = fila.find_all(['th', 'td'])

                # Construye una cadena HTML para mostrar los datos de la fila
                fila_html = '<div style="margin-bottom: 10px;">'
                for celda in celdas:
                    # Usa html.escape para codificar caracteres especiales
                    fila_html += f'<span style="font-weight: bold;">{html.escape(celda.text.strip())}</span><br>'
                fila_html += '</div>'

                # Agrega los datos de la fila al resultado HTML
                html_output += fila_html

            return html_output

        else:
            return "No se encontró la tabla de información personal."
    else:
        return f"Error al acceder a la página: {response.status_code}"

# URL de las páginas de Wikipedia
urls = [
    'https://es.wikipedia.org/wiki/Sean_O%27Pry',
    'https://es.wikipedia.org/wiki/Ben_Affleck'
]

# Construir una caja HTML para cada página
cajas_html = []
for url in urls:
    informacion_html = obtener_informacion_wikipedia(url)
    caja_html = f'''
    <div style="max-width: 350px; background: #F8F9FD; background: linear-gradient(0deg, rgb(255, 255, 255) 0%, rgb(244, 247, 251) 100%); border-radius: 40px; padding: 25px 35px; border: 5px solid rgb(255, 255, 255); box-shadow: rgba(133, 189, 215, 0.8784313725) 0px 30px 30px -20px; margin: 20px; float: left; text-align: center;">
        <div style="margin-bottom: 20px;">
            {informacion_html}
        </div>
    </div>
    '''
    cajas_html.append(caja_html)

# Concatenar todas las cajas HTML en una sola cadena
html_output = ''.join(cajas_html)

# Crear el archivo HTML
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Información Wikipedia</title>
<style>
/* Estilos para hacer responsivo */
@media screen and (max-width: 600px) {{
  .caja {{
    float: none;
    width: 100%;
    margin-right: 0;
  }}
}}
</style>
</head>
<body>
{html_output}
</body>
</html>
"""

# Guardar el HTML en un archivo temporal
with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as f:
    f.write(html_content)

# Abrir el archivo en el navegador web predeterminado
webbrowser.open(f.name)
