from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'cars'

urlpatterns= [
    path('', views.fleet, name='fleet'),
    path('<int:car_id>/', views.details, name='details'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
