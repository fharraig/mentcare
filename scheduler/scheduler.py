from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
import sys
from mentcare_api import models


def check():
    print("Checking for overdue appointments...")
    items = models.Patient.objects.all()
    for obj in items:
        if obj.DateOfLastVisit:
            dt = timezone.now - obj.DateOfLastVisit
            if dt.days > 30:
                obj.AppointmentOverdue = 1
            else:
                obj.AppointmentOverdue = 0


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # run this job every 24 hours
    scheduler.add_job(check, 'interval', hours=24, name='check_overdue_appointments', jobstore='default')
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
