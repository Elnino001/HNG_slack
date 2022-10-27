from django.contrib import admin
from . import models

class HngAdmin(admin.ModelAdmin):
    list_display = ('slackUsername', 'backend', 'age', 'bio')
    
admin.site.register(models.HngSlackDetails, HngAdmin)
