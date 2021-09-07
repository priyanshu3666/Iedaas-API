"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django import urls
from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from myapi import views


urlpatterns = [
    path('',include('myapi.urls')),
   path('admin/', admin.site.urls),
   path('employee/', views.EmployeeList.as_view()),
   path('teams/', views.Teams.as_view()),
   path('teams/chennai-super-kings/', views.ChennaiSuperKings.as_view()),
   path('teams/delhi-capitals/', views.DelhiCapitals.as_view()),
   path('teams/sunrisers-hyderabad/', views.SunRisersHydrabad.as_view()),
   path('teams/rajasthan-royals/', views.RajasthanRoyals.as_view()),
   path('teams/royal-challengers-bangalore/', views.RoyalChallengersBangalore.as_view()),
   path('teams/kings-xi-punjab/', views.KingsXIPunjab.as_view()),
   path('teams/kolkata-knight-riders/', views.KolkataKnightRiders.as_view()),
   path('teams/mumbai-indians/', views.MumbaiIndians.as_view()),

   

]

