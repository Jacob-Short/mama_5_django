from django.urls import path
from tranont import views as tranont_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('tranont/', tranont_views.TranontIndexView.as_view(), name='tranont_index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)