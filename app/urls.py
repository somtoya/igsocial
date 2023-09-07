from django.urls import path
from app.views import post, user


urlpatterns = [
    path('', post.home, name='home'),
    path('signin/', user.signin, name='login'),
    path('signup/', user.signup, name='signup'),
    path('logout/', user.logout_user, name='logout')
]
