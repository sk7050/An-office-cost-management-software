from django.db import models




# Create your models here.
class user_class(models.Model):
  name=models.CharField(max_length=50)
  email=models.EmailField()
  password=models.CharField(max_length=50)
  
  
  def __str__(self):
    return self.name

class office_expense(models.Model):
    name_id=models.ForeignKey(user_class, on_delete=models.CASCADE)
    expense=models.CharField(max_length=50)
    cost=models.FloatField()
    date=models.DateField(auto_now_add=False)
    


    def __str__(self):
        return self.expense


class product_cost(models.Model):
    name_id=models.ForeignKey(user_class, on_delete=models.CASCADE,related_name='name_id')
    products=models.CharField(max_length=50)
    measurements=models.FloatField()
    measurements_type=models.CharField(max_length=6)
    cost=models.FloatField()
    date=models.DateField(auto_now_add=False)
    


    def __str__(self):
        return self.products