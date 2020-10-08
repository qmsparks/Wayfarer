from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:profile_id>/', views.profile_page, name='profile_page'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail')
]