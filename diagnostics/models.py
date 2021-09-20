from django.db import models


class Lab(models.Model):
    name = models.CharField(max_length=100, null=True)
    desc = models.TextField(null=True, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    rating = models.IntegerField()
    postalCode = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Test(models.Model):
    name = models.CharField(max_length=100, null=True)
    desc = models.TextField(null=True, blank=True)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
