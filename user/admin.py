from django.contrib import admin
from .models import Modell, Images
from django.utils.safestring import mark_safe


# Register your models here.


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'profile', 'wth', 'price', 'time')

    # readonly_fields = ('image',)
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Изображение"


admin.site.register(Modell)
