from django.contrib import admin
from django.urls import path
from stories import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('submit/', views.submit_story, name='submit_story'),
]
