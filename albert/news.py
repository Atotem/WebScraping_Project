import urllib.request # library to make http request
from bs4 import BeautifulSoup as bs # library to parse html file

# news-class object
from news_obj import *

def news():
    # open & parse html file
    html = urllib.request.urlopen('https://www.cnnchile.com/economia/').read()
    html = bs(html, 'html.parser')

    # html list with headers for each title for each div-sub-container
    html_list = html.body.find('div', attrs={'class':'inner-list'})

    # create an empty list for a list of objects
    news_list = [0 for i in range(12)]

    # create a news object and for each add the title from each news
    i = 0
    for html_item in html_list:
        try:
            title = html_item.find('h2', attrs={'class':'inner-item__title'}).text # get title of the news
            news_list[i] = news_obj() # create an news object
            news_list[i].title = title # add to title attribute the title of the news

            i += 1
        except:
            pass

    return(news_list)