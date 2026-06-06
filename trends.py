from pytrends.request import TrendReq

pytrends = TrendReq()

keywords = ["AI"]

pytrends.build_payload(keywords)

trending = pytrends.related_queries()["AI"]["top"]

topics = trending["query"].head(5).tolist()

print(topics)