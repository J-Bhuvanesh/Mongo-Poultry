from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.views import View
# from newbatch.models import NewBatch
from common.response import responses
from .models import NewBatch,ImageFile
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


class AddImage(View):
    def post(self,request):
        try:
            file_list = request.FILES.getlist('file')
            print(type(file_list))
            # print(file_list[0].temporary_file_path())
            print(type(file_list[0]))
            image = open(file_list[0].temporary_file_path(), 'rb')
            image_read = image.read()
            import base64
            print(type(image_read))
            image_64_encode = base64.encodestring(image_read)
            print(type(image_64_encode))
            img_obj = ImageFile()
            img_obj.image_data = image_64_encode
            img_obj.save()
            return responses('success',"ok")
        except Exception as e:
            print(e)
            return responses('failed','error')

    def get(self,request):
        try:
            img_obj = list(ImageFile.objects.all().values())
            print(img_obj[0])
            k = img_obj[0]
            lm = (bytes(k['image_data']))
            import base64
            image_64_decode = base64.decodestring(lm)
            print(type(image_64_decode))
            import io
            from PIL import Image
            from io import BytesIO
            # assume data contains your decoded image
            im = Image.open(BytesIO(image_64_decode))
            # im.save('aaaaa.png', 'PNG')
            response = HttpResponse(content_type="image/png",
                                    headers={'Content-Disposition': 'attachment; filename="somefilename.png"'})
            im.save(response, 'PNG')
            return response


        except Exception as e:
            return responses('failed','error')





