from django.http import HttpResponse
from django.shortcuts import render


def handleAction(request):
	print(request.POST['email'])

	return HttpResponse("<h1> Hello </h1>")


def homePage(request):
	return render(request,"userinput.html")