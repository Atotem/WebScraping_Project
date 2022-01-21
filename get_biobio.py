def bio_bio(URL_1):
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    from Class_biobio import biobio



    #creación de archivo con la noticia, no es necesario pero puede ser util más adelante.

    #f=open("biobio.csv","w+")
    #headers="URL, CATEGORIA, FECHA, TITULO, COLABORADOR\n"
    #f.write(headers)


    try:#bio bio
        my_url = URL_1
        #abre conexion url bio bio
        uClient=uReq(my_url)
        page_html=uClient.read()
        uClient.close()
        #html parsing
        page_soup= soup(page_html, "html.parser")
    except:
        print("Error en conexión a página web")

    #toma todos los productos
    containers=page_soup.findAll("div",{"class":"nota-subseccion"})

    noticias = [0 for x in range(len(containers))]

    i=0
    for container in containers:
        try:
            #abre conexion url bio bio
            uClient=uReq(my_url)
            page_html=uClient.read()
            uClient.close()
            #html parsing
            page_soup= soup(page_html, "html.parser")
        except:
            print("Error en conexión a página web")

        url = container.select("a")[0]["href"]
    

        web=container.select("a")[0]["href"]
        #entra a url de la noticia
        try:
            uClient=uReq(web)
            page_html=uClient.read()
            uClient.close()
            #html parsing
            page_soup= soup(page_html, "html.parser")
        except:
            print("Error en conexión a página web")

        try:
            cat = page_soup.findAll("div",{"class":"categoria-titulo-nota"})[0].text.strip()

        except:
            #print('category error')
            cat = 'error'

        try:
            fecha = page_soup.findAll("div",{"class":"nota-fecha am-hide"})[0].text.strip().replace('\n', ' ').replace('\r', '')
        except:
            #print('fecha error')
            fecha = 'error'

        try:
            titulo = page_soup.findAll("div",{"class":"nota-titular robotos"})[0].text.strip()
        except:
            #print('titulo error')
            titulo = 'error'

        try:
            colab = page_soup.findAll("div",{"class":"autores"})[0].text.strip()
        except:
            #print('colaborator error')
            colab = 'error'
        
        noticias[i] = biobio()

        noticias[i].url = url
        noticias[i].cat = cat
        noticias[i].fecha = fecha
        noticias[i].titulo = titulo
        noticias[i].colab = colab

        #noticias[i].print_attr()
        noticias[i].print_ttl()

        i = i+1
    #f.close
    return noticias
