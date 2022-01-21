def mega(URL_1):
	#import bs4
	from urllib.request import urlopen as uReq
	from bs4 import BeautifulSoup as soup
	from Class_mega import mega

	try:
		my_url = URL_1
		uClient = uReq(my_url)
		page_html = uClient.read()
		uClient.close()
		#html parsing
		page_soup = soup(page_html, "html.parser")
	except:
		print("Error en conexión página web")

	a=page_soup.findAll("div",{"class":"bottom"})
	#print(len(a))


	noticias = [0 for x in range(len(a))]

	i=0

	for container in a:
		try:
			#abre conexion url mega
			uClient=uReq(my_url)
			page_html = uClient.read()
			uClient.close()
			#html parsing
			page_soup = soup(page_html,"html.parser")
		except:
			print("error en conexión página web")
		
		#imprime el URL
		if(container.select("a")[0]["href"]=="http://www.mega.cl/home/"):
			break

		url = container.select("a")[0]["href"]

		if(container.select("h1")==[]):
			titulo = str(container.select("h2"))
		else:
			titulo = str(container.select("h1"))

		
		web=container.select("a")[0]["href"]
		try:
			#entra a url de la noticia
			uClient=uReq(web)
			page_html=uClient.read()
			uClient.close()
			#html parsing
			page_soup= soup(page_html, "html.parser")
			#Imprime el autor de la noticia
		except:
			print("Error en conexión en página web")


		try:
			autor = page_soup.findAll("span",{"class":"periodista"})[0].text.strip()
		except:
			autor = "Error en el formato (Autor) html de la pagina"

		#Imprime la categoria
		try:
			cat = page_soup.findAll("ul",{"class":"tag-fecha"})[0].text.strip()
		except:
			cat = "Error en el formato (categoria) html de la pagina"

		#Imprime la fecha, esta wea deberia imprimir la fecha, pero utiliza etiquetas raras y no se como trabajarlo
		try:
			fecha = page_soup.findAll("time",{"datetime":"2019-10-07T10:02:00-03:00 10:02"})[0].text.strip().replace('\n', ' ').replace('\r', '')
		except:
			fecha = "Error en el formato (fecha) html de la pagina"


		noticias[i] = mega()

		noticias[i].url = url
		noticias[i].cat = cat
		noticias[i].fecha = fecha
		noticias[i].titulo = titulo
		noticias[i].autor = autor

		#noticias[i].print_attr()
		noticias[i].print_ttl()

		i = i+1
	return noticias

