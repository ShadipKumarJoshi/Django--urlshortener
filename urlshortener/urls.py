from django.contrib import admin
from django.urls import path
from shortener import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.shorten_url, name='shorten_url'),
    path('<str:short_code>/', views.redirect_to_original, name='redirect_to_original'),
]