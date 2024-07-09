from django.shortcuts import render, redirect
from django.views import View
from .models import Country, State
from django.contrib import messages

# Create your views here.

class Countryview(View):
 def get(self, request, slug=None):
  if slug:     
   countryobj = Country.objects.get(slug=slug)
   if countryobj.is_active:
    countryobj.is_active = False
    countryobj.save()
    return redirect('/')
   else:
    countryobj.is_active = True
    countryobj.save()
    return redirect('/')
  else:
   c_obj = Country.objects.all()
   return render(request, 'country.html', {'countryobj' : c_obj})
 
 def post(self, request, slug=None):
  if slug:
    countryobj = Country.objects.get(slug=slug)
    countryobj.delete()
    return redirect('/')
  else:
    c_country = request.POST.get('c_name')
    slug = request.POST.get('slug')
    code = request.POST.get('code')
    flag = request.FILES.get('flag')
    state_available = request.POST.get('state_available')
    if not state_available:
      state_available = False
    if Country.objects.filter(slug=slug).exists():
      messages.error(request, f"{slug} is already exists!!")
      return redirect('/')
    if Country.objects.filter(code=code).exists():
      messages.error(request,f"{code} is already exists!!")
      return redirect('/')
    
    Country.objects.create(name = c_country, slug = slug, code = code, flag = flag, is_state_available = state_available)
    messages.success(request,"Country is successfully created!!")
    return redirect('/')
  
class Countryupdate(View):
 def get(self, request, slug):
  obj = Country.objects.get(slug=slug)
  return render(request,'countryupdate.html',{'c_obj':obj})
 
 def post(self, request, slug):
    c_country = request.POST.get('c_name')
    slug = request.POST.get('slug')
    code = request.POST.get('code')
    flag = request.FILES.get('flag')
    state_available = request.POST.get('state_available')

    obj = Country.objects.get(slug=slug)
    if c_country:
      obj.name = c_country
     
    if slug:
      obj.slug = slug
    
    if code:
      obj.code = code
    
    if flag:
      obj.flag = flag
    
    if state_available:
      state_available = True
      obj.is_state_available = state_available
    else:
      obj.is_state_available = False
  
    obj.save()
    messages.success(request, f'Updated Successfully')
    return redirect('/')


