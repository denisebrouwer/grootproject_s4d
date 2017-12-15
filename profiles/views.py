from django.shortcuts import render

# Create your views here.
def home (request):
	context = locals()
	template = 'home.html'
	return render(request,template,context)

def about (request):
	context = locals()
	template = 'about.html'
	return render(request,template,context)

def instellingen (request):
	context = locals()
	template = 'instellingen.html'
	return render(request,template,context)

def voorkeurlijst (request):
	context = locals()
	template = 'voorkeurlijst.html'
	return render(request,template,context)

def infolijst (request):
	context = locals()
	template = 'infolijst.html'
	return render(request,template,context)

def WeekPlanner (request):
	context = locals()
	template = 'WeekPlanner.html'
	return render(request,template,context)
