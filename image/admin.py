from django.contrib import admin

# Register your models here.

from .models import *


class ImageAdmin(admin.ModelAdmin):


    list_display=('image', 'title', 'product_description', 'price')

    list_filter=('image', 'title','price')



admin.site.register(Image_u, ImageAdmin)