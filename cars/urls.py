from django.urls import path
from cars import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'cars'

urlpatterns= [
    path('', views.fleet, name='fleet'),
    path('<int:car_id>/', views.details, name='details'),
    path('rent_form', views.rent_form, name='rent_form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
