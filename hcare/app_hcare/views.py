from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse,HttpResponseRedirect

import MySQLdb as sqldb
import django.db

#from datetime import datetime
#from dateutil import tz
#from_zone = tz.gettz('UTC')
#to_zone = tz.gettz('America/Los_Angeles')


# Create your views here.

def main(request):
	return render(request, 'app_hcare/index.html',) 

def process_data(request):
	med = request.POST['med']
	return HttpResponse('Thanks for submitting your request for information on %s. We will have a recommendation for you in 2 weeks.'%med)

