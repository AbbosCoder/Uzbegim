from django.contrib import admin
from .models import Region, District,Ish_kuni

# Region uchun admin paneli
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)  # admin panelida ko'rsatish
    search_fields = ('name',)  # qidiruv uchun maydon

@admin.register(Ish_kuni)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('day',)  # admin panelida ko'rsatish
    search_fields = ('day',)  # qidiruv uchun maydon

# District uchun admin paneli
@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')  # admin panelida ko'rsatish
    autocomplete_fields = ['region']  # avtomatik to'ldirish
