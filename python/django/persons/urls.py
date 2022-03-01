from django.urls import path
from . import views

app_name='persons'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:person_id>/delete', views.delete, name='delete'),
    path('<int:person_id>/update', views.update, name='update'),
    path('add/', views.add, name='add')
]