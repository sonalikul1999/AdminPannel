from django.shortcuts import render, redirect
from django.views.decorators.csrf import *

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
		if e=='admin@gazzapp.com' and p=='1234':
			return render(request,'index.html',{})
		else:
			return redirect('/error/')
def addvendor(request):
	return render(request,'addvendor.html',{})
def addproduct(request):
	return render(request,'addproduct.html',{})
def addproductcategory(request):
	return render(request,'addproductcategory.html',{})