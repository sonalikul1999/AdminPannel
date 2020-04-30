from django.shortcuts import render, redirect
from django.views.decorators.csrf import *
from rest_framework import generics, filters
from app.models import *
from app.serializer import *

#API VIEWS START
class UserAPIView(generics.ListCreateAPIView):
	search_fields = ['User_Email','User_Password']
	filter_backends = (filters.SearchFilter, )
	queryset = UserData.objects.all()
	serializer_class = UserSerializer

class VendorAPIView(generics.ListCreateAPIView):
	search_fields = ['Vendor_Name']
	filter_backends = (filters.SearchFilter, )
	queryset = VendorsData.objects.all()
	serializer_class = VendorSerializer

#API VIEWS END
def basictable(request):
	return render(request,'basic_table.html',{})
def blank(request):
	return render(request,'blank.html',{})
def buttons(request):
	return render(request,'buttons.html',{})
def calendar(request):
	return render(request,'calendar.html',{})
def chartjs(request):
	return render(request,'chartjs.html',{})
def formcomponent(request):
	return render(request,'form_component.html',{})
def gallery(request):
    return render(request,'gallery.html',{})
def general(request):
   	return render(request,'general.html',{})
def lockscreen(request):
	return render(request,'lock_screen.html',{})
def login(request):
	return render(request,'login.html',{})
def morris(request):
	return render(request,'morris.html',{})
def panels(request):
	return render(request,'panels.html',{})
def responsivetable(request):
	return render(request,'responsive_table.html',{})
def todolist(request):
	return render(request,'todo_list.html',{})
def error(request):
	return render(request,'error.html',{})
@csrf_exempt
def adminlogin(request):
	if request.method=='POST':
		e=request.POST.get('email')
		p=request.POST.get('pass')
		request.session['admin_id'] = e
		if e=='admin@gazzapp.com' and p=='1234':
			return render(request,'index.html',{})
		else:
			return redirect('/error/')
def addvendor(request):
	try:
		if request.session['admin_id'] == 'admin@gazzapp.com':
			return render(request,'addvendor.html',{'data':VendorsCategoryData.objects.all()})
	except:
		return redirect('/error/')
def addvendorcategory(request):
	try:
		if request.session['admin_id'] == 'admin@gazzapp.com':
			return render(request,'addvendorcategory.html',{})
	except:
		return redirect('/error/')

@csrf_exempt
def savevendorcategory(request):
	try:
		if request.session['admin_id'] == 'admin@gazzapp.com':
			if request.method=="POST":
				n=request.POST.get('name')
				i=request.FILES['image']
				obj=VendorsCategoryData(
					VendorCategory_Name=n,
					VendorCategory_Image=i,
					)
				obj.save()
				return render(request,'addvendorcategory.html',{'msg':'Category Saved'})
	except:
		return redirect('/error/')
def addproduct(request):
	return render(request,'addproduct.html',{})
def addproductcategory(request):
	return render(request,'addproductcategory.html',{})
def displayvendor(request):
	try:
		if request.session['admin_id'] == 'admin@gazzapp.com':
			return render(request,'displayvendor.html',{'data':VendorsData.objects.all()})
	except:
		return redirect('/error/')

@csrf_exempt
def savevendor(request):
	try:
		if request.session['admin_id'] == 'admin@gazzapp.com':
			if request.method=="POST":
				sname=request.POST.get('shopname')
				oname=request.POST.get('ownername')
				address=request.POST.get('address')
				city=request.POST.get('city')
				state=request.POST.get('state')
				phone=request.POST.get('phone')
				email=request.POST.get('email')
				category=request.POST.get('category')
				obj=VendorsData(
					Vendor_Name=sname,
					Vendor_Category=category,
					Vendor_Owner=oname,
					Vendor_Address=address,
					Vendor_City=city,
					Vendor_State=state,
					Vendor_Phone=phone,
					Vendor_Email=email
					)
				obj.save()
				dic={'data':VendorsCategoryData.objects.all(),
					'msg':'Vendor Saved Successfully'}
				return render(request,'addvendor.html',dic)
			else:
				return redirect('/error/')
	except:
		return redirect('/error/')
def addvendorimages(request):
	try:
		if request.session['admin_id'] == 'admin@gazzapp.com':
			return render(request,'addvendorimages.html',{'data':VendorsData.objects.all()})
	except:
		return redirect('/error/')
def deletevendor(request):
	try:
		if request.session['admin_id'] == 'admin@gazzapp.com':
			return render(request,'deletevendor.html',{})
	except:
		return redirect('/error/')
def addvendorproduct(request):
	try:
		if request.session['admin_id'] == 'admin@gazzapp.com':
			return render(request,'addvendorproduct.html',{})
	except:
		return redirect('/error/')
def deleteproduct(request):
	try:
		if request.session['admin_id'] == 'admin@gazzapp.com':
			return render(request,'deleteproduct.html',{})
	except:
		return redirect('/error/')
def addproductimages(request):
	try:
		if request.session['admin_id'] == 'admin@gazzapp.com':
			return render(request,'addproductimages.html',{})
	except:
		return redirect('/error/')
def addvendorcategory(request):
	try:
		if request.session['admin_id'] == 'admin@gazzapp.com':
			return render(request,'addvendorcategory.html',{})
	except:
		return redirect('/error/')