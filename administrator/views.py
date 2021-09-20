from django.shortcuts import render
from math import radians, cos, sin, asin, sqrt
from .models import pharmacy


def index(request):
    distance = dist(8.337611, 5.131840, 8.02315646, 5.131840)
    print(request.user)
    return render(request, 'administrator/index.html')


def findPharmacy(request):
    allPharmacy = pharmacy.objects.all()
    nearestPharmacyDistance = 99999
    nearestPharmacyID = None
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        for each in allPharmacy:
            temp = dist(float(latitude), float(longitude), float(each.lattitude), float(each.longitude))
            if temp < nearestPharmacyDistance:
                nearestPharmacyDistance = temp
                nearestPharmacyID = each.id
        context = {'nearestPharmacy': pharmacy.objects.get(id=nearestPharmacyID)}
        return render(request, 'administrator/findPharmacy.html', context)
    return render(request, 'administrator/findPharmacy.html')


def dist(lat1, long1, lat2, long2):
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
    dlon = long2 - long1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km
