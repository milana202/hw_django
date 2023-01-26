from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

with open ('data-398-2018-08-30.csv') as file:
    content = csv.DictReader(file)

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    pagi = Paginator(content, 15)
    page = pagi.get_page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': pagi,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
