from django.shortcuts import render,redirect,get_object_or_404
from urbanstay.forms import FlatFrom,INDIAN_STATES_CITIES
from urbanstay.models import Flat,Booking
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden,JsonResponse
from django.contrib import messages

# Create your views here.
@login_required
def landlord_dashboard(request):
        if request.user.role!='Landlord':
            return HttpResponseForbidden('Only landlords can add PG listing:')
        else:
            form=FlatFrom()
        user_flats=Flat.objects.filter(listed_by=request.user)
        return render(request,'dashboard/landlord_home.html',{'form':form,'user_flats':user_flats})
@login_required
def boarder_dashboard(request):
    all_flats=Flat.objects.all().order_by('-listed_on')   
    return render(request,'dashboard/boarder_home.html',{'all_flats':all_flats})

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

@login_required
def book_flat(request,flat_id):
        flat=get_object_or_404(Flat,id=flat_id)
        if Booking.objects.filter(flat=flat,boarder=request.user).exists():
                messages.warning(request,'You have already requested this Flat')
        else:
            Booking.objects.create(flat=flat,boarder=request.user)
            messages.success(request,'Your booking request has been sent!')
        return render(request,'dashboard/booking_successful.html',{'flat':flat})