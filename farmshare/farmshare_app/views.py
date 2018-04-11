from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    my_list = ['hello', 'there']
    return render(request, 'farmshare_app/index.html', {'names' : my_list} )