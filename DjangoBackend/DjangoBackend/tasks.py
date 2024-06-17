from activities_organization.models import Notice
from .celery import app

@app.task
def modify_notice_condition(notice_id):
    print("execute")
    notice = Notice.objects.get(id=notice_id)
    notice.condition = True
    notice.save()