import forca
import adivinho

def escolhe_jogo():
    print("********************************")
    print("*******Escolha o seu jogo*******")
    print("********************************")

    print("(1) Forca (2) Avinhação")

    jogo = int(input("Escolha o jogo: "))

    if(jogo==1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo==2):
        print("Jogando Avinhação")
        adivinho.jogar()

if(__name__=="__main__"):
    escolhe_jogo()
