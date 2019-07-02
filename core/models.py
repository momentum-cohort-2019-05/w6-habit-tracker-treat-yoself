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

    class Meta:
        ordering = ['-date_started']


class DailyRecord(models.Model):
    date = models.DateField(default=date.today)
    num_achieved = models.PositiveIntegerField(default=0)
    goal_met = models.BooleanField(default=False)
    habit = models.ForeignKey(to=Habit, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-date']
        unique_together = ['habit', 'date']

    def __str__(self):
        return f"{self.date} | {self.num_achieved}"
