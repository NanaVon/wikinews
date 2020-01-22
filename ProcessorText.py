t1= "A través de un comunicado de prensa, así lo informó hoy la Secretaría de Finanzas. Allí, a su vez, informó que 'hasta el día 3 de enero de 2020 (inclusive) se recibirán propuestas de instituciones y asesores financieros relativas al diseño del proceso de gestión de la sostenibilidad de la deuda pública externa de la República Argentina' "
t2= "El cuerpo parcialmente calcinado hallado este jueves, entre pastizales, en una zona rural del departamento cordobés de San Justo, es el del médico ginecólogo Daniel Casermeiro, quien se hallaba desaparecido desde hace una semana, confirmó el fiscal a cargo de la investigación, Bernardo Alberione. Alberione ordenó que el cadáver sea trasladado a la morgue para la realización de la autopsia. En tanto, este viernes los encargados del operativo brindarán una conferencia de prensa, a las 11, para aportar mayor información sobre el caso."
t3= "aaaA "


l1=["2", "1", "4", "5", "6", "7", "8", "9", "10", "bajo"]
l2=["2", "11", "44", "1", "33", "13", "7", "11", "10", "bajo"]

def removeCharactersNoAlfaNum(str):
    signos ="?!¿¡'.,:?!¿¡.,:(){}"
    i=0

    while i<len(signos):
        if str.find(signos[i]) > -1:
            str=str.replace(signos[i], "")

        else:
            i=i+1
    return str
def convertirEnLista(str):
    return str.split()           
def SacarAcento(str):
    signos ="ÁáÉéíÍÓóÚú"
    i=0
    vocales="AaEeiIOoUu"

    while i<len(signos):
        if str.find(signos[i]) > -1:
            str=str.replace(signos[i], vocales[i])

        else:
            i=i+1
    return str

def contarPalabras(list):
    preposiciones=["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "segun", "sin", "so", "sobre", "tras", "versus","via"]
    i=0
    for item in list:
        if item in preposiciones:
            i=i
        else:
            i=i+1
    return i
    

def comparar(list, list1):
    CP=contarPalabras(list)
    a=[]
    preposiciones=["a","un","al" , "|", "los","las", "es", "una", "-" ,"en", "su", "y", ":" ,"la","que","se" , "el", "ante", "bajo", "cabe", "con", "contra", "de", "del", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "segun", "sin", "so", "sobre", "tras", "versus","via"]
    i=0
    e=0
    for item in list:
        if item in preposiciones:
            i=i
        elif item in list1:
            i=i+1
            if item in a:
                None
            else:
                a.append(item)
        else:
            e=e+1
    resultado = { "%":i/CP*100  , "CC":i, "CP": CP, "lista":a} #CC= CANTIDAD DE COINCIDENCIAS, CP= CANTIDAD DE PALABRAS NO PREPOSICIONES
    print(i)
    return resultado

def procesarText(str):
    str=SacarAcento(removeCharactersNoAlfaNum(str))
    return convertirEnLista(str)

t1=procesarText(t1)
t2=procesarText(t2)
#rint(comparar(t1,t2)["lista"])





#print(convertirEnLista(text))
