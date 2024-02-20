
from django.urls import path

from teachers import views


urlpatterns = [
    path("form/",views.teaform),
    path("fview/",views.teareg,name='viewst'),
    path("fupdate/<int:pk>",views.teaupdate,name="tupdate"),
    path("delete/<int:pk>",views.delete,name="tupdate")
]