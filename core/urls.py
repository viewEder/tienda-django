# importamos url de django:
from django.urls import path
from core.views import HomePageView, HomeApiView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'inicio'),
    path('apiview', HomeApiView.as_view()),
]