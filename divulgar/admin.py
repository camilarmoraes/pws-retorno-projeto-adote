from django.contrib import admin
from .models import Raca,Tag,Pet

class RacaAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Raca)
admin.site.register(Tag)
admin.site.register(Pet)