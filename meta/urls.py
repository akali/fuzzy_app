from django.urls import path

from meta.views import FileUploadView

urlpatterns = [
    path('upload/', FileUploadView.as_view())
]
