from django import forms
from .models import user_class
from .models import sold_data
from datetime import date




class User_Class(forms.Form):
    name=forms.CharField(max_length=50,)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)

class Office_expense(forms.Form):
   
    expense=forms.CharField(max_length=50)
    cost=forms.FloatField()
    date=forms.DateField(widget=forms.SelectDateWidget(),initial=date.today)

class Product_cost(forms.Form):
    
    products=forms.CharField(max_length=50)
    measurements=forms.FloatField()
    measurements_type=forms.ChoiceField(choices =[
        ('Kg','KG'),
        ('Liter','LTR'),
        ('Hali','HALI'),
        ('Dozen','DOZEN'),
    ],  initial='KG', widget=forms.Select(), required=True)
    cost_per_measurement=forms.FloatField()
    date=forms.DateField(widget=forms.SelectDateWidget(),initial=date.today)

class Sold_data(forms.ModelForm):
    transaction_id=forms.CharField(max_length=50,required=False)
    sold_date=forms.DateField(widget=forms.SelectDateWidget(),initial=date.today)
    measurements_type=forms.ChoiceField(choices =[
        ('Kg','KG'),
        ('Liter','LTR'),
        ('Hali','HALI'),
        ('Dozen','DOZEN'),
    ],  initial='KG', widget=forms.Select(), required=True)
    class Meta:
        model=sold_data
        fields = ['sold_products','how_many', 'measurements_type','sold_price','transaction_id','sold_date']
