from django.urls import path, include
from .views import Home, logout_page, signup_view, login_page
urlpatterns = [
    path("", Home.as_view(), name="home"),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name="logout"),
    path('signup/', signup_view, name="signup"),
]
