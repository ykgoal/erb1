from django.contrib import admin
from .models import Msglist

# Register your models here.

class MsglistAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    list_display_links = 'id', 'name',
    search_fields = 'id', 'name',
    list_filter = 'name',
    list_per_page = 25


admin.site.register(Msglist, MsglistAdmin)
