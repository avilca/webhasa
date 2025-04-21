from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    #para poner en modificar los enlaces de la redes sociales
    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name="Hasa").exists():
            return ('created', 'updated', 'key', 'name')
        else:
            return ('created', 'updated')

admin.site.register(Link, LinkAdmin)    