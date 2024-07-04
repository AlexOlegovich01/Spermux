# https://t.me/spermuxbot
import telebot
import random
TOKEN=
bot=telebot.TeleBot(TOKEN)

score=0

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id,'Бот запущен!!!')

@bot.message_handler(commands=['play'])
def start(message):
    global score
    lst=["🍎","🍒","🍉"]
    bank=[]
    for i in range(4):
        bank.append(random.choice(lst))
    if len(set(bank))==1:
        score+=1000
        bot.send_message(message.chat.id, ' '.join(bank))
        bot.send_message(message.chat.id,"Всего очков - "+str(score))
    elif len(set(bank))==2:
        score+=100
        bot.send_message(message.chat.id, ' '.join(bank))
        bot.send_message(message.chat.id,"Всего очков - "+str(score))
    elif len(set(bank))==3:
        score+=10
        bot.send_message(message.chat.id, ' '.join(bank))
        bot.send_message(message.chat.id,"Всего очков - "+str(score))
    elif len(set(bank))==3:
        score-=100
        bot.send_message(message.chat.id, ' '.join(bank))
        bot.send_message(message.chat.id,"Всего очков - "+str(score))
bot.polling()

