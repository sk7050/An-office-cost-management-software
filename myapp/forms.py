from django import forms
from .models import user_class





class User_Class(forms.Form):
    name=forms.CharField(max_length=50,)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)

class Office_expense(forms.Form):
   
    expense=forms.CharField(max_length=50)
    cost=forms.FloatField()
    date=forms.DateField(widget=forms.SelectDateWidget())

class Product_cost(forms.Form):
    
    products=forms.CharField(max_length=50)
    measurements=forms.FloatField()
    measurements_type=forms.ChoiceField(choices =[
        ('kilogram','KG'),
        ('Liter','LTR'),
        ('Hali','HALI'),
        ('Dozen','DOZEN'),
    ],  initial='KG', widget=forms.Select(), required=True)
    cost=forms.FloatField()
    date=forms.DateField(widget=forms.SelectDateWidget())