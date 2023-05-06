from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import formBook
from app import models

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def book(request):
    submitted = False
    if request.method == 'POST':
        form = formBook(request.POST)
        time = request.POST.get('time')
        date = request.POST.get('date')
        #print(time,date)
        if form.is_valid:
            obj = models.Book.objects.all()
            bool = True
            for i in obj:
                if str(i.time) == str(time):
                    #print(str(date),formater(str(i.date)))
                    if str(date) == formater(str(i.date)):
                        bool = False
            if bool == True:
                print('form saved')
                form.save()
                submitted =True
                return HttpResponseRedirect('/book?submitted=True')
    else:
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'book.html',{'form': formBook,'submitted':submitted})

def menu(request):
    take = models.Menu.objects.all()
    mydic = {}
    for i in take:
        mydic[i.name] = [i.price,i.description,i.image]
    mydic = dict(sorted(mydic.items()))
    #print(mydic)
    return render(request,'menu.html',{'take':take,'mydic':mydic})

def about(request):
    return render(request,'about.html',{})

def page(request,name):
    take = models.Menu.objects.all()
    dic = {}
    for i in take:
        if i.name == name:
            source = i.image
            print(source)
            source = source
            dic = {"title": i.name,
            "image": source,
            "desc": i.description,
            "price": i.price}
    return render(request,'page.html',dic)

def formater(obj):
    obj = obj.replace('-','/')
    ls = ['1','2','3','4','5','6','7','8','9','0']
    ls[0] = obj[5]
    ls[1] = obj[6]
    ls[2] = obj[4]
    ls[3] = obj[8]
    ls[4] = obj[9]
    ls[5] = obj[7]
    ls[6] = obj[0]
    ls[7] = obj[1]
    ls[8] = obj[2]
    ls[9] = obj[3]
    from functools import reduce
    ret = listToStr = reduce(lambda a, b : a+ "" +str(b), ls)
    return ret