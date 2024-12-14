from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name_plural = "Viloyatlar"
        
    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')


    class Meta:
        verbose_name_plural = "Tumanlar"


    def __str__(self):
        return f"{self.name} ({self.region.name})"

class Ish_kuni(models.Model):
    day = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Ish kunlari"


    def __str__(self) -> str:
        return self.day