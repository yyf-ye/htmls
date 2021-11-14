from django.urls import  path
from . import  views
app_name = 'blog'
urlpatterns = [
 path('', views.index, name='index'),
 path('posts/<int:pk>/', views.detail, name='detail'),
]
# 如果path这加了test,访问路径后面加/test,保持一致
