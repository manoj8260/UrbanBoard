from django.shortcuts import render,redirect
from PG.forms import PGlistingform
from PG.models import PGlisting
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
# Create your views here.
@login_required
def landlord_dashboard(request):
        if request.user.role!='landlord':
            return HttpResponseForbidden('Only landlords can add PG listing:')
        if request.method=='POST':
            form=PGlistingform(request.POST)
            if form.is_valid():
                pg=form.save(commit=False)
                pg.owner=request.user
                pg.save()
                form=PGlistingform()

        else:
            form=PGlistingform()
        user_PGs=PGlisting.objects.filter(owner=request.user)
        return render(request,'dashboard/landlord_home.html',{'form':form,'user_PGs':user_PGs})
@login_required
def boarder_dashboard(request):
    all_PGs=PGlisting.objects.all().order_by('-created_at')
    return render(request,'dashboard/boarder_home.html',{'all_PGs':all_PGs})