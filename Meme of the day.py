import time
import os
import schedule
import pyninegag
""" Sends random meme from 9gag via iMessage"""


"""send_message()

schedule.every().day.at("23:00").do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)"""


def ninegag():
    url = 'http://9gag.com/hot'
    for i in pyninegag.get_articles(url,max_pages=3):
        return i


ninegag()