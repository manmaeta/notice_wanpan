from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from linebot import LineBotApi
from linebot.models import TextSendMessage
import requests
import json


def detect_update():
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome('chromedriver',options=options)
  driver.implicitly_wait(10)
  driver.get("https://tonarinoyj.jp/episode/13932016480028985383")
  html = driver.page_source.encode('utf-8')
  soup = str(BeautifulSoup(html, "html.parser"))

  with open('title.txt', encoding='utf-8') as f:
    keyword = f.read()

  if (soup.find(keyword) < 0 ):
    keylist = list(keyword)
    newkey_num = int(''.join(keylist[1:len(keylist)]))
    newkey_num+=1
    newkey = '='+ str(newkey_num)
    with open('title.txt','w') as f:
      f.write(newkey)
    notice()


def notice():
  file = open('info.json','r')
  info = json.load(file)

  CHANNEL_ACCESS_TOKEN =info['CHANNEL_ACCESS_TOKEN']
  USER_ID = info['USER_ID']
  line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

  messages = TextSendMessage(text="最新話が更新されました。\n https://tonarinoyj.jp/episode/13932016480028985383")
  line_bot_api.push_message(USER_ID,messages=messages)

def main():
  detect_update()

if __name__=="__main__":
  main()
  
