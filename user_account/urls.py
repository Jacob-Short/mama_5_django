from django.urls import path
from user_account import views as user_account_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', user_account_views.IndexView.as_view(), name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)