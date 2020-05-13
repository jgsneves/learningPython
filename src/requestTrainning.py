import requests

query = str(input('Digite o código da ação: '))
getUrl = 'https://www.google.com/search?q={query}'.format(query=query)
print(getUrl)


def stockSearch():
    request = requests.get(getUrl)
    siteOnText = request.text
    print(siteOnText)
