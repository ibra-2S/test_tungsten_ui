from django.shortcuts import render
from django.http import HttpResponse

def testapp(request):
  return render(request, 'testapp.html')