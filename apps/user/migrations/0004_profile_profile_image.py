# Generated by Django 2.2.6 on 2019-10-28 22:38

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('user', '0003_remove_profile_profile_image'),
	]
	
	operations = [
		migrations.AddField(
			model_name='profile',
			name='profile_image',
			field=models.ImageField(blank=True, default='default-avatar.png', null=True, upload_to='users/'),
		),
	]
