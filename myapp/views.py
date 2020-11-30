from django.shortcuts import render,redirect
from django.urls import reverse

from .models import user_class,office_expense,product_cost,sold_data
from .forms import User_Class,Office_expense,Product_cost,Sold_data
from django.contrib.sessions.models import Session



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
        request.session['username'] = username
        password=login_password(password)
        context=cont(error,form1=Office_expense(),form2=Product_cost(),form3=Sold_data(),detail1=user_class.objects.get(name=username),detail2=office_expense.objects.all(),detail3=product_cost.objects.all())
        return render(request, 'user.html',context) 
      else:
        context=cont(error,form)
        return render(request, 'base.html',context) 
             
  else:  
    try:
      with open("temp_user.txt",'w',encoding = 'utf-8') as f:
          f.write(" ")
      with open("temp_password.txt",'w',encoding = 'utf-8') as f:
          f.write(" ")
      error=1
      username=login_user()
      #password=login_password()
      context=cont(error,form1=Office_expense(),form2=Product_cost(),form3=Sold_data(),detail1=user_class.objects.get(name=username),detail2=office_expense.objects.all(),detail3=product_cost.objects.all())
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
          username=login_user(user_class.objects.get(id=user_id).name)
          return redirect('/login/accounts/')
        elif request.method == 'GET':
            error=1
            username=login_user()
            #password=login_password()
            context=cont(error,form1=Office_expense(),form2=Product_cost(),form3=Sold_data(),detail1=user_class.objects.get(name=username),detail2=office_expense.objects.all(),detail3=product_cost.objects.all())
            return render(request, 'user.html',context)
       
  elif Product_cost(request.POST or None).is_valid():
        if request.method == 'POST':
              user_id=request.POST['user_name_id']  
              name_of_products=request.POST['products']
              measurements_name=request.POST['measurements']
              measurements_type=request.POST['measurements_type']
              cost_amount=request.POST['cost_per_measurement']
              month=request.POST['date_month']
              day=request.POST['date_day']
              year=request.POST['date_year']
              date=year+'-'+month+'-'+day
              total_cost=float(measurements_name)*float(cost_amount)
  
              probject=product_cost(name_id_id=user_id,products=name_of_products,measurements=measurements_name,measurements_type=measurements_type,cost=total_cost,date=date)  
              probject.save()
              username=login_user(user_class.objects.get(id=user_id).name)
              return redirect('/login/accounts/')
        elif request.method == 'GET':
            error=1
            username=login_user()
            #password=login_password()
            context=cont(error,form1=Office_expense(),form2=Product_cost(),form3=Sold_data(),detail1=user_class.objects.get(name=username),detail2=office_expense.objects.all(),detail3=product_cost.objects.all())
            return render(request, 'user.html',context)

  elif Sold_data(request.POST or None).is_valid():
        if request.method == 'POST':
           
          #name_of_expense=request.POST['expense']
          #cost_amount=request.POST['cost']
          #month=request.POST['date_month']
          #day=request.POST['date_day']
          #year=request.POST['date_year']
          #date=year+'-'+month+'-'+day
  
          object=Sold_data(request.POST) 
          object.save()
          username=login_user(request.session['username'])
          
          return redirect('/login/accounts/')
        elif request.method == 'GET':
            error=1
            username=login_user()
            #password=login_password()
            context=cont(error,form1=Office_expense(),form2=Product_cost(),form3=Sold_data(),detail1=user_class.objects.get(name=username),detail2=office_expense.objects.all(),detail3=product_cost.objects.all())
            return render(request, 'user.html',context)
        else:
            print("error")
            return redirect('/login/')
  
  else:
    try:
      error=1
      username=login_user()
      username=login_user(request.session['username'])
      #password=login_password()
      context=cont(error,form1=Office_expense(),form2=Product_cost(),form3=Sold_data(),detail1=user_class.objects.get(name=username),detail2=office_expense.objects.all(),detail3=product_cost.objects.all())
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
  
  bd=Office_expense(data)
  if request.method=='POST':
    name_of_expense=request.POST['expense']
    cost_amount=request.POST['cost']
    month=request.POST['date_month']
    day=request.POST['date_day']
    year=request.POST['date_year']
    date=year+'-'+month+'-'+day
    office_expense.objects.filter(id=id).update(expense=name_of_expense,cost=cost_amount,date=date)
    username=login_user(user_class.objects.get(id=user_id).name)
   
    #return redirect('accounts',context) 
    return redirect('/login/accounts/')
    
  context=cont(form1=bd,detail1=user_class.objects.get(id=user_id))
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
      username=login_user(user_class.objects.get(id=user_id).name)  
      
      return redirect('/login/accounts/')
  context=cont(form3=bd,detail3=user_class.objects.get(id=user_id))
  return render(request, 'edit.html',context) 

def sold_data_view(request):
  sell_amount=0
  for i in sold_data.objects.all():
    sell_amount += i.sold_price
  
  context=cont(detail1=sold_data.objects.all())
  context['total_sell']=sell_amount 
  
  
  return render(request, 'sold_data.html',context)


def office_account_view(request):
  context={}
  office_cost=0
  purchase_cost=0
  Office_user=[]
  Employee_name={}
  for i in user_class.objects.all():
    Office_user.append(i.name)
  
  n=0
  x=0
  Expense_by_Office_Account=0
  
  for j in Office_user:
    
    for i in office_expense.objects.filter(name_id_id=user_class.objects.get(name=j).id):
      Employee_name.setdefault('office_expense'+'_'+str(i.name_id_id),[])
      Employee_name['office_expense'+'_'+str(i.name_id_id)].append(i.cost)
      #of=Employee_name.setdefault('office_expense'+'_'+str(i.name_id_id))
    for i in product_cost.objects.filter(name_id_id=user_class.objects.get(name=j).id):
      Employee_name.setdefault('product_cost'+'_'+str(i.name_id_id),[])
      Employee_name['product_cost'+'_'+str(i.name_id_id)].append(i.cost)
      #po=Employee_name.setdefault('product_cost'+j)
  for user in user_class.objects.all():
    for keys,values in Employee_name.items(): 
      #if str(user.id) == str(keys.split('_')[1]):
        n+=1
        context[keys]=sum(values)
        context['user'+'_'+str(user.id)]=user_class.objects.get(id=user.id).name
        context.setdefault('no',[])
        context['no'].append(n)
    for k,v in context.items():
      if(len(k.split('_')))==3:
        if (user_class.objects.get(id=(k.split('_')[2])).name) =='Office_Account':
           if 'office_expense_'+str(user.id) in k or 'product_cost_'+str(user.id) in k :
             
             Expense_by_Office_Account +=float(v)

      
      if 'office_expense_'+str(user.id) in k or 'product_cost_'+str(user.id) in k :
        x+=float(v)

        
       
  
  context['Expense_by_Office_Account']=Expense_by_Office_Account
  context['Total_cost']=x
  context["user"]=user_class.objects.all()
  context['Total_sell']=sum([i.sold_price for i in sold_data.objects.all()])
  d=context['Total_sell']-context['Total_cost']
  context['dif']=d
  context['office_balane']=context['Total_sell']-context['Expense_by_Office_Account']
  return render(request,'office_account.html',context)
  
  

      

