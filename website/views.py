from django.shortcuts import render, HttpResponse
from .forms import FeedbackForm


def base(request):
	return render(request,'website_base.html')

def about(request):
	return render(request,'website_about.html')


def services(request):
	return render(request,'website_services.html')

def products(request):
	return render(request,'website_products.html')

def blog(request):
	return render(request,'website_blog.html')

def hiring(request):
	return render(request,'website_hiring.html')

def contact(request):
	return render(request,'website_contact.html')


def apps(request):
	return render(request,'website_apps.html')


def signup(request):
	return render(request,'website_signup.html')


def feedback(request):
	form = FeedbackForm()
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'website_base.html',{'form':form})
		else:
			form = FeedbackForm()
	return render(request,'website_feedback.html',{'form':form})



