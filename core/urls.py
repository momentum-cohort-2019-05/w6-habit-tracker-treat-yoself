from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('habits/<int:pk>', views.habit_detail, name='habit-detail'),
]

# views for creating and deleting habits
urlpatterns += [
    path('habits/new/', views.new_habit, name='new-habit'),
    # path('habit/<int:pk>/delete/',
    #      views.HabitDelete.as_view(),
    #      name='habit-delete'),
]

# views for creating, updating, and deleting dailyrecords

urlpatterns += [
    path('habits/<int:pk>/new/', views.new_daily_record, name='new-record'),
]
