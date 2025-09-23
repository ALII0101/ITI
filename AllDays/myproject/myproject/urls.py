"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myuser.views import *
from track.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', login),
    # path('logout/', logout),
    # path('register/', register),
    path('',include('myuser.urls')),
    # path('all_tracks/', all_tracks),
    # path('get_track/', get_track),
    # path('insert_track/', insert_track),
    # path('update_track/', update_track),
    # path('delete_track/', delete_track),
    path('tracks/',include('track.urls')),
    path('trainees/', include('trainee.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 