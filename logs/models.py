from django.db import models

class Log(models.Model):
	entry = models.CharField(max_length=255)
	comments = models.TextField()
	device_name = models.CharField(max_length=200)
	classification = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.device_name + " " + self.classification

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
