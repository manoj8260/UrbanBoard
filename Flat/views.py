from django.shortcuts import render ,redirect
from django.http import JsonResponse
from django.views.generic import UpdateView ,DeleteView,DetailView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from Flat.models import Flat
from Flat.forms import FlatEditForm ,FlatFrom 
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from Flat.forms import FlatFrom,INDIAN_STATES_CITIES,FlatFilterForm
from Flat.models import Flat,Booking
from django.contrib import messages
# Create your views here.

class FlatDetailView(DetailView):
    model = Flat
    template_name = 'Flat/flat_detail.html'
    context_object_name = 'flat'


class EditFlatView(UpdateView , LoginRequiredMixin,UserPassesTestMixin):
    model = Flat
    form_class = FlatEditForm
    template_name = 'Flat/flat_edit.html'
    success_url  = reverse_lazy('landlord_dashboard')
    
    def test_func(self):
        flat = self.get_object()
        return self.request.user == flat.listed_by

class DeleteFlatView(DeleteView ,LoginRequiredMixin,UserPassesTestMixin):
    model = Flat
    template_name = 'Flat/flat_confirm_delete.html'
    success_url = reverse_lazy('landlord_dashboard')
    
    def test_func(self):
        flat = self.get_object()
        return self.request.user == flat.listed_by



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
        return render(request,'Flat/create_flat_listing.html' , {'form' : form})       

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
        return render(request,'Flat/booking_successful.html',{'flat':flat})  
    
    
def flat_list(request):
    flats = Flat.objects.all()
    form = FlatFilterForm(request.GET)

    if form.is_valid():
        state = form.cleaned_data.get('state')
        city = form.cleaned_data.get('city')
        bhk = form.cleaned_data.get('bhk')

        if state:
            flats = flats.filter(state__iexact=state)
        if city:
            flats = flats.filter(city__iexact=city)
        if bhk:
            flats = flats.filter(bhk=bhk)

    return render(request, 'dashboard/boarder_daskboard.html', {'form': form, 'flats': flats})
