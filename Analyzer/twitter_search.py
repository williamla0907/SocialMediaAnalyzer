import twitter
from Analyzer import response

#Authentication Keys
CONSUMER_KEY = '6bGvPIczIz1roXCrwfBQppAYs'
CONSUMER_SECRET = 'SGszHBt2KpmPRyGQmuEZ6mqLu0XXMmTGMnbuuCPUEgal8gsWjR'
OAUTH_TOKEN = '805894637290295296-eRnGmrIR0fT3gY5HNlOwPVHf04oeKqy'
OAUTH_TOKEN_SECRET = 'bVJgtvA8TG9JzaFoSbP4sy4aFsQwoeGFZIajmXzs7ROsT'

class Twitter_Search():

    def __init__(self):
        #Innitialize WHERE ON EARTH ID, 1 means search will be done on worldwide scale
        self.WOE_ID = 1
        self.auth = twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
        self.twitter_api = twitter.Twitter(auth=self.auth)

    # Change geo location
    def change_woe_id(self, NEW_WOE):
        self.WOE_ID = NEW_WOE

    # Top 10 keyword from Twitter based on geo location
    def trending_search(self):
        world_trends = self.twitter_api.trends.place(_id=self.WOE_ID)
        full_trending = world_trends[0]["trends"]
        shorted_trending = {}
        for i in range(0, len(full_trending)):
            if full_trending[i]["tweet_volume"] != None:
                shorted_trending[full_trending[i]["tweet_volume"]] = full_trending[i]["name"]

        temp_results = []

        for key in shorted_trending.keys():
            temp_results.append(key)

        temp_results.sort(reverse=True)
        keywords = []

        for j in range(len(temp_results)):
            keywords.append(shorted_trending[temp_results[j]])

        result = []
        for j in range(len(temp_results)):
            result.append(response.Response())
            result[j].changeText(keywords[j])
            result[j].changeVote(temp_results[j])

        return result