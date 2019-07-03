from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('habits/', views.user_profile, name='user-profile'),
    path('habits/<int:pk>', views.habit_detail, name='habit-detail'),
]

# views for creating and deleting habits
urlpatterns += [
    path('habits/new/', views.new_habit, name='new-habit'),
    path('habits/<int:pk>/delete/',
         views.HabitDelete.as_view(),
         name='habit-delete'),
]

# views for creating, updating, and deleting dailyrecords
urlpatterns += [
    path('habits/<int:pk>/new/', views.new_daily_record, name='new-record'),
    path('records/<int:pk>/update/',
         views.DailyRecordUpdate.as_view(),
         name='update-record'),
    path('records/<int:pk>/delete/',
         views.DailyRecordDelete.as_view(),
         name='delete-record'),
]
