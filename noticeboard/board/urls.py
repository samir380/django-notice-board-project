from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import NoticeListView, NoticeDetailView, NoticeCreateView, NoticeUpdateView, NoticeDeleteView, FileDownloadView

urlpatterns = [
    path('', NoticeListView.as_view(), name='notice_list'),
    path('notices/<uuid:pk>/', NoticeDetailView.as_view(), name='notice_detail'),
    path('notices/create/', NoticeCreateView.as_view(), name='notice_create'),
    path('notices/<uuid:pk>/update/', NoticeUpdateView.as_view(), name='notice_update'),
    path('notices/<uuid:pk>/delete/', NoticeDeleteView.as_view(), name='notice_delete'),
    path('notices/<uuid:pk>/download/', FileDownloadView.as_view(), name='download_file'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)