from django.contrib import admin
from .models import Post,Comentario
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','status','create_on')
    search_fields =['titulo','contenido']

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('nombre', 'email', 'body')
    actions = ['desactivar_comentarios']

    def desactivar_comentarios(self, request, queryset):
        queryset.update(active=False)

admin.site.register(Post,PostAdmin)
admin.site.register(Comentario,ComentarioAdmin)
