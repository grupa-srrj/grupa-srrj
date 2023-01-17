from django.urls import path
from . import views


app_name = 'cars'

urlpatterns= [
    path('', views.fleet, name='fleet'),
    path('<int:car_id>/', views.details, name='details'),
    # testing view for details
    path('details/', views.test_details, name='test_details'),
]
