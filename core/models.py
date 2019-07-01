from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Habit(models.Model):
    activity = models.CharField(
        max_length=200, help_text="What activity are you performing?")
    goal_num = models.PositiveIntegerField(default=0,
                                           help_text="How many units is your goal?")
    unit = models.CharField(
        max_length=200, help_text="What units are you completing? (steps, lines of code, hours, etc.")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.activity} {self.goal_num} {self.unit}"


class DailyRecord(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    user_habit = models.ForeignKey(to=Habit, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

# need to change this string so it shows date and the input of the user that day
    def __str__(self):
        return f"{self.date} | {self.user_habit}"

    class Meta:
        unique_together = ['user', 'user_habit']
