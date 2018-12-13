"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from facebook.views import play, play2, profile, event, help, fail, warn, newsfeed, detail_feed, new_feed, edit_feed, remove_feed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('play/', play),
    path('play2/', play2), #play2 함수를 실행해
    path('yangyoun/profile/', profile),
    path('event/', event),
    path('help/', help),
    path('fail/', fail),
    path('warn/', warn),
    path('/', newsfeed),
    path('feed/<pk>/', detail_feed),
    path('new/', new_feed),
    path('feed/<pk>/edit/', edit_feed),
    path('feed/<pk>/remove/', remove_feed),
]
