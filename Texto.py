import requests
from tkinter import * 
import ProcessorText
import ConvertTexto
from bs4 import BeautifulSoup

ventana= Tk()

#def obtenNGramas(texto, n):
#    return [texto[i:i+n] for i in range(len(texto)-(n-1))]

def resultados(URL):
    str=ConvertTexto.htmlToTxt(URL)
    str=ProcessorText.removeCharactersNoAlfaNum(str)
    str=ProcessorText.SacarAcento(str)
    str=ProcessorText.convertirEnLista(str)

    return str
    
def get_selection():
    lista=resultados(noticia1.get())
    lista1=resultados(noticia.get())
    resultado=ProcessorText.comparar(lista,lista1)
    if resultado["CC"]>250:
        label.config(text="COINCIDENCIA")
    else:
        label.config(text="SIN CORRELACION")
    print(resultado)

#RES=ProcessorText.comparar(str, str1)

#print(RES["lista"])
noticia1=Entry(ventana)
noticia1.place(x=50, y=70)
noticia=Entry(ventana)
noticia.place(x=50, y=50)
button = Button(ventana, text="Obtener selección",command=get_selection)
button.place(x=50, y=20)
label = Label(ventana, text="")
label.config(font= 20)
label.place(x=50, y=100)
ventana.mainloop()