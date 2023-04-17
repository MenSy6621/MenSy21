from django.db import models



class People(models.Model):
    name = models.CharField(max_length=255)
    year_of_brith = models.DateTimeField()
    Year_of_death = models.DateTimeField(blank=True)
    type_of_activity= models.TextField()
    Reason_for_popularity = models.TextField()
    photo = models.ImageField()
