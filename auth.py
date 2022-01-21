from TwitterAPI import TwitterAPI
from twitter import *

import sys
sys.path.append(".")

def trends():
  twitter = Twitter(auth = OAuth(
                    "234111197-vZ84703EP2Byaub75qBUAY0e7TDJpllVMcgZYQmQ",
                    "ehzPmLU9fJF8pkVF51YIqOuGC80HR2D9RQVnuQUOFw",
                    "p0mYBrK2pGstQ9lwtMPrg",
                    "24Yjp5OAbTY00uNqrmOTSaLV1sroNRUv1Sk33ngf9k"
                    ))


  results = twitter.trends.place(_id = 349859)

  print("Chile Trends")

  for location in results:
      for trend in location["trends"]:
          print(" - %s" % trend["name"])
          trends[trend] = trend["name"]


  print("Otro resultado")
  """ api = TwitterAPI(
                    "p0mYBrK2pGstQ9lwtMPrgx",
                    "24Yjp5OAbTY00uNqrmOTSaLV1sroNRUv1Sk33ngf9k",
                    "234111197-vZ84703EP2Byaub75qBUAY0e7TDJpllVMcgZYQmQx",
                    "ehzPmLU9fJF8pkVF51YIqOuGC80HR2D9RQVnuQUOFw"
                  )

        
  r = api.request('trends/place', {'id':'349859'})
  for item in r:
          print(item["name"]) """
  return trends

trends()