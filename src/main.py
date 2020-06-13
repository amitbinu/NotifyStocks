import schedule
import time
from notify import notify

def job():
    notify()

schedule.every().day.at("10:17").do(job)
schedule.every().day.at("11:00").do(job)
schedule.every().day.at("11:30").do(job)
schedule.every().day.at("12:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
