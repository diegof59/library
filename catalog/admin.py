from django.contrib import admin

from .models import Autor, Editor, Libro

class AutorAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido')
    
class LibroAdmin(admin.ModelAdmin):
    
    list_display = ('titulo', 'editor', 'fecha_pub')
    list_filter =  ('fecha_pub',)
    date_hierarchy = 'fecha_pub'
    
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editor)
admin.site.register(Libro, LibroAdmin)