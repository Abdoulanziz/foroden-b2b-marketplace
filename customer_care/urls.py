from django.urls import path
from . import views

app_name = 'customer_care' 

urlpatterns = [
    path('', views.index, name='index'),
    path('metrics/', views.metrics, name='metrics'),
    path('reports/', views.reports, name='reports'),
    path('notifications/', views.notifications, name='notifications'),
    path('chats/', views.chats, name='chats'),
]