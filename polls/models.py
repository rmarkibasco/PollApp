from django.db import models
import datetime
from django.utils import timezone

class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	#second part (page 1)
	#Edit the name of a created object
	def __unicode__(self):
		return self.question

	#third part (page 1)
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	#second part (page 1)
	#Edit the name of a created object
	def __unicode__(self):
		return self.choice_text