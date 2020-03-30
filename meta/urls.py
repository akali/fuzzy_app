from django.urls import path

from meta.views import FileUploadView, get_fuzzy_set, get_files_list

urlpatterns = [
    path('upload/', FileUploadView.as_view()),
    path('filter/', get_fuzzy_set),
    path('<str:creator>/files/', get_files_list)
]
