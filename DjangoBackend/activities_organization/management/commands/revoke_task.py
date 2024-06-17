from django.core.management.base import BaseCommand
from DjangoBackend.celery import app


class Command(BaseCommand):
    help = 'Revoke a Celery task by task_id'

    def add_arguments(self, parser):
        parser.add_argument('task_id', type=str, help='The ID of the task to revoke')

    def handle(self, *args, **kwargs):
        task_id = kwargs['task_id']
        app.control.revoke(task_id, terminate=True)
        self.stdout.write(self.style.SUCCESS(f'Successfully revoked task {task_id}'))