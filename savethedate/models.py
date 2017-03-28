from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.auth.models import AbstractUser



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	full_day = models.BooleanField(default=True)
	family = models.TextField(max_length=100, blank=True)
	conferma_pranzo = models.BooleanField(default=False)
	conferma_sera = models.BooleanField(default=False)
	conferma_inviata = models.BooleanField(default=False)
	
	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name


	
#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()