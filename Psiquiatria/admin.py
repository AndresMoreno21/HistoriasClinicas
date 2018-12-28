from django.contrib import admin
from .models import Psiquiatria, Familiograma

# Register your models here.

class FamiliogramaPsiquiatriaInLine(admin.TabularInline):
    model = Psiquiatria.miembro.through
    

#class Historia_medicaAdmin(admin.ModelAdmin):
#    inlines = [HistoriaAperturaAdultosInLine,]

class PsiquiatriaAdmin(admin.ModelAdmin):
    inlines = [FamiliogramaPsiquiatriaInLine,]

    exclude = ('miembro',)

admin.site.register(Psiquiatria, PsiquiatriaAdmin)
admin.site.register(Familiograma)

