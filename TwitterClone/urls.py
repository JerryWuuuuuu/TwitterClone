"""TwitterClone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from core.views import splash, signup_view, login_view, home_view, tweet, profile_view, logout_action, hashtag_view, like_tweet, delete_tweet, hashtag_all_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splash, name = "splash"),
    path('signup', signup_view, name = "signup"),
    path('login', login_view, name = "login"),
    path('home', home_view, name = "home"),
    path('tweet', tweet, name = "tweet"),
    path('profile/<author>', profile_view, name = "profile"),
    path('logout', logout_action, name = 'logout'),
    path('hashtag/<hashtag>', hashtag_view, name = "hashtag"),
    path('like/<id>', like_tweet, name = "like_tweet"),
    path('delete/<id>', delete_tweet, name = "delete_tweet"),
    path('hashtag', hashtag_all_view, name = "hashtag_all_view")
]
