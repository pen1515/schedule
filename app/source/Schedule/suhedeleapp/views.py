from django.shortcuts import render

# Create your views here.

def testView(request):
	return render(request, "suhedeleapp/test.html")