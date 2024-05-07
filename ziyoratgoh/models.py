from django.db import models
import uuid
from django.core.exceptions import ValidationError
from malumotlar.models import Region,District
from xizmat.models import Mehmonxona,Oshxona,Shifoxona,Ustaxona
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import crop_to_16_9
# Create your models here.

class Ziyoratgoh(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    rasm_first = models.ImageField(upload_to='rasmlar/')
    rasm_second = models.ImageField(upload_to='rasmlar/')
    about = models.TextField(blank=True)
    viloyat = models.ForeignKey(Region,on_delete=models.CASCADE)
    tuman=models.ForeignKey(District,on_delete=models.CASCADE)
    mehmonxona = models.ForeignKey(Mehmonxona,on_delete=models.CASCADE,blank=True)
    oshxona = models.ForeignKey(Oshxona,on_delete=models.CASCADE,blank=True)
    ustaxona = models.ForeignKey(Ustaxona,on_delete=models.CASCADE,blank=True)
    shifoxona = models.ForeignKey(Shifoxona,on_delete=models.CASCADE,blank=True)

    def __str__(self) -> str:
        return self.title



class Carusel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ziyoratgoh = models.ForeignKey(Ziyoratgoh,on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        # Check the count of Carusel instances referencing this Ziyoratgoh
        if Carusel.objects.count() >= 5:
            raise ValidationError("Karuselga 5 tadan kop Ziyoratgoh qo'shib bo'lmaydi,Agar qo'shmoqchi bo'lsangiz qaysidir Ziyoratgohni o'chiring!")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.ziyoratgoh.title

# Rasm yuklanganda qirqishni amalga oshirish
@receiver(post_save, sender=Ziyoratgoh)
def crop_image_on_save1(sender, instance, created, **kwargs):
    if created and instance.rasm_first:
        # Rasmni 16:9 nisbatda qirqish
        crop_to_16_9(instance.rasm_first.path)

@receiver(post_save, sender=Ziyoratgoh)
def crop_image_on_save2(sender, instance, created, **kwargs):
    if created and instance.rasm_second:
        # Rasmni 16:9 nisbatda qirqish
        crop_to_16_9(instance.rasm_second.path)
