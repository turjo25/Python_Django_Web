from django.http import HttpResponse
#request and response built in function
def home(request):
    return HttpResponse("<h1>Hello World</h1>")
