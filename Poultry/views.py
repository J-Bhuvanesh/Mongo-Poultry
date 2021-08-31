

from django.http import HttpResponse

def homepage(request):

    return HttpResponse("<h4 style='text-align:center'>POULTRY</h4>")