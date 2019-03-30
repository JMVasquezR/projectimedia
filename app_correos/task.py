from celery import shared_task
from django.core.mail import send_mail
from smtplib import SMTPException


@shared_task(bind=True)
def task_enviar_mail(self, subject, body, correo_de_salida, ls_correo_de_destino, html_message=None):
    try:
        send_mail(subject, body, correo_de_salida, ls_correo_de_destino, html_message=html_message, fail_silently=False)
    except SMTPException as exc:
        raise self.retry(exc=exc)
