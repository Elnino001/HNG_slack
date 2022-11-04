from django.contrib import admin
from . import models

class HngAdmin(admin.ModelAdmin):
    list_display = ('slackUsername', 'backend', 'age', 'bio')
    
admin.site.register(models.HngSlackDetails, HngAdmin)


class ArithmeticAdmin(admin.ModelAdmin):
    list_display = ('operation_type', 'x', 'y')
    
admin.site.register(models.Arithmetic, ArithmeticAdmin)
