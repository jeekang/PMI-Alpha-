from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.translation import gettext as _
from django.forms import ModelForm


# USE THIS TO ENABLE SCROLL DOWN SELECTION
GENDERCHOICE = (
	('M', 'Male'),
	('F', 'Female'),
	('O', 'Other'),
	)

# Generally want  models.ManyToManyField in encapsulating entity
# ie. want  models.ManyToManyField in Pizza for FK to toppings
# Can't use add(), create(), set(), use Intermediary_name(person, group, ...) 
# - RA
class Vendor(models.Model):
	def __str__(self):
   		return self.LegalName
	ZipCode = models.CharField(_("Zip code"), max_length = 10)
	TIN = models.IntegerField(_("TIN"))
	State = models.CharField(_("State"), max_length = 10)
	POC = models.CharField(_("Point of Contact"), max_length = 50)
	Phone = models.CharField(_("Phone"), max_length = 20)
	LegalName = models.CharField(_("Legal Name"), max_length = 50)
	Fax = models.CharField(_("Fax"), max_length = 50)
	Email = models.CharField(_("Email"), max_length = 50)
	DUNs = models.CharField(_("DUNs"), max_length = 50)
	DBA = models.CharField(_("DBA"), max_length = 50)
	Country = models.CharField(_("Country"), max_length = 20)
	City = models.CharField(_("City"), max_length = 20)
	CAGE = models.CharField(_("CAGE"), max_length = 50)
	Address = models.CharField(_("Address"), max_length = 50)

class Employee(models.Model):
	def __str__(self):
   		return self.FName + " " + self.MName + " " + self.LName
	VendorID = models.ManyToManyField(Vendor, through='Customer_Employee')
	FName = models.CharField(_("Resource First Name"), max_length = 20)
	MName = models.CharField(_("Resource Middle Name"), max_length = 20)
	LName = models.CharField(_("Resource Last Name"), max_length = 20)
	Gender = models.CharField(_("Gender"), max_length = 10, choices=GENDERCHOICE)
	PersonalEmail = models.CharField(_("Personal Email"), max_length = 50)
	PMIEmail = models.CharField(_("PMI Email"), max_length = 50)
	TypeOfContract = models.CharField(_("Type of Contract"), max_length = 20)
	Addresses = models.CharField(_("Addresses"), max_length = 30)
	City = models.CharField(_("City"), max_length = 20)
	ZipCode = models.CharField(_("Zip code"), max_length = 10)
	State = models.CharField(_("State"), max_length = 10)
	Country = models.CharField(_("Country"), max_length = 20)
	Phone = models.CharField(_("Phone"), max_length = 20)
	BirthDate = models.DateField(_("Birth Date"), default=datetime.date.today)
	DateOfHire = models.DateField(_("Date of Hire"), default=datetime.date.today)
	PMICareerTitle = models.CharField(_("PMI Career Title    "), max_length = 50)
	ResourceType= models.CharField(_("Resource Type"), max_length = 20)
	GSALaborCategory = models.CharField(_("GSA Labor Category"), max_length=20)
	VacationHour = models.CharField(_("Vacation Hour"), max_length = 20)
	SickLeaveHour = models.CharField(_("Sick Leave Hour"), max_length = 20)
	EmployementStatus = models.CharField(_("Employment Status"), max_length = 50)
	ContractLaborCategory = models.CharField(_("Contract Labor Category"), max_length = 20)
	RecruitmentSource = models.CharField(_("Recruitment Source"), max_length = 50)
	ResponsibleRecruiter = models.CharField(_("Responsible Recruiter"), max_length = 50)
	HUBzone = models.BooleanField(_("HUBzone"), default = True)
	ProbationaryEnd= models.DateField(_("Probationary End"), default=datetime.date.today)
	TerminationDate = models.DateField(_("Termination Date"), default=datetime.date.today)
	Department = models.CharField(_("Department"), max_length = 50)
	WorkLocation = models.CharField(_("Work Location"), max_length = 50)
	Billable = models.BooleanField(_("Billable"), default = True)
	SalaryType = models.CharField(_("Salary Type"), max_length = 20)
	Salary = models.IntegerField(_("Salary"))
	ClearanceStatus = models.CharField(_("Clearance Status"), max_length = 20)
	ClearedDate = models.DateField(_("Cleared Date"), default=datetime.date.today)
	ClearedType = models.CharField(_("Cleared Type"), max_length = 20)
	Rehire = models.BooleanField(_("Rehire (T/F)"), default = True)
	_401KEligible = models.BooleanField(_("401K Eligible"), default = True)
	OrientationDate = models.DateField(_("Orientation Date"), default=datetime.date.today)
	ClientBillRate = models.CharField(_("Client Bill Rate"), max_length = 20)
	GSA_vehicle = models.CharField(_("GSA Vehicle"), max_length = 50)
	GSA_rate = models.CharField(_("GSA Rate"), max_length = 50)
	CAMPINSent = models.CharField(_("CAMPINSent"), max_length = 50)
	PaycomLogin = models.CharField(_("Paycom Login"), max_length = 50)
	eFAACT = models.CharField(_("eFAACT"), max_length=50)
	Computer = models.CharField(_("Computer"), max_length=50)
	BusinessCard = models.CharField(_("Business Card"), max_length=50)

class GoogleGroup(models.Model):
	def __str__(self):
   		return self.Name
	Name = models.CharField(_("Name"), max_length = 50)
	Admin = models.CharField(_("Admin"), max_length = 50)

class Customer(models.Model):
	def __str__(self):
   		return self.LegalName
	LegalName = models.CharField(_("Legal Name"), max_length = 50)
	DBA = models.CharField(_("DBA"), max_length = 50)
	Address = models.CharField(_("Address"), max_length = 50)
	City = models.CharField(_("City"), max_length = 20)
	ZipCode = models.CharField(_("Zip code"), max_length = 10)
	State = models.CharField(_("State"), max_length = 10)
	Country = models.CharField(_("Country"), max_length = 20)
	Phone = models.CharField(_("Phone"), max_length = 20)
	LegalName = models.CharField(_("Legal Name"), max_length = 50)
	Fax = models.CharField(_("Fax"), max_length = 50)
	Email = models.CharField(_("Email"), max_length = 50)
	DUNs = models.CharField(_("DUNs"), max_length = 9)
	CAGE = models.CharField(_("CAGE"), max_length = 50)
	POC = models.CharField(_("Point of Contact"), max_length = 50)
	TIN = models.CharField(_("TIN"), max_length=11)

class Contract(models.Model):
	def __str__(self):
   		return self.ContractNumber
	CustomerID = models.ManyToManyField(Customer, through='Department')
	IssuingCompany = models.CharField(_("Issuing Company"), max_length = 50)
	ContractNumber = models.CharField(_("Contract Number"), max_length = 50)
	DocumentLocation = models.CharField(_("Document Location"), max_length = 50)
	OrganizationType = models.CharField(_("Organization Type"), max_length = 50)
	POC = models.CharField(_("Point of Contact"), max_length = 50)
	EffectiveDate = models.DateField(_("Effective Date"), default=datetime.date.today)
	EndDate = models.DateField(_("End Date"), default=datetime.date.today)
	StartDate = models.DateField(_("Start Date"), default=datetime.date.today)
	Status = models.CharField(_("Status"), max_length = 50)
	Comments = models.CharField(_("Status"), max_length = 1000)

class Partner(models.Model):
	def __str__(self):
   		return self.LegalName
	Address = models.CharField(_("Address"), max_length = 50)
	CAGE = models.CharField(_("CAGE"), max_length = 50)
	City = models.CharField(_("City"), max_length = 20)
	ZipCode = models.CharField(_("Zip code"), max_length = 10)
	State = models.CharField(_("State"), max_length = 10)
	Country = models.CharField(_("Country"), max_length = 20)
	Phone = models.CharField(_("Phone"), max_length = 20)
	LegalName = models.CharField(_("Legal Name"), max_length = 50)
	Fax = models.CharField(_("Fax"), max_length = 50)
	Email = models.CharField(_("Email"), max_length = 50)
	DBA = models.CharField(_("DBA"), max_length = 50)
	DUNs = models.CharField(_("DUNs"), max_length = 9)
	POC = models.CharField(_("Point of Contact"), max_length = 50)
	TIN = models.CharField(_("TIN"), max_length=11)
	Type = models.CharField(_("Type"), max_length=20)

# INTERMEDIARY TABLES
# I'm pretty sure we want on_delete=models.CASCADE when deleting from intermediary tables - RA
# deletes all references to deleted object - RA

class Department(models.Model):
	def __str__(self):
   		return self.Name
	ContractID = models.ForeignKey(Contract)
	CustomerID = models.ForeignKey(Customer)
	Name = models.CharField(_("Name"), max_length = 50)
	Location = models.CharField(_("Location"), max_length = 50)
	Fax = models.CharField(_("Fax"), max_length = 50)
	Supervisor = models.CharField(_("Supervisor"), max_length = 50)
	Phone = models.CharField(_("Phone"), max_length = 50)


class Department_Employee(models.Model):
	DepartmentID = models.ForeignKey(Department,  on_delete=models.CASCADE)
	ContractID = models.ManyToManyField(Contract, through='Department',  on_delete=models.CASCADE)
	CustomerID = models.ManyToManyField(Customer, through='Department',  on_delete=models.CASCADE)
	EmployeeID = models.ManyToManyField(Employee, through='Customer_Employee',  on_delete=models.CASCADE)
	VendorID = models.ManyToManyField(Vendor, through='Customer_Employee',  on_delete=models.CASCADE)
class Contract_Employee(models.Model):
	ContractID = models.ForeignKey(Contract,  on_delete=models.CASCADE)
	CustomerID = models.ManyToManyField(Customer, through='Department',  on_delete=models.CASCADE)
	EmployeeID = models.ManyToManyField(Employee, through='Customer_Employee',  on_delete=models.CASCADE)
	VendorID = models.ManyToManyField(Vendor, through='Customer_Employee',  on_delete=models.CASCADE)

class Customer_Vendor(models.Model):
	CustomerID = models.ForeignKey(Customer,  on_delete=models.CASCADE)
	VendorID = models.ForeignKey(Vendor,  on_delete=models.CASCADE)

class Customer_Employee(models.Model):
	CustomerID = models.ForeignKey(Customer,  on_delete=models.CASCADE)
	EmployeeID = models.ForeignKey(Employee,  on_delete=models.CASCADE)
	VendorID = models.ForeignKey(Vendor,  on_delete=models.CASCADE)

class Customer_Partner(models.Model):
	CustomerID = models.ForeignKey(Customer,  on_delete=models.CASCADE)
	PartnerID = models.ForeignKey(Partner,  on_delete=models.CASCADE)

class POC(models.Model):
	PartnerID = models.ForeignKey(Partner,  on_delete=models.CASCADE)
	CustomerID = models.ManyToManyField(Customer, through='Customer_Partner',  on_delete=models.CASCADE)
	ContractID = models.ManyToManyField(Contract, through='Department',  on_delete=models.CASCADE)
	Address = models.CharField(_("Address"), max_length = 50)
	Phone = models.CharField(_("Phone"), max_length = 20)
	Email = models.CharField(_("Email"), max_length = 50)
	LName = models.CharField(_("Resource First Name"), max_length = 20)
	FName = models.CharField(_("Resource Last Name"), max_length = 20)

class Vendor_Contract(models.Model):
	CustomerID = models.ForeignKey(Customer,  on_delete=models.CASCADE)
	ContractID = models.ManyToManyField(Contract, through='Department',  on_delete=models.CASCADE)
	VendorID = models.ManyToManyField(Vendor, through='Customer_Vendor',  on_delete=models.CASCADE)


class GoogleGroup_Employee(models.Model):
	GoogleGroupID = models.ForeignKey(GoogleGroup,  on_delete=models.CASCADE)
	EmployeeID = models.ForeignKey(Employee,  on_delete=models.CASCADE)
	VendorID = models.ManyToManyField(Vendor, through='Customer_Employee',  on_delete=models.CASCADE)
