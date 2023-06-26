from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .tasks import wa_queue
from django.urls import reverse
from .models import *
import csv

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')


def campaign(request):
    if request.method == 'POST':
        name = request.POST.get('namee', False)
        file = request.FILES.get('file', False)
        csv_data = file.read().decode('utf-8')
        
        wa_queue.delay(name, csv_data)
        # Return a response or redirect to another page
        return HttpResponseRedirect(reverse('campaign'))
    else:
        return render(request, 'campaign.html')

def wa_camps(request):
    context = {}
    campaigns = wa_camp.objects.all()
    context['camp_list'] = campaigns
    return render(request, 'camp_list.html', context)


def automation(request):
    return render(request, 'journey.html')