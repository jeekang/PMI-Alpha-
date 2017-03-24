import django_tables2 as tables
from .models import *
from django_tables2.utils import A  # alias for Accessor

class VendorTable(tables.Table):
    class Meta:
        model = Vendor
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class EmployeeTable(tables.Table):
    VendorID = tables.LinkColumn('vendor_detail', args=[A('pk')])
    class Meta:
        model = Employee
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
    

class GoogleGroupTable(tables.Table):
    class Meta:
        model = GoogleGroup
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class CustomerTable(tables.Table):
    class Meta:
        model = Customer
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class ContractTable(tables.Table):
    class Meta:
        model = Contract
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class PartnerTable(tables.Table):
    class Meta:
        model = Partner
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class DepartmentTable(tables.Table):
    class Meta:
        model = Department
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class Department_EmployeeTable(tables.Table):
    class Meta:
        model = Department_Employee
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class Contract_EmployeeTable(tables.Table):
    class Meta:
        model = Contract_Employee
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class Customer_VendorTable(tables.Table):
    class Meta:
        model = Customer_Vendor
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class Customer_EmployeeTable(tables.Table):
    class Meta:
        model = Customer_Employee
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class Customer_PartnerTable(tables.Table):
    class Meta:
        model = Customer_Partner
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}


class POCTable(tables.Table):
    class Meta:
        model = POC
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class Vendor_ContractTable(tables.Table):
    class Meta:
        model = Vendor_Contract
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class GoogleGroup_EmployeeTable(tables.Table):
    class Meta:
        model = GoogleGroup_Employee
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

