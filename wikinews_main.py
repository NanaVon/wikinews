import requests
import ProcessorText
import ConvertTexto
from bs4 import BeautifulSoup

def obtenNGramas(texto, n):
    return [texto[i:i+n] for i in range(len(texto)-(n-1))]
file= open("Myfile.txt", "w" )
url = 'https://www.lanacion.com.ar/politica/cristina-se-hace-cargo-presidencia-pero-no-nid2325650'
url1= "https://tn.com.ar/politica/cristina-kirchner-volvera-ejercer-la-presidencia-de-la-nacion-por-el-viaje-de-alberto-fernandez_1027213"

URL="https://tn.com.ar/politica/alberto-fernandez-viaja-israel-y-se-esperan-encuentros-con-lideres-mundiales_1027251"
URL1="https://tn.com.ar/politica/los-zocatruchos-de-anibal-fernandez-y-el-profe-romero-publicaron-noticias-falsas-para-difamar-nisman_1027170"


str=ConvertTexto.htmlToTxt(URL)
str=ProcessorText.removeCharactersNoAlfaNum(str)
str=ProcessorText.SacarAcento(str)
str=ProcessorText.convertirEnLista(str)

str1=ConvertTexto.htmlToTxt(URL1)
str1=ProcessorText.removeCharactersNoAlfaNum(str1)
str1=ProcessorText.SacarAcento(str1)
str1=ProcessorText.convertirEnLista(str1)

RES=ProcessorText.comparar(str, str1)
print(RES["lista"])