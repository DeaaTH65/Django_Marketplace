from django.urls import path
from . import views

app_name = 'chat'


urlpatterns = [
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
]
