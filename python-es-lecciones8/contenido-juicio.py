# contenido-juicio.py

import urllib.request, urllib.error, urllib.parse, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

respuesta = urllib.request.urlopen(url)
HTML = respuesta.read()

print(obo.quitarEtiquetas(HTML))