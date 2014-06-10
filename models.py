from django.db import models

class Dataset(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    key_field = models.CharField(max_length=75)

##combined admin and dataset key should be unique
class DatasetOptions(models.Model):
	dataset = models.ForeignKey(Dataset)
#	admin = some admin id
	min_votes = models.IntegerField(default=1)
	allow_tagging = models.BooleanField(default=False)
	allow_new_tag = models.BooleanField(default=False)

class Tag(models.Model):
	dataset = models.ForeignKey(DatasetOptions)
	tag = models.CharField(max_length=200)
	approved = models.BooleanField(default=False)

class TaggedPoint(models.Model):
	tag = models.ForeignKey(Tag)
	kay_value = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

class Tagger(models.Model):
	tagged_point = models.ForeignKey(TaggedPoint)
#	user = 