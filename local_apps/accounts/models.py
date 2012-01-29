from django.contrib.auth.models import User
from django.db import models
# Create your models here.




class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='profile')
    company = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    #pais = models.ForeignKey(Pais)

    def __unicode__(self):
        try:
            return  self.user.username
        except:
            return "perfil sin usuario!!!"


def agregar_perfil(user,*args,**kwargs):
    try:
        profile=Profile.objects.get(user=user)
        profile.save(force_update=True)
    except:
        profile=Profile(user=user,*args,**kwargs)
        profile.save()
