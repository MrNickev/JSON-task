import urllib.parse
from urllib.request import urlopen
import json
import itertools as it

url = 'Бельмондо,_Жан-Поль'

url = urllib.parse.quote(url)
print(url)

def get_max_revisions_date(title):
    url='https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=' + title
    data = json.loads(urlopen(url).read().decode('utf8'))
    dict = {}
    # print(data['query']['pages'])
    for key, group in it.groupby(data['query']['pages']['192203']['revisions'], key=lambda x: x['timestamp'].split('T')[0]):
        dict[key] = sum(1 for x in group)
    #                                                                 градский: 183903
    for key in dict:
        print(key, dict[key])

    max_value_key = max(dict, key=lambda key: dict[key])
    print("Наибольшее число правок: ", max_value_key, dict[max_value_key])

get_max_revisions_date(url)