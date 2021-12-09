from urllib.request import urlopen
import xml.etree.ElementTree as ET
import xmltodict, json

def writeNewsTitleDateToJSON(text):
    parser = ET.XMLPullParser(['start', 'end'])
    parser.feed(text)

    items_list = []
    flag = False
    dict = {}
    for event, elem in parser.read_events():
        if elem.tag == 'item' and event == 'start':
            flag = True
        if flag and event == 'start' and (elem.tag == 'pubDate' or elem.tag == 'title'):
            dict[elem.tag] = elem.text
        if elem.tag == 'item' and event == 'end':
            flag = False
            items_list.append({"pubDate" : dict['pubDate'], "title" : dict['title']})
            dict = {}

    with open('news.json', 'w', encoding='utf8') as json_file:
        json.dump(items_list, json_file, ensure_ascii=False)


def write_all_news_info_to_JSON(text):
    parser = ET.XMLPullParser(['start', 'end'])
    parser.feed(text)

    items_list = []
    flag = False
    dict = {}
    for event, elem in parser.read_events():
        if elem.tag == 'item' and event == 'start':
            flag = True
        if flag and event == 'start':
            dict[elem.tag] = elem.text
        if elem.tag == 'item' and event == 'end':
            flag = False
            items_list.append(dict)
            dict = {}

    with open('news_all_info.json', 'w', encoding='utf8') as json_file:
        json.dump(items_list, json_file, ensure_ascii=False)


text = urlopen('https://lenta.ru/rss').read().decode('utf8')
writeNewsTitleDateToJSON(text)
write_all_news_info_to_JSON(text)




