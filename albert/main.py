# libraries
import numpy as np # matrix calculations

# news-class object
from news_obj import *

# twitter-trending-topics function
from trend import *

# cnn-economics-news function
from news import *

# without-whitespaces function 'on the fly'
from wspaces import *


if __name__ == "__main__":
    # save news from http request from news function
    news_list = iter(news())
    
    # call the trending topics from twitter & save them in a list
    trends = trend()

    """
    # invoke a method to print every attribute of each news
    news_listp = news()
    for i in range(len(news_listp)):
        news_listp[i].print_attr()

    # print every trendig topic
    for j in range(len(trends)):
        print(trends[j])
    """
    
    # counter for a match between a news and a trending topic
    match = 0

    # compare trends with news
    try:
        while True:
            # one iteration for every news
            news = next(news_list)

            for i in range(len(trends)):
                #print(trends[i])

                # fast comparisons: if words from trendings match words from news title
                mask = np.isin(
                    [words for words in wspaces(news.title.strip('\n'))], # remove all '\n'
                    [words for words in wspaces(trends[i])]
                    )
                
                # if mask[i] is true, then there is a match
                for j in range(len(mask)):
                    if(mask[j] == True):
                        match += 1
                        
                        print(news.title)
                        print(trends[i])

    except StopIteration:
        #print('\n no more news \n')
        pass

    # question 1
    print('\n %s trends are allready news from the economic section of CNN \n' % match)

    # question 2
    print('\n %s news from the economic section of CNN are not trending topics on twitter \n' % (12 - match))

    # question 3
    print('\n %s percent of trends are news \n' % ((match/12)*100))
    
    pass