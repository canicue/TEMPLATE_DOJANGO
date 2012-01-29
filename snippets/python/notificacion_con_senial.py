from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from django.core.mail import send_mail

class Document(models.Model):
    pass

class Comment(models.Model):
    pass

def notify_admin(sender, instance, created, **kwargs):
    '''Notify the administrator that a new user has been added.'''
    if created:
        subject = 'New user created'
        message = 'User %s was added' % instance.username
        from_addr = 'no-reply@example.com'
        recipient_list = ('admin@example.com',)
        send_mail(subject, message, from_addr, recipient_list)

signals.post_save.connect(notify_admin, sender=User)
