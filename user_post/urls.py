from django.urls import path
from user_post import views as user_post_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('posts/', user_post_views.AllPostsView.as_view(), name='all_posts'),
    path('user_posts/', user_post_views.UserPostsView.as_view(), name='user_posts'),
    path('create_post/', user_post_views.CreateUserPostView.as_view(), name='create_post'),
    path('post_detail/', user_post_views.PostDetailView.as_view(), name='post_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)