from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/create/', views.create_user),
    path('users/top/',views.list_top_users),
    path('users/follow/',views.follow_user),
    path('posts/create/', views.create_post),
    path('posts/<int:post_id>/', views.individual_post),
    path('users/feed/<int:user_id>/',views.view_posts)
    # Add remaining endpoints here
]
