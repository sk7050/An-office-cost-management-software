from django.shortcuts import render,redirect
from django.urls import reverse

from .models import user_class,office_expense,product_cost
from .forms import User_Class,Office_expense,Product_cost




def email_check(mail):
      emaillist = list()
      detail=user_class.objects.order_by("name")
      for i in detail:
        emaillist.append(str(i.email))

      if mail in emaillist:
        return 1
      else:
        return 0
def pass_check(psw,name):
      if psw=="" or name=="":
        return -2
      else :
        try:
          detail=user_class.objects.get(name=name)
          password=detail.password
          if psw == password:
            return 1
          else:
            return -1
        except:
          return -3

        
def cont(error="",form1="",form2="",form3="",form4="",form5="",form6="",detail1="",detail2="",detail3="",detail4="",detail5="",detail6=""):
  context1={
    'error':error,
    'form1':form1,
    'form2':form2,
    'form3':form3,
    'form4':form4,
    'form5':form5,
    'form6':form6,
    'detail1':detail1,
    'detail2':detail2,
    'detail3':detail3,
    'detail4':detail4,
    'detail5':detail5,
    'detail6':detail6,
          }

  return context1

def login_user(user_name=''):
    if len(user_name) > 2:
      with open("temp_user.txt",'w',encoding = 'utf-8') as f:
        f.write(user_name)
    f = open("temp_user.txt",'r',encoding = 'utf-8')
    username=f.read()
    return username
def login_password(user_password=''):
    if len(user_password) > 2:
      with open("temp_password.txt",'w',encoding = 'utf-8') as f:
        f.write(user_password)
    f = open("temp_password.txt",'r',encoding = 'utf-8')
    userpassword=f.read()
    return userpassword
        
def Accounts_view(request):
  
  form=User_Class(request.POST or None)
  if request.method == 'POST':
    

    if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            check=email_check(email)
            password=form.cleaned_data['password']
            if check == 0:
                data=user_class(name=name,email=email,password=password)
                data.save() 
                context=cont(check,form)
                return render(request, 'base.html',context) 
            else:
              context=cont(check,form)
              return render(request, 'base.html',context)
    else:
      username=request.POST['name']
      password=request.POST['password']
      
      error=pass_check(password,username)
    
      if error== 1:
        username=login_user(username)
        password=login_password(password)
        context=cont(error,form1=Office_expense(),form2=Product_cost(),detail1=user_class.objects.get(name=username),detail2=office_expense.objects.all(),detail3=product_cost.objects.all())
        return render(request, 'user.html',context) 
      else:
        context=cont(error,form)
        return render(request, 'base.html',context) 
             
  else:  
    try:
      error=1
      username=login_user()
      #password=login_password()
      context=cont(error,form1=Office_expense(),form2=Product_cost(),detail1=user_class.objects.get(name=username),detail2=office_expense.objects.all(),detail3=product_cost.objects.all())
      return render(request, 'user.html',context)
     
             
  
    except:
        context=cont(form1=form)
        return render(request, 'base.html',context)
  

def accounts_view(request):
  
  if Office_expense(request.POST or None).is_valid():
        if request.method == 'POST':
          user_id=request.POST['user_name_id']  
          name_of_expense=request.POST['expense']
          cost_amount=request.POST['cost']
          month=request.POST['date_month']
          day=request.POST['date_day']
          year=request.POST['date_year']
          date=year+'-'+month+'-'+day
  
          exobject=office_expense(name_id_id=user_id,expense=name_of_expense,cost=cost_amount,date=date)  
          exobject.save()
          context=cont(error=0,form1=Office_expense(),form2=Product_cost(),detail1=user_class.objects.get(id=user_id),detail2=office_expense.objects.all(),detail3=product_cost.objects.all())
          return render(request, 'user.html',context)
        elif request.method == 'GET':
            error=1
            username=login_user()
            #password=login_password()
            context=cont(error,form1=Office_expense(),form2=Product_cost(),detail1=user_class.objects.get(name=username),detail2=office_expense.objects.all(),detail3=product_cost.objects.all())
            return render(request, 'user.html',context)
       
  elif Product_cost(request.POST or None).is_valid():
        if request.method == 'POST':
              user_id=request.POST['user_name_id']  
              name_of_products=request.POST['products']
              measurements_name=request.POST['measurements']
              measurements_type=request.POST['measurements_type']
              cost_amount=request.POST['cost']
              month=request.POST['date_month']
              day=request.POST['date_day']
              year=request.POST['date_year']
              date=year+'-'+month+'-'+day
  
              probject=product_cost(name_id_id=user_id,products=name_of_products,measurements=measurements_name,measurements_type=measurements_type,cost=cost_amount,date=date)  
              probject.save()
              context=cont(error=0,form1=Office_expense(),form2=Product_cost(),detail1=user_class.objects.get(id=user_id),detail2=office_expense.objects.all(),detail3=product_cost.objects.all())
              return render(request, 'user.html',context) 
        
        elif request.method == 'GET':
            error=1
            username=login_user()
            #password=login_password()
            context=cont(error,form1=Office_expense(),form2=Product_cost(),detail1=user_class.objects.get(name=username),detail2=office_expense.objects.all(),detail3=product_cost.objects.all())
            return render(request, 'user.html',context)
  else:
    try:
      error=1
      username=login_user()
      #password=login_password()
      context=cont(error,form1=Office_expense(),form2=Product_cost(),detail1=user_class.objects.get(name=username),detail2=office_expense.objects.all(),detail3=product_cost.objects.all())
      return render(request, 'user.html',context)
     
             
  
    except:
        return redirect('/')
      
        
  
      
def logout(request):
  with open("temp_user.txt",'w',encoding = 'utf-8') as f:
    f.write(" ")
  with open("temp_password.txt",'w',encoding = 'utf-8') as f:
    f.write(" ")
  return redirect('/')
      
    
    
        
def  office_expense_edit_view(request,id):
  
  

  obex=office_expense.objects.get(id=id)
  user_id=obex.name_id_id
  data = {'expense':obex.expense,
        'cost':obex.cost,
        'date':obex.date,
          }
  print(data)
  bd=Office_expense(data)
  if request.method=='POST':
    name_of_expense=request.POST['expense']
    cost_amount=request.POST['cost']
    month=request.POST['date_month']
    day=request.POST['date_day']
    year=request.POST['date_year']
    date=year+'-'+month+'-'+day
    office_expense.objects.filter(id=id).update(expense=name_of_expense,cost=cost_amount,date=date)
    context=cont(error=0,form1=Office_expense(),form2=Product_cost(),detail1=user_class.objects.get(id=user_id),detail2=office_expense.objects.all(),detail3=product_cost.objects.all())
    #return redirect('accounts',context) 
    return redirect('/login')
    
  context=cont(form1=bd,detail1=obex)
  return render(request, 'edit.html',context)
  
  

def product_purchase_edit_view(request,id):
  obex=product_cost.objects.get(id=id)
  user_id=obex.name_id_id
  data = {'products':obex.products,
        'measurements':obex.measurements,
        'measurements_type':obex.measurements_type,
        'cost':obex.cost,
        'date':obex.date,
          }
  print(data)
  bd=Product_cost(data)
  if request.method=='POST':
      name_of_products=request.POST['products']
      measurements_name=request.POST['measurements']
      measurements_type=request.POST['measurements_type']
      cost_amount=request.POST['cost']
      month=request.POST['date_month']
      day=request.POST['date_day']
      year=request.POST['date_year']
      date=year+'-'+month+'-'+day
  
      product_cost.objects.filter(id=id).update(products=name_of_products,measurements=measurements_name,measurements_type=measurements_type,cost=cost_amount,date=date)  
      
      return redirect('/login/accounts')
  context=cont(form3=bd,detail3=user_class.objects.get(id=user_id))
  return render(request, 'edit.html',context) 




      

