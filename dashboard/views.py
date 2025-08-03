from django.shortcuts import render,redirect,get_object_or_404
from urbanstay.forms import FlatFrom,INDIAN_STATES_CITIES
from urbanstay.models import Flat,Booking
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden,JsonResponse



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
