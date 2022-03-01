from django.urls import URLResolver, path
from .views import PersonAPIView

urlpatterns = [
    path('persons', PersonAPIView.as_view()),
    path('persons/<str:pk>', PersonAPIView.as_view()), # to capture our ids
]

