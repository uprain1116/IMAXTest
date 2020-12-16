import requests
import telegram
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime
myToken = '1499755282:AAEBKbdxR14J1aNQnAuYS49ZDzw_b8cMCf0'
bot = telegram.Bot(token=myToken)
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20201219'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
list = soup.select('.info-hall')
if 'IMAX' in str(list):
    bot.sendMessage(chat_id=981941034, text="예매오픈!")
else:
    if (now.hour == 12 and now.minute == 0):
        bot.sendMessage(chat_id=981941034, text="정상작동 중")




