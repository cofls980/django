from django.urls import path
from . import views

urlpatterns = [
    path('color_update', views.color_update, name='color_update'),
    path('color_output', views.color_output, name='color_output'),
    path('text_insert', views.text_insert, name='text_insert'),
    path('text_update', views.text_update, name='text_update'),
    path('text_delete', views.text_delete, name='text_delete'),

]