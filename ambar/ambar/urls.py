"""
URL configuration for ambar project.
"""
from django.contrib import admin
from django.urls import path

from core.views import IndexView, DataFormView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("submit/", DataFormView.as_view(), name="submit-data"),
    path("admin/", admin.site.urls),
]
