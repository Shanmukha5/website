from django.shortcuts import render, HttpResponse
from .forms import ContactForm

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
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'website_base.html',{'form':form})
		else:
			form = ContactForm()
	return render(request,'website_contact.html',{'form':form})



