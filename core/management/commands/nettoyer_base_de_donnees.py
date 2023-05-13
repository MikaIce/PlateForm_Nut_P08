from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Description de ma tâche Cron'

    def handle(self, *args, **options):
        # Code pour exécuter votre tâche ici
        print('Tâche exécutée avec succès')

        self.stdout.write(self.style.SUCCESS('Tâche exécutée avec succès'))

