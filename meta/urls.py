from django.urls import path

from meta.views import FileUploadView, get_fuzzy_set

urlpatterns = [
    path('upload/', FileUploadView.as_view()),
    path('filter/', get_fuzzy_set)
]
