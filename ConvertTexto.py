import requests
from bs4 import BeautifulSoup

def obtenNGramas(texto, n):
    return [texto[i:i+n] for i in range(len(texto)-(n-1))]
file= open("Myfile.txt", "w" )
url = 'https://www.clarin.com/sociedad/ultimo-eclipse-ano-medianoche-vera-seguirlo_0_xYh0tlln.html'

blacklist=['[documesnt]',
	'noscript',
	'header',
	'html',
	'meta',
	'head', 
	'input',
	'script']

    
def htmlToTxt(url):
    global blacklist
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    output = ''
    for t in text:
    	if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output.lower()

t=htmlToTxt(url)

#print(obtenNGramas(output, 3))
