from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('post/<int:pk>',views.PostDetailView,name="post-detail"),
    path('testimonials/', views.testimonials,name="testi"),
    path('students/', views.students,name="studd"),
    path('create_post/',views.createPost,name="createPost"),
  #  path('login/',views.loginPage,name="login"),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('userPage/',views.userPage,name="userPage"),
    path('userPosts/',views.userPosts,name="userPosts"),
    path('account/',views.account_info,name='account'),
    path('like/<int:pk>',views.LikeView,name='like_post'),
    path('post/comment/<int:pk>',views.addComment,name='addComment'),
    path('search_company',views.search_company,name='search-company'),

]
