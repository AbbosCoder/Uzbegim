from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return f"{self.name} ({self.region.name})"

class Ish_kuni(models.Model):
    day = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.day