from django.db import models


class Restaurant(models.Model):
    name = models.TextField(max_length=200)
    desc = models.TextField(max_length=500)
    avg_rating = models.FloatField()
    addr = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name

class Rating(models.Model):
    rate = models.FloatField()
    res_id = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.rate