from django.db import models

# Create your models here.
from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=100)
    temperature_type = models.CharField(
        max_length=10,
        choices=[
            ('hot', 'Hot'),
            ('warm', 'Warm'),
            ('cold', 'Cold')
        ]
    )
    weather_tags = models.TextField(help_text="مثلاً: گرم، سرد، مرطوب")

    def __str__(self):
        return self.name
