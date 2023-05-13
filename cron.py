from django_cron import CronJobBase, Schedule
from core.management.commands.update_open_food_facts import Command

class UpdateOpenFoodFactsCronJob(CronJobBase):
    RUN_EVERY_WEEK = Schedule(run_every_mins=10080)  # Exécute toutes les semaines (1 semaine = 10080 minutes)
    schedule = RUN_EVERY_WEEK
    code = 'core.update_open_food_facts_cron_job'

    def do(self):
        command = Command()
        command.handle()

