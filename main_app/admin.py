from django.contrib import admin
from .models import School, PlannedEvent, Chapter

# Register your models here.
admin.site.register(School)
admin.site.register(PlannedEvent)
admin.site.register(Chapter)
