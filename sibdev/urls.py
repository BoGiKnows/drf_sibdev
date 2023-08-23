from django.urls import path
from sibdev.views import FileUploadView, TopFiveList

urlpatterns = [
    path('get-top/', TopFiveList.as_view()),
    path('post-deals/', FileUploadView.as_view()),
]