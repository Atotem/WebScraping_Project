from get_biobio import bio_bio 
from get_mega import mega
from auth import trends
""" while True:
    choice=input("En cual página quieres hacer webscrapping: \n 1)Bio Bio \n 2)Mega\n \n 3)Esc\n")
    if(choice=="1"):
        try:
            bio_bio("https://www.biobiochile.cl/lista/categorias/nacional")
            print("Webscrapping de bio bio finalizada exitosamente\n")
        except:
            print("Error en webscrapping de bio bio\n")
    elif(choice=="2"):
        try:
            mega('https://www.mega.cl/noticias/nacional/')
            print("Webscrapping de mega finalizada exitosamente\n")
        except:
            print("Error en webscrapping de mega\n")
    elif(choice=='3'):
        break
    else:
        print("Opción no válida\n")
        print(choice) """

if __name__ == "__main__":
    #Trends
    """ Trends = trends()
    for trend in Trends:
        print(Trends[trend]) """

    #Titles
    #noticiasB = 
    bio_bio("https://www.biobiochile.cl/lista/categorias/nacional")

    #noticiasM = 
    mega('https://www.mega.cl/noticias/nacional/')

    """ for noticia in noticiasB:
        noticiasB[noticia].print_ttl()

    for noticia in noticiasM:
        noticiasM[noticia].print_ttl() """
