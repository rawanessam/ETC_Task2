import bs4
import requests_html
import json
data={}
data['Titles']=[]
data['Links']=[]
for i in range(10):

    if i ==0:
        url= 'https://news.un.org/en/news/region/middle-east'
    else:
        url = 'https://news.un.org/en/news/region/middle-east'+'?page='+str(i)
    session = requests_html.HTMLSession()
    Page = session.get(url)
    Page_Html = bs4.BeautifulSoup(Page.text, 'html.parser')
    body = Page_Html.find_all(id='block-system-main')[0]
    articles = body.find_all('h1')
    for article in articles:

        links = article.find_all('a', recursive=False, href=True)[0]
        data['Titles'].append(article.text.strip())
        data['Links'].append('https://news.un.org/'+links['href'])
json_object = json.dumps(data, indent=4)
print(json_object)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
with open('results.json', 'w') as outfile:
    json.dump(data, outfile)