import send_sms_reminder
from apscheduler.schedulers.blocking import BlockingScheduler

#database_url = "mysql://root:root@localhost/gym_management"
database_url = "mysql://porovvasu:vasu1234@porovvasu.mysql.pythonanywhere-services.com/porovvasu$gym_management"

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(module)s [%(process)d %(thread)d] | [%(filename)s:%(lineno)s - %(funcName)s() ] | \n%(message)s')
##logger = logging.get#logger(__name__)

send_sms_reminder_id = "send_sms_reminder"


def send_sms_reminders():
    send_sms_reminder.main()


def remove_jobs(scheduler):
    ##logger.debug("Removing existing jobs")

    if scheduler.get_job(send_sms_reminder_id):
        #logger.debug("Job available: " + str(send_sms_reminder_id))
        scheduler.remove_job(send_sms_reminder_id)
        #logger.debug("Job removed: " + str(send_sms_reminder_id))

    #logger.debug("All jobs removed")
    #logger.debug(str(scheduler.print_jobs()))


def add_jobs(scheduler):
    if not scheduler.get_job(send_sms_reminder_id):
        added_job = scheduler.add_job(send_sms_reminders, 'cron', hour='16', minute='22',
                                      id=send_sms_reminder_id)
        print("Added job" + added_job.id)

    scheduler.print_jobs()


def main():
    ##logger.info("send_sms_reminder")
    print ("send_sms_reminder")
    # logging.basicConfig()

    scheduler = BlockingScheduler()
    scheduler.add_jobstore("sqlalchemy", url=database_url)

    # Uncomment if we want to remove the jobs
    # remove_jobs(scheduler)
    # return

    add_jobs(scheduler)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    main()
