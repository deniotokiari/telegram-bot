# -*- coding: utf-8 -*-

from sys import argv

from bot import Bot


def handle_response(response):
    print(response)


token = argv[1]  # get token from cli
bot = Bot(token, handle_response)


def stop():
    print("Stopping bot")
    bot.stop()


while True:
    text = input(">>")

    if "start" in text:
        print("Starting bot with token: %s" % token)
        bot.start()
    elif "stop" in text:
        stop()
    elif "exit" in text:
        stop()
        break
