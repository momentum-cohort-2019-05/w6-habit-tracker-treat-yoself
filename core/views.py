from django.shortcuts import render, get_object_or_404
from .models import Habit, DailyRecord
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .forms import NewHabitForm, NewDailyRecordForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    """
    View function for home page of site.
    """
    habit_list = Habit.objects.all()
    # most_recent_record = habit.dailyrecord_set.order_by(‘-date’).first()

    context = {
        'habit_list': habit_list,
    }

    return render(request, 'index.html', context=context)


# def habit_detail(request, pk):
#     habit = Habit.objects.get(pk=pk)
#     habit_detail = habit.dailyrecord_set.all()

#     context = {
#         'habit': habit,
#         'habit_detail': habit_detail,
#     }

#     return render(request, 'core/habit_detail.html', context=context)

@login_required
def new_habit(request):
    if request.method == 'POST':
        form = NewHabitForm(request.POST)
        if form.is_valid():
            obj = Habit()
            obj.activity = form.cleaned_data['activity']
            obj.goal_num = form.cleaned_data['goal_num']
            obj.unit = form.cleaned_data['unit']
            obj.owner = request.user
            obj.save()
            return HttpResponseRedirect('/')

    # if GET (or any other method) create a blank form
    else:
        form = NewHabitForm()

    return render(request, 'core/habit_form.html', {
        'form': form,
    })


@login_required
def new_daily_record(request, pk):
    habit = get_object_or_404(Habit, id=pk)

    if request.method == 'POST':
        form = NewDailyRecordForm(request.POST)
        if form.is_valid():
            obj = DailyRecord()
            obj.num_achieved = form.cleaned_data['num_achieved']
            obj.date = form.cleaned_data['date']
            obj.save()
            return HttpResponseRedirect('/')

    # if GET (or any other method) create a blank form
    else:
        form = NewDailyRecordForm()

    return render(request, 'core/dailyrecord_form.html', {
        'form': form, 'habit': habit,
    })
