from os import system, path
system("clear")
try:
    if (path.exists(".ps.ngrok") == True):
        system("clear")
        print("INICIE O NGROK NA PORTA 8000\nCOMANDO E ESSE AI EM OUTRA ABA\ncd .ps.ngrok && chmod 777 ngrok && ./ngrok http 8000\n")
    else:
        system("apt install git")
        system("cd && git clone https://github.com/PSecurity/ps.ngrok")
        system("mv -v ps.ngrok .ps.ngrok")
        system("clear")
        print("INICIE O NGROK QUE JA FOI INSTALADO NO SEU TERMINAL\nCOMANDO E ESSE AI, EM OUTRA ABA\n cd .ps.ngrok && chmod 777 ngrok && ./ngrok http 8000")
except:
    print("Erro")

try:
    system("cd paginas && php -S localhost:8000")
except KeyboardInterrupt:
    system("python .serve.py")
