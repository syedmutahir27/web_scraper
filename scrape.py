import requests
from bs4 import BeautifulSoup
import pprint
import re

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')
link1 = soup.select('.titleline')
link2 = soup2.select('.titleline')
subline = soup.select('.subtext')
subline2 = soup2.select('.subtext')

mega_link = link1 + link2
mega_subtext = subline + subline2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist,key = lambda k:k['votes'],reverse = True)

def create_custom_hm(links,subline):
    hn = []
    for idx , item in enumerate(links):
        title = item.getText()
        href = item.find('a', attrs={'href': re.compile("^https://")})
        vote = subline[idx].select('.score')
        if len(vote) :
            points = int(vote[0].getText().replace(' points',''))
            if points >99:
                hn.append({'title': title ,'link':href,'votes':points})
    return sort_stories_by_votes(hn)


pprint.pprint( create_custom_hm(mega_link, mega_subtext))


#solve the dictionay link problem