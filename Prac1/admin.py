from django.contrib import admin
from .models import Text, Color
# Register your models here.


class TextAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,        {'fields': ['pid', 'ptext']}),
    ]
    list_display = ('pid', 'ptext')


class ColorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,             {'fields': ['pid', 'pcolor']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


admin.site.register(Color, ColorAdmin)
admin.site.register(Text, TextAdmin)