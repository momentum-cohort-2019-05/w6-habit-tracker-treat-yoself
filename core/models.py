from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Habit(models.Model):
    activity = models.CharField(max_length=200)
    goal_num = models.PositiveIntegerField
    unit = models.CharField(max_length=200)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.activity} {self.goal_num} {self.unit}"


class DailyRecord(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    user_habit = models.ForeignKey(to=Habit, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} | {self.user_habit}"

    class Meta:
        unique_together = ['user', 'user_habit']
