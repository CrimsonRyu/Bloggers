from . import views
from django.urls import path
from mysite import settings
from django.conf.urls import url

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    url(r'/$',views.new, name='newpage'),
    path(r'/$',views.main, name='main'),
    ]