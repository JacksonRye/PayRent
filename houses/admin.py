from django.contrib import admin
from .models import House, HouseImage

class HouseImageInline(admin.TabularInline):
    model = HouseImage
    extra = 3

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    inlines = [ HouseImageInline, ] 

admin.site.register(HouseImage)