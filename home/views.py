from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home_page(request):
    first_block = Home_block.objects.all()
    second_block = Welcome_block.objects.all()
    thrid_block = Why_us.objects.all()
    fourth_block = Service_block.objects.all()
    fifth_block = Portfolio_block.objects.all()
    sixth_block = Social_networks.objects.all()
    seventh_block = Contact_block.objects.all()
    
    con = {'first':first_block,
		   'second':second_block,
		   'thrid':thrid_block,
		   'fourth':fourth_block,
		   'fifth':fifth_block,
		   'sixth':sixth_block,
		   'seventh':seventh_block
	}

    return render(request,'home/index.html', context=con)

# Create your views here.
