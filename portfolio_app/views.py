from django.shortcuts import render
# Create your views here.
import portfolio_app
from .models import Home
def home(request):

	projects=Home.objects.all()

	return render(request,"portfolio_app/home.html",{'data':projects})
