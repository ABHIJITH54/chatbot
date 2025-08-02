from django.core.management.base import BaseCommand
from chat.services import build_knowledge_base

class Command(BaseCommand):
    help = 'Build knowledge base from DOCX'

    def add_arguments(self, parser):
        parser.add_argument('docx_path', type=str)

    def handle(self, *args, **options):
        path = options['docx_path']
        build_knowledge_base(path)
        self.stdout.write(self.style.SUCCESS('Knowledge base indexed.'))
