import telebot
import config
import requests
import time
from lxml import html


bot = telebot.TeleBot(config.TOKEN)
flag = 1
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, "Start") 
	status1 = int(-1)
	price = ""
	while(flag):
		ref_price = get_price()
		if(ref_price != price):
			bot.send_message(message.chat.id, ref_price)
			price = ref_price

		

@bot.message_handler(commands=['stop'])
def stop(msg):
    global flag
    flag = 0
    bot.send_message(msg.chat.id, "stopped")



def get_price(): 
	URL = 'https://jabko.ua/iphone/apple-iphone-13/apple-iphone-13-256gb--product-red'
	res = requests.get(URL)
	tree = html.fromstring(res.text)

	prices = tree.xpath("/html/body/section[1]/div/div/div[3]/div[2]/span[3]/span[1]/text()")
    
	for price in prices:
		return (price.strip())

#RUN
bot.polling(none_stop=True)