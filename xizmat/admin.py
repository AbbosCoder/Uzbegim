from django.contrib import admin
from .models import Mehmonxona,Oshxona,Shifoxona,Ustaxona

@admin.register(Mehmonxona)
class MehmonxonaAdmin(admin.ModelAdmin):
    list_display = ('nomi','ish_kunlari','telefon_raqam','tuman','ochilish_vaqti','yopilish_vaqti',)  # admin panelida ko'rsatish
    search_fields = ('nomi',) 


@admin.register(Oshxona)
class OshxonaAdmin(admin.ModelAdmin):
    list_display = ('nomi','ish_kunlari','telefon_raqam','tuman','ochilish_vaqti','yopilish_vaqti',)  # admin panelida ko'rsatish
    search_fields = ('nomi',)


@admin.register(Ustaxona)
class UstaxonaAdmin(admin.ModelAdmin):
    list_display = ('nomi','ish_kunlari','telefon_raqam','tuman','ochilish_vaqti','yopilish_vaqti',)  # admin panelida ko'rsatish
    search_fields = ('nomi',) 


@admin.register(Shifoxona)
class ShifoxonaAdmin(admin.ModelAdmin):
    list_display = ('nomi','ish_kunlari','telefon_raqam','tuman','ochilish_vaqti','yopilish_vaqti',)  # admin panelida ko'rsatish
    search_fields = ('nomi',) 

