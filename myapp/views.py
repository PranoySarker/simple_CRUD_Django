from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def InsertPageView(request):
    return render(request, "app/insert.html")


def InsertData(request):
    # data come form html to view
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    #creating object of modal class
    #Inserting data into table
    newuser = Student.objects.create(Firstname=fname, Lastname=lname, Email=email, Contact=contact)

    #after insert redirect data on show page view
    return redirect('showpage')

#show page view
def ShowPage(request):
    #select * from tablename query by django ORM
    # For fetching all the data of the table
    all_data = Student.objects.all()
    return render(request, "app/show.html", {'key1':all_data})

#Edit Page View
def EditPage(request,pk):
   #fetching the data of particular ID
   get_data = Student.objects.get(id=pk)
   return render(request, "app/edit.html", {'key2':get_data}) 

#update data view
def UpdateData(request,pk):
    udata = Student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']
    #query for update
    udata.save()
    #redirect to showpage
    return redirect('showpage')


def DeleteData(request,pk):
    ddata = Student.obejcts.get(id=pk)
    #query for delete
    ddata.delete()
     #redirect to showpage
    return redirect('showpage')