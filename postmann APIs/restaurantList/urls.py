from django.urls import path
from .views import RestaurantView

urlpatterns = [
    path('display/', RestaurantView.as_view()), #it will give nice format of the api
    path('display1/<int:pk>',RestaurantView.as_view()),
]