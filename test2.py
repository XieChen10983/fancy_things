from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# 定义BlockingScheduler


if __name__ == "__main__":
    sched = BlockingScheduler()
    sched.add_job(job, 'interval', minutes=1)
    # sched.add_job(job, 'interval', seconds=5)
    sched.start()
