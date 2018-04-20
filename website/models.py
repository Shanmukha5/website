from django.db import models
from django.contrib.auth.models import User

class UsersForm(models.Model):
	name=models.CharField(max_length=50)
	email = models.EmailField(blank=False,null=True)
	mobile = models.CharField(max_length=12,null=True,blank=False)
	message = models.CharField(max_length=5000,null=True,blank=False)




	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name
	class Meta:
		managed = True
		db_table = 'website_feedback_database'