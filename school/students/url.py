
from django.urls import path

from students import views


urlpatterns = [
    path("form/",views.stuform),
    path("fview/",views.stureg),
    path("fupdate/<int:pk>",views.stuupdate,name="update"),
    path("delete/<int:pk>",views.delete,name="update")
]