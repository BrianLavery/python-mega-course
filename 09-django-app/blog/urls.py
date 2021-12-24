from . import views
from django.urls import path

# Routes are defined here
urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name = 'blog_view'), # This is defined in views.py
    path('about/', views.AboutView.as_view(), name = 'about_view'),
    path('', views.PostList.as_view(), name = 'home')
]
