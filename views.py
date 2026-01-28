from django.shortcuts import render,redirect


# Create your views here.
def home(request):
	return render(request,'base.html')
def services(request):
	return render(request,'services.html')
def portfolio(request):
	return render(request,'portfolio.html')
def contact(request):
	return render(request,'contact.html')
	