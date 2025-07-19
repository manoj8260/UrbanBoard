from django.shortcuts import render,redirect
from urbanstay.forms import FlatFrom,INDIAN_STATES_CITIES
from urbanstay.models import Flat
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden,JsonResponse
from django.contrib import messages

# Create your views here.
@login_required
def landlord_dashboard(request):
        if request.user.role!='landlord':
            return HttpResponseForbidden('Only landlords can add PG listing:')
        else:
            form=FlatFrom()
        user_flats=Flat.objects.filter(listed_by=request.user)
        return render(request,'dashboard/landlord_home.html',{'form':form,'user_flats':user_flats})
@login_required
def boarder_dashboard(request):
    all_PGs=Flat.objects.all().order_by('-created_at')
    return render(request,'dashboard/boarder_home.html',{'all_PGs':all_PGs})

def create_flat_listing(request):
        if request.method=='POST':
            form=FlatFrom(request.POST,request.FILES)
            if form.is_valid():
                flat=form.save(commit=False)
                flat.listed_by=request.user
                flat.save()
                return redirect('landlord_dashboard')
        else :    
         form = FlatFrom()
         return render(request,'dashboard/create_flat_listing.html' , {'form' : form})       


        
def load_cities(request):
    state_name = request.GET.get('state')
    cities = INDIAN_STATES_CITIES.get(state_name,[])
    city_choices = [{'id' : city , 'name' : city}for city in cities]
    return JsonResponse({'cities' : city_choices})