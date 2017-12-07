from django.test import TestCase

# Create your tests here.
def contact(request):
	context = locals()
	template = 'contact.html'
	return render(request,template,context)