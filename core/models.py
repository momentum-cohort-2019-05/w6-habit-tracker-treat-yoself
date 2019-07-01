from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class Habit(models.Model):
    activity = models.CharField(
        max_length=200, help_text="What activity are you performing?")
    goal_num = models.PositiveIntegerField(default=0,
                                           help_text="How many units is your goal?")
    unit = models.CharField(
        max_length=200, help_text="What units are you completing? (steps, lines of code, hours, etc.")
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_started = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity} {self.goal_num} {self.unit}"


class DailyRecord(models.Model):
    num_achieved = models.PositiveIntegerField(default=0)
    owner_habit = models.ForeignKey(to=Habit, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

# need to change this string so it shows date and the input of the user that day
    def __str__(self):
        return f"{self.date} | {self.owner_habit}"

    class Meta:
        unique_together = ['date', 'owner_habit']
