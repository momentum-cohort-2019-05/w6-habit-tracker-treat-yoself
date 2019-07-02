from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('habits/<int:pk>', views.habit_detail, name='habit-detail'),
]

urlpatterns += [
    path('habit/create/', views.HabitCreate.as_view(), name='habit-create'),
    path('habit/<int:pk>/delete/',
         views.HabitDelete.as_view(),
         name='habit-delete'),
]

urlpatterns += [
    path('dailyrecord/create/', views.DailyRecordCreate.as_view(),
         name='dailyrecord_create'),
    path('dailyrecord/<int:pk>/update/',
         views.DailyRecordUpdate.as_view(),
         name='dailyrecord_update'),
    path('dailyrecord/<int:pk>/delete/',
         views.DailyRecordDelete.as_view(),
         name='dailyrecord_delete'),
]
