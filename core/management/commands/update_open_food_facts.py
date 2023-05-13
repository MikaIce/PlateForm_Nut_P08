from django.core.management.base import BaseCommand
from core.models import Product

class Command(BaseCommand):
    help = 'Met à jour les éléments récupérés d\'Open Food Facts'

    def handle(self, *args, **options):
        # Code pour mettre à jour les éléments
        # Exemple :
        Product.objects.update_from_open_food_facts()

