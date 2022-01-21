#import noticia_obj
class noticia_obj:
        #url = ''
        #cat = ''
        #fecha = ''
        #titulo = ''
        #colab = ''

    def __init__(self, url='', cat='', fecha='', titulo='', colab=''):
        self.url = url
        self.cat = cat
        self.fecha = fecha
        self.titulo = titulo
        self.colab = colab
            
    def print_attr(self):
        print('url: ' + self.url)
        print('\n')
        print('category: ' + self.cat)
        print('\n')
        print('fecha: ' + self.fecha)
        print('\n')
        print('titulo: ' + self.titulo)
        print('\n')
        print('colaborators: ' + self.colab)
        print('\n')

    def print_ttl(self):
        print('titulo: ' + self.titulo)
        print('\n')