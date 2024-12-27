from celery import shared_task

@shared_task
def send_report_email():
    # Simulate sending an email
    return "Report email sent."
