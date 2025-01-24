from django.contrib import admin
from index.models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [ 'full_name', 'rank', 'tap_count', 'profile_pic']
    list_filter = ['date_of_birth']
    search_fields = ['date_of_birth']

@admin.register(Ranks)
class RanksAdmin(admin.ModelAdmin):
    list_display = ['title', 'coin', 'id']