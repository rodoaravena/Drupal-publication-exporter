import feedparser
from bs4 import BeautifulSoup
import datetime
from dateutil.parser import *

def get_rss_list():
    list_rss_url = ['url1','url2','url3']
    # csv = 'Actividad;Categoria;Nombre publicacion;enlace;descripcion;anio;fecha\n'
    csv = ''
    print('Iterando sobre', len(list_rss_url), ' elementos')
    for rss_url in list_rss_url:
        print('===================================================')
        print('Conectando...')
        print('Información descargada')
        print('Leyendo información...')
        feed = feedparser.parse( rss_url )  
        print('Almacenando ', len(list(enumerate(feed['entries']))), ' publicaciones')
        for id_item, item in enumerate(feed['entries']):           
            texto = BeautifulSoup(item['summary_detail']['value'])
            fecha = parse(item['published'])
            anio = fecha.strftime('%Y')
            fecha = fecha.strftime('%d/%m/%Y')

            texto = str(texto.get_text()).replace('\n','').strip()
            csv_item = str(str(feed['feed']['title']))+';'+str(item['title']) +';' + str(item['links'][0]['href']) + ';'+texto+'.;'+str(anio)+';'+str(fecha)+'\n'
            csv += csv_item
        print('Almacenado')

    return csv

file_name = "Listado.csv"
event_file = open(file_name,'w')
event_file.write(get_rss_list())
print('Listo')
#get_rss_list()
