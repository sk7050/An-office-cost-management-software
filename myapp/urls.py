from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.Accounts_view, name='login'),
    path('login', views.Accounts_view, name='login'),
    path('logout/', views.logout, name='logout'),
    re_path(r'^login/|login/\w+/',views.accounts_view, name='accounts'),
    #path('login',views.accounts_view, name='accounts'),
    path('office_expense_edit/<int:id>/',views.office_expense_edit_view, name='office_expense_edit'),
    path('product_purchase_edit/<int:id>',views.product_purchase_edit_view, name='product_purchase_edit'),
    
]
