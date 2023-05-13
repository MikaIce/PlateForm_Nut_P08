from crontab import CronTab

if __name__ == '__main__':
    cron = CronTab(user=True)
    job = cron.new(command='python3 /home/mbenoit/platform/manage.py nettoyer_base_de_donnees')
    job.minute.on(0)
    job.hour.on(0)
    job.enable()
    cron.write()

    cron.write_to_user(user=True)

