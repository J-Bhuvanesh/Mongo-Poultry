from django.conf.urls import url
from .views import AddNewBatch,AddImage

urlpatterns=[
    url(r'^create$', AddNewBatch.as_view(), name="Creating new batch"),
    url(r'^upload_images',AddImage.as_view(),name="for adding image and retriving"),

]