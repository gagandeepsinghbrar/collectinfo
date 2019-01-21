from django.db import models


class Person(models.Model):
	name=models.charField(max_length=40)
	email= models.EmailField()

