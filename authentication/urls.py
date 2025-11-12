from django.urls import include, path
from authentication.views import create_news_flutter, login, logout, register
from authentication.views import proxy_image

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_news_flutter, name='create_news_flutter'),
    path('logout/', logout, name='logout')
]