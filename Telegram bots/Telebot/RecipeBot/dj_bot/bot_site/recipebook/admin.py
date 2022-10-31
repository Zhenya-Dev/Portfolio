from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class RecipeBookAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'user_name',
        'user_id',
        'profile_name',
        'gender')
    search_fields = ('name', 'last_name')
    list_filter = ('name', 'last_name', 'id')


admin.site.register(RecipeBook, RecipeBookAdmin)


class RecipeBook_recipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_html_photo', 'description')
    search_fields = ('title',)
    list_filter = ('title', 'id')
    fields = ('title', 'photo', 'get_html_photo', 'description')
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img scr={object.photo.url}' width=150>")

    get_html_photo.short_description = "Фото страви"


admin.site.register(RecipeBook_recipe, RecipeBook_recipeAdmin)


class FSMAdmin(admin.ModelAdmin):
    list_display = ('fsm_flag',)
    list_filter = ('fsm_flag',)
    readonly_fields = ('fsm_flag',)


admin.site.register(FSM, FSMAdmin)
