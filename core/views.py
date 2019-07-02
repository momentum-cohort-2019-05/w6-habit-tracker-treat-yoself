from django.shortcuts import render
from .models import Habit, DailyRecord
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .forms import NewHabitForm
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


# OLD MODELS FOR CREATE/UPDATE/DELETE

# from django.views.generic.edit import CreateView, UpdateView, DeleteView

# class HabitCreate(CreateView):
#     model = Habit
#     fields = ['activity', 'goal_num', 'unit']

# class HabitDelete(DeleteView):
#     model = Habit
#     success_url = reverse_lazy('index')


# class DailyRecordCreate(CreateView):
#     model = DailyRecord
#     fields = ['date', 'num_achieved', 'habit']


# class DailyRecordUpdate(UpdateView):
#     model = DailyRecord
#     fields = ['date', 'num_achieved']


# class DailyRecordDelete(DeleteView):
#     model = DailyRecord
#     success_url = reverse_lazy('index')
