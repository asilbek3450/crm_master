from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

phone_regex = RegexValidator(
	regex=r'^998[0-9]{9}$',
	message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	phone_number = models.CharField(max_length=12, validators=[phone_regex], blank=True, null=True, default=None)
	birth_date = models.DateField(null=True, blank=True)
	profile_image = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)
	
	def __str__(self):
		return '%s %s' % (self.user.first_name, self.user.last_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
