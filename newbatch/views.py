from django.shortcuts import render

# Create your views here.

from django.views import View
# from newbatch.models import NewBatch
from common.response import responses
from .models import NewBatch
import json

class AddNewBatch(View):
    def post(self,request):
        try:
            # print(request.GET.get['total'])
            input_values=json.loads(request.body.decode('utf-8'))
            print(input_values['total'])
            NewBatch.objects.update_or_create(total_chicks=input_values['total'])
            print("1")
            return responses('success',"ok")
        except Exception as e:
            print(e)
            return responses('failed',str(e))

    def get(self,request):
        try:
            input_values=json.loads(request.body.decode('utf-8'))
            return responses('success',{"message":input_values})
        except Exception as e:
            print(e)
            return responses('failed', str(e))






