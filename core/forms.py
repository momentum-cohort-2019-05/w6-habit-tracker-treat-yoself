from django import forms
from datetime import date
from .models import DailyRecord


class NewHabitForm(forms.Form):
    activity = forms.CharField(
        max_length=200, help_text="What activity are you performing?")
    goal_num = forms.CharField(max_length=10,
                               help_text="How many units is your goal?")
    unit = forms.CharField(
        max_length=200, help_text="What units are you completing? (steps, lines of code, hours, etc.)")


class NewDailyRecordForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = ('date', 'num_achieved')
