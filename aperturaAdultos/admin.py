from django.contrib import admin
from .models import *

"""class HistoriaAperturaAdultosInLine(admin.TabularInline):
    model = AperturaAdultos.historias_medicas.through
    

#class Historia_medicaAdmin(admin.ModelAdmin):
#    inlines = [HistoriaAperturaAdultosInLine,]

class AperturaAdultosAdmin(admin.ModelAdmin):
    inlines = [HistoriaAperturaAdultosInLine,]

    exclude = ('historias_medicas',)"""



# Register your models here.


admin.site.register(AperturaAdultos)

#admin.site.register(AperturaAdultos, AperturaAdultosAdmin)

