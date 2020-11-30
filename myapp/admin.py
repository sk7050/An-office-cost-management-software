from django.contrib import admin
from .models import user_class,office_expense,product_cost,sold_data

admin.site.register(user_class)
admin.site.register(office_expense)
admin.site.register(product_cost)
admin.site.register(sold_data)
