from apscheduler.schedulers.blocking import BlockingScheduler
from twiliooo import checktimes
sched = BlockingScheduler()
# Schedule job_function to be called every half hours
sched.add_job(checktimes, 'interval', seconds=1800)
sched.start()