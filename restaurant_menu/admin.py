from django.contrib import admin
from . models import Item

class MenuAdmin(admin.ModelAdmin):
    list_display = ('meal', 'status')
    list_filter = ('status',)
    search_fields =('meals', 'description')


admin.site.register(Item, MenuAdmin)