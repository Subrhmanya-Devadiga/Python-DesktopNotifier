from bs4 import BeautifulSoup
import notify2
import requests

# get news from timenownews
icon_path = '/home/subbu/Documents/GitHub/Desktop-Notifier/news_icon.png'
html_file = requests.get('https://www.timesnownews.com/').text
soup = BeautifulSoup(html_file,'lxml')
s1 = soup.find('div', class_='section-one')
s1_h_text = s1.find('h2',class_='content').text
link = s1.a['href']
headline_text = (f"\t{s1_h_text}")
headline_link = (f"\t https://www.timesnownews.com{str(link)}")
headlines = s1.find_all('div',class_='component_1')
for headline in headlines:
    news = headline.find('h3',class_='text').text
    news_link = headline.a['href']
    news_text = (f"\t {news.strip()} \n")
    links = (f"\t https://www.timesnownews.com{news_link.strip()}")
# notifying the news
    notify2.init("news")
    notification = notify2.Notification(news_text,links,icon= icon_path)
    notification.show()
# notifying headline which is outside the for loop
notify2.init("news")
headlines = notify2.Notification(headline_text,headline_link,icon= icon_path)
headlines.show()