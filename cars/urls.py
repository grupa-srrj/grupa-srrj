from django.urls import path
from cars import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'cars'

urlpatterns= [
    path('list', views.list, name = 'list'),
    path('<int:id>', views.detail, name='detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)