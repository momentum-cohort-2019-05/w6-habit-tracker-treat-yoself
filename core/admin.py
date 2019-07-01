from django.contrib import admin
from .models import Habit, DailyRecord

# Register your models here.
admin.site.register(Habit)
admin.site.register(DailyRecord)
