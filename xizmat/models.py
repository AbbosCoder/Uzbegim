from django.db import models
import uuid
from malumotlar.models import Region,District,Ish_kuni
# Create your models here.


class Mehmonxona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nomi = models.CharField(max_length=255)
    ish_kunlari = models.ForeignKey(Ish_kuni, on_delete=models.CASCADE)
    ochilish_vaqti = models.TimeField()  # ish boshlanish vaqti
    yopilish_vaqti = models.TimeField()    # ish tugash vaqti
    telefon_raqam = models.CharField(max_length=15)
    viloyat = models.ForeignKey(Region,on_delete=models.CASCADE)
    tuman=models.ForeignKey(District,on_delete=models.CASCADE)
    joylashuv = models.CharField(max_length=400)
    
    def __str__(self) -> str:
        return f'{self.nomi} | {self.tuman}'
    

class Oshxona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nomi = models.CharField(max_length=255)
    ish_kunlari = models.ForeignKey(Ish_kuni, on_delete=models.CASCADE)
    ochilish_vaqti = models.TimeField()  # ish boshlanish vaqti
    yopilish_vaqti = models.TimeField()    # ish tugash vaqti
    telefon_raqam = models.CharField(max_length=15)
    viloyat = models.ForeignKey(Region,on_delete=models.CASCADE)
    tuman=models.ForeignKey(District,on_delete=models.CASCADE)
    joylashuv = models.CharField(max_length=400)

    def __str__(self) -> str:
        return f'{self.nomi} | {self.tuman}'


class Ustaxona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nomi = models.CharField(max_length=255)
    ish_kunlari = models.ForeignKey(Ish_kuni, on_delete=models.CASCADE)
    ochilish_vaqti = models.TimeField()  # ish boshlanish vaqti
    yopilish_vaqti = models.TimeField()    # ish tugash vaqti
    telefon_raqam = models.CharField(max_length=15)
    viloyat = models.ForeignKey(Region,on_delete=models.CASCADE)
    tuman=models.ForeignKey(District,on_delete=models.CASCADE)
    joylashuv = models.CharField(max_length=400)
    
    def __str__(self) -> str:
        return f'{self.nomi} | {self.tuman}'
    

class Shifoxona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nomi = models.CharField(max_length=255)
    ish_kunlari = models.ForeignKey(Ish_kuni, on_delete=models.CASCADE)
    ochilish_vaqti = models.TimeField()  # ish boshlanish vaqti
    yopilish_vaqti = models.TimeField()    # ish tugash vaqti
    telefon_raqam = models.CharField(max_length=15)
    viloyat = models.ForeignKey(Region,on_delete=models.CASCADE)
    tuman=models.ForeignKey(District,on_delete=models.CASCADE)
    joylashuv = models.CharField(max_length=400)

    def __str__(self) -> str:
        return f'{self.nomi} | {self.tuman}'