from django.urls import path
from .views import *

urlpatterns = [
    path('', all_trainees),
    path('id/', get_trainee),
    path('insert/', insert_trainee),
    path('update/<int:id>', update_trainee),
    path('delete/<int:id>', delete_trainee),
]