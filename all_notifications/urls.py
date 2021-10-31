from django.urls import path
from all_notifications import views as notification_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('notifications/<int:id>/', notification_views.AllNotificationsView.as_view(), name='notifications'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)