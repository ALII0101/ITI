from django.urls import path
from .views import *

urlpatterns = [
    path('', all_trainee,name='all_trainee'),
    path('id/', get_trainee),
    path('insert/', insert_trainee,name='insert_trainee'),
    path('update/<int:id>', update_trainee,name='update_trainee'),
    path('delete/<int:id>', delete_trainee,name='delete_trainee'),
]