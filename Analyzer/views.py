from django.shortcuts import render
from Analyzer.forms import keywordForm, locationForm
from Analyzer.database_handler import DatabaseHandler
from Analyzer.woeid import WOEID
from Analyzer.twitter_search import Twitter_Search
from . import Sent_Analyzer
from Analyzer.response import Response
import time, json, operator

def index(request):
    return render(request, 'Analyzer/index.html')

def sentiment_scores(request):

    #Start time
    start_time = time.time()

    #Get input
    if request.method == 'POST':
        form = keywordForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
    else:
        form = keywordForm()

    #Connect to DynamoDB and get data in database
    db_handler = DatabaseHandler()
    data = db_handler.getItem(keyword)

    result_list = []
    for d in data:
        result_list.append(d['text'])

    keyword_hits = len(result_list)

    analyzer = Sent_Analyzer.Analyzer()
    scores, length = analyzer.retrieveSentScores(result_list)
    scoresList = []
    scoresList.append(scores['pos'])
    scoresList.append(scores['neg'])
    scoresList[0] = scoresList[0] * 100
    scoresList[1] = scoresList[1] * 100

    labels = ['Positive', 'Negative']

    #Done time
    elapsed_time = time.time() - start_time

    return render(request, 'Analyzer/sentiment_scores.html', {"elapsed_time": elapsed_time,
                                                              "data": result_list,
                                                              "keyword_hits": keyword_hits,
                                                              "keyword": keyword,"labels": labels, "scores": scoresList})
    '''
    return render(request, 'Analyzer/sentiment_scores.html',
                  {"labels": labels, "scores": scoresList, 'data': result_list, "keyword_hits": keyword_hits,
                   "elapsed_time": elapsed_time,
                   "keyword": keyword})
    '''


def show_database(request):
    start_time = time.time()
    db_handler = DatabaseHandler()
    db_length = db_handler.getAllItem()

    elapsed_time = time.time() - start_time

    return render(request, 'Analyzer/show_database.html', {"db_length": db_length, "elapse_time": elapsed_time})

def trending(request):
    with open("woeid.json") as file_obj:
        data = json.load(file_obj)
    woeid_list = []
    for item in data:
        i = WOEID(item['name'], item['country'], item['woeid'], )
        woeid_list.append(i)
    sorted_woeid_list = sorted(woeid_list, key=operator.attrgetter('name'))
    return render(request, 'Analyzer/trending.html', {"sorted_woeid_list": sorted_woeid_list})

def show_trending(request):
    if request.method == 'POST':
        form = locationForm(request.POST)
        if form.is_valid():
            geographical_code = form.cleaned_data['location']
    else:
        form = locationForm()

    with open("woeid.json") as file_obj:
        data = json.load(file_obj)
    woeid_dic = {}
    for item in data:
        woeid_dic[item['woeid']] = item['name'] + ", " + item['country']
    key = geographical_code
    woeid_location = woeid_dic[int(key)]

    trend_search = Twitter_Search()
    trend_search.change_woe_id(key)
    res = trend_search.trending_search()
    keywords = []
    counts_data = []
    print(len(res))
    for r in res:
        keywords.append(r.text)
        counts_data.append(r.vote)



    return render(request, 'Analyzer/show_trending.html', {"keywords":keywords, "counts_data":counts_data, "woeid_location":woeid_location})