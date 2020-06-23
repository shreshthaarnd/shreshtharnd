from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.mail import EmailMessage

def sitemap(request):
	return render(request,'srdsitemap.xml',{})
def index(request):
	return render(request,'index.html',{})
def aboutus(request):
	return render(request,'about.html',{})
def service(request):
	return render(request,'services.html',{})
def portfolio(request):
	return render(request,'portfolio.html',{})
def blog(request):
	return render(request,'blog.html',{})
def contact(request):
	return render(request,'contact.html',{})
def blogitem(request):
	return render(request,'blog-item.html',{})
@csrf_exempt
def contactmail(request):
	if request.method=="POST":
		n=request.POST.get('name')
		e=request.POST.get('email')
		s=request.POST.get('subject')
		m=request.POST.get('message')
		sub='New Query Message'
		msg='''Hi there!
Name : '''+n+'''
Email : '''+e+'''
Subject : '''+s+'''
Message : '''+m+'''

Thanks & Regards,
Team SRD'''
		email=EmailMessage(sub,msg,to=['shreshtharnd20@gmail.com'])
		email.send()
		sub='SRD - Thanks for Your Message!'
		msg='''Hi '''+n+''',
We got your message. We will contact you soon!

Thanks & Regards,
Team SRD'''
		email=EmailMessage(sub,msg,to=[e])
		email.send()
		return render(request,'contact.html',{'msg':'We have recieved your message.'})

@csrf_exempt
def newsletter(request):
	if request.method=="POST":
		e=request.POST.get('email')
		sub='Newsletter Subsciption'
		msg='''Hi there!
New newsletter Subsciption,

Email : '''+e+'''

Thanks & Regards,
Team SRD'''
		email=EmailMessage(sub,msg,to=['shreshtharnd20@gmail.com'])
		email.send()
		return render(request,'index.html',{})