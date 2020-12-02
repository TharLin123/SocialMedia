from django.urls import path
from . import views
from . views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('home/', PostListView.as_view(), name= "blog-home"),
    path('detail/<int:pk>/', PostDetailView.as_view(), name= "blog-detail"),
    path('post/', PostCreateView.as_view(), name= "blog-create"),
    path('update/<int:pk>/', PostUpdateView.as_view(), name= "blog-update"),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name= "blog-delete"),
    path('postuser/<str:username>/', UserPostListView.as_view(), name= "user-post"),
    path('password_reset/', PasswordResetView.as_view(template_name='password_rest.html'), name= "password_reset"),
    path('password_reset/sent', PasswordResetDoneView.as_view(template_name='password_rest_done.html'), name= "password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name= "password_reset_confirm"),
    path('password_reset/complete', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name= "password_reset_complete"),
]   