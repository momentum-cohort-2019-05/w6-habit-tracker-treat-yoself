from django.shortcuts import render
from .models import Habit, DailyRecord
# Create your views here.


def index(request):
    """
    View function for home page of site.
    """
    habit_list = Habit.objects.all()

    


    context = {
        'habit_list': habit_list,
    }

    return render(request, 'index.html', context=context)
