from nltk.sentiment.vader import SentimentIntensityAnalyzer

import nltk
nltk.data.path.append('./nltk_data/')

class Analyzer:
    tweets = []
    length=0

    def __init__(self):
        length = 0

    def retrieveSentScores(self,data):
        # initialize Sentiment analyzer

        sid = SentimentIntensityAnalyzer()
        scores = {"pos": 0, "neg": 0}
        percentScores = {"pos": 0.0, "neg": 0.0}
        # represents score for positive,negative,neutral
        finalCompoundScore = 0

        length = len(data)
        for line in data:
            sentimentScores = sid.polarity_scores(line)
            # Compound is the sum of both pos & neg scores
            compoundScore = sentimentScores['compound']
            neuScore = sentimentScores['neu']
            posScore = sentimentScores['pos']
            negScore = sentimentScores['neg']
            if (posScore>negScore):
                scores['pos'] += 1
            else:
                scores['neg'] += 1


            finalCompoundScore = finalCompoundScore + compoundScore

            roundedFinalScore = round(finalCompoundScore / len(data), 4)

        percentScores['pos'] = float(scores['pos']) / length
        percentScores['neg'] = float(scores['neg']) / length
        return percentScores, length
