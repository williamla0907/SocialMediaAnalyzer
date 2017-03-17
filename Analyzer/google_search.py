from xml.etree import ElementTree as ET
import urllib.request




def gogTopTrends():
    # get xml
    with urllib.request.urlopen("https://trends.google.com/trends/hottrends/atom/feed?pn=p1") as url:
        f = url.read()

    root = ET.fromstring(f)
    channel = root[0]

    # make a list of data
    titles = []
    searchCounts = []

    # parse the xml
    for item in channel.findall('item'):
        titles.append(item.find('title').text)
        searchCounts.append(int(item[1].text.replace('+', '').replace(',', '')))

    dictionary = dict(zip(titles, searchCounts))

    return dictionary