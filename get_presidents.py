import requests

def get_presidents():
    url = 'https://api.duckduckgo.com/?q=presidents+of+the+united' \
          '+states&format=json'
    response = requests.get(url)
    president_list =[]
    for i in response.json()['RelatedTopics']:
        president_list.append(i["Text"])

    return president_list
