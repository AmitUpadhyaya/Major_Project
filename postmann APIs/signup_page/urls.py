from django.urls import path
from .import views
from .views import SignupApiView

urlpatterns=[
    path('Signup/', views.signup),
    path('abc/', views.signupUser, name="signupBtn"),
    path('login1/', SignupApiView.as_view()),
    path('login1/<int:pk>', SignupApiView.as_view()),
]