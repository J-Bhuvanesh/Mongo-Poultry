from django.conf.urls import url
from .views import AddNewBatch

urlpatterns=[
    url(r'^create$', AddNewBatch.as_view(), name="Creating new batch"),

]