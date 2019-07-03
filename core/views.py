from django.shortcuts import render, get_object_or_404, redirect
from .models import Habit, DailyRecord
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .forms import NewHabitForm, NewDailyRecordForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

def user_profile(request):
    habit_list = Habit.objects.all()

    context = {
        'habit_list': habit_list,
    }

    return render(request, 'core/user_profile.html', context=context)

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    habit_detail = habit.dailyrecord_set.all()
    records_list = []
    for record in DailyRecord.objects.filter(habit=habit):
        records_list.append(record)

    context = {
        'habit': habit,
        'habit_detail': habit_detail,
        'records_list' : records_list,
    }

    return render(request, 'core/habit_detail.html', context=context)


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
            return HttpResponseRedirect('core/habits/')

    # if GET (or any other method) create a blank form
    else:
        form = NewHabitForm()

    return render(request, 'core/habit_form.html', {
        'form': form,
    })


class HabitDelete(DeleteView):
    model = Habit
    success_url = reverse_lazy('index')


@login_required
def new_daily_record(request, pk):
    habit = get_object_or_404(Habit, id=pk)

    if habit.owner != request.user:
        messages.warning(
            request, "You tried to add a daily record to a habit that you do not own!")
        return redirect('/')

    if request.method == 'POST':
        form = NewDailyRecordForm(request.POST)
        if form.is_valid():
            obj = DailyRecord()
            obj.num_achieved = form.cleaned_data['num_achieved']
            obj.date = form.cleaned_data['date']
            obj.habit = habit
            obj.save()
            return HttpResponseRedirect('/')

    # if GET (or any other method) create a blank form
    else:
        form = NewDailyRecordForm()

    return render(request, 'core/dailyrecord_form.html', {
        'form': form, 'habit': habit,
    })


class DailyRecordUpdate(UpdateView):
    model = DailyRecord
    fields = ['date', 'num_achieved']
    template_name_suffix = '_update_form'


class DailyRecordDelete(DeleteView):
    model = DailyRecord
    success_url = reverse_lazy('index')
