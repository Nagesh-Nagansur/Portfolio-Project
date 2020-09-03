from django.urls import path
from . import views

urlpatterns = [
        path('',views.blog,name='blog-home'),
        path('all_blogs/',views.all_blogs,name='allBlogs'),
        path('<int:blog_id>',views.detail,name='detail'),
]
