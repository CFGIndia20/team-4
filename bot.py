#Author : KUMARASUBRAHMANYA H
import telepot
import csv    
import json 
import requests
import time
import csv
import time
import telegram,telebot
#from mainExcalibur import *
from datetime import datetime

#Token
token=#token_value
URL = "https://api.telegram.org/bot{}/".format(token)

TelegramBot=telepot.Bot(token)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js
    
def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


  

def send_message(text, chat_id,user):
    if text=="/start":
    	text="Enter Name, Location of incident, Description separated by \\n"
    	url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    	get_url(url)
    else:
    	text1=str(text)
    	myCsvRow=text1.split('\n')    	
        now = time.time()
#        timestamp = now.strftime("%H:%M:%S")
    	print(now)
    	source='TL'
    	paragraph=text1
    	'''with open('janagrah.csv', mode='a') as employee_file:
    		employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    		employee_writer.writerow(myCsvRow)'''
    	#print(message.from_user['username'])
    	
    	#Remove to call without error
    	#dictt=mainExcalibur(paragraph,now,source,None,user)
    	
    	
    	#obj='{"timestamp":timestamp,"source":source,"paragraph":paragraph}'	
    	#obj1=json.loads(obj)
    	
    	
    	text="Your response has been recorded."# with tracking id . You can visit{} for more"#.format(dictt["id"],dictt["url"])
    	url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    	get_url(url)
    
def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            #print(update["message"])
            user=str(update["message"]["from"]["username"])
            send_message(text, chat,user)
        except Exception as e:
            print(e)
                

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
