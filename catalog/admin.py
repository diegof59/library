from django.contrib import admin

from .models import Autor, Editor, Libro

class AutorAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido')
    
class LibroAdmin(admin.ModelAdmin):
    
    list_display = ('titulo', 'get_autor','editor', 'fecha_pub')
    list_filter =  ('fecha_pub',)
    date_hierarchy = 'fecha_pub'
    ordering = ('-fecha_pub',)
    filter_horizontal = ('autor',)
    raw_id_fields = ('editor',)
    
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editor)
admin.site.register(Libro, LibroAdmin)