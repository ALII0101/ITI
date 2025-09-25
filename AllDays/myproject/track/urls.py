from django.urls import path
from .views import *
urlpatterns = [

    path('', all_tracks,name='all_tracks'),
    path('id/', get_track),
    path('insert/', insert_track),
    path('update/<int:id>', update_track,name='update_track'),
    path('delete/<int:id>', delete_track,name='delete_track'),

]
 