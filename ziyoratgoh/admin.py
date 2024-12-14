from django.contrib import admin
from .models import Ziyoratgoh,Carusel


admin.site.register(Carusel)

@admin.register(Ziyoratgoh)
class ZiyoratgohAdmin(admin.ModelAdmin):
    # List display
    list_display = ('title', 'tuman','subtitle')

    # Qidirish imkoniyati
    search_fields = ('title',)

    # Oddiy ro'yxatda ko'rsatish uchun
    fields = ('title', 'subtitle','rasm_first','rasm_second', 'about','viloyat','tuman','mehmonxona','oshxona','ustaxona','shifoxona')
