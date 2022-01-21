from twitter import * # library to connect to twitter api
import re # library to modify regular expressions

def trend():
    # authentication key for twitter api
    twitter = Twitter(auth = OAuth(
                    "234111197-vZ84703EP2Byaub75qBUAY0e7TDJpllVMcgZYQmQ",
                    "ehzPmLU9fJF8pkVF51YIqOuGC80HR2D9RQVnuQUOFw",
                    "p0mYBrK2pGstQ9lwtMPrg",
                    "24Yjp5OAbTY00uNqrmOTSaLV1sroNRUv1Sk33ngf9k"))
    
    # call api request
    results = twitter.trends.place(_id = 349859)

    # create trending topic list
    trends = [0 for i in range(50)]

    i = 0
    for location in results:
        for trend in location["trends"]:
            trends[i] = trend["name"]
            i += 1

    # filter 'extra' expressions from trending phrases
    for j in range(len(trends)):
        if (trends[j][0] == '#'):
            trends[j] = trends[j][1:]

        # apply regex to get accurate comparisons (ej: separate words)
        trends[j] = re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z])|[a-z](?=[0-9])|[A-Z](?=[0-9]))', r'\1 ', trends[j])

    return(trends)