from django.db import models



class TimeStampedModel(models.Model):

	created = models.DateTimeField(
			'criado em',
			auto_now_add=True,
			auto_now=False,
			blank=True
		)
	modified = models.DateTimeField(
			'modificado em',
			auto_now_add=False,
			auto_now=False,
			blank=True
		)

	class Meta:

		abstract = True