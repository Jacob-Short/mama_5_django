from django.urls import path
from user_account import views as user_account_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', user_account_views.IndexView.as_view(), name='index'),
    path('home/', user_account_views.HomeView.as_view(), name='home'),
    path('login/', user_account_views.LoginView.as_view(), name='login'),
    path('logout/', user_account_views.logout_view, name='logout'),
    path('register/', user_account_views.RegisterView.as_view(), name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)