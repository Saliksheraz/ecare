from django.db import models


class pharmacy(models.Model):
    name = models.CharField(max_length=200, null=True)
    desc = models.TextField(null=True, blank=True)
    dateAdded = models.DateField(auto_now=True)
    longitude = models.CharField(max_length=30, null=True)
    lattitude = models.CharField(max_length=30, null=True)
    postalCode = models.IntegerField(null=True)
    city = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class products(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.CharField(max_length=50, null=True)
    image = models.FileField(null=True)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    def __str__(self):
        return str(self.name)
