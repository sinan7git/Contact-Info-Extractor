from django.urls import path
from.views import search_and_enhance

urlpatterns = [
    path('', search_and_enhance),
]

