import time
import os
import schedule
import pyninegag

""" Sends random meme from 9gag via iMessage"""

def send_message():
    def ninegag():
        url = 'http://9gag.com/hot'
        for i in pyninegag.get_articles(url, max_pages=15):
            return i['url']

    cmd = """osascript<<END

    tell application "Messages"

    send "MEME OF THE DAY is %s " to buddy " email or phone number " of (service 1 whose service type is iMessage) 

    end tell

    END""" % ninegag()
    os.system(cmd)

send_message()

schedule.every().day.at("23:00").do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)
