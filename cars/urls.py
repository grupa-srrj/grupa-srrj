from django.contrib import admin
from django.urls import path
from cars import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', views.config),
    path('adding/', views.adding),
    path('subtraction/', views.subtraction),
    path('edition/', views.edition),
    path('our_fleet/', views.our_fleet),
    path('details/', views.details),
]