from django.urls import path
from django.conf.urls.static import static
from django.urls import include
from .views import home_page

urlpatterns = [
    path('', home_page, name='home_page_url'),
]