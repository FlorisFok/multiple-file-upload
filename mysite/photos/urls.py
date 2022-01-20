from django.urls import include, path

from . import views

app_name = 'photos'

urlpatterns = [
    path(r'clear/', views.clear_database, name='clear_database'),
    path(r'basic-upload/', views.BasicUploadView.as_view(), name='basic_upload'),
    path(r'progress-bar-upload/', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    path(r'drag-and-drop-upload/', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),
]
