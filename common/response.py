from django.http import JsonResponse

def responses(type,content):
    res = dict()

    resp = dict()
    if type=='success':
        resp["status"] = 200
        resp["message"] = "Successfully Created"
        resp["content"]=content
        return JsonResponse(resp)
    else:
        resp["status"] = 400
        resp["message"] = "failed"
        resp["error"]=content
        return JsonResponse(resp)



