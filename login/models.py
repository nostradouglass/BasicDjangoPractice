from django.db import models

# Create your models here.

class TestModel(models.Model):
    color = models.CharField(max_length=128)
    amount = models.IntegerField(),
    text = models.TextField(default="null")

    published_date = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return self.color