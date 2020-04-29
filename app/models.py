from django.db import models
from datetime import date
from django.conf import settings
TIME_FORMAT = '%d.%m.%Y'

class VendorsCategoryData(models.Model):
	VendorCategory_ID=models.CharField(max_length=50)
	VendorCategory_Name=models.CharField(max_length=100)
	VendorCategory_Image=models.ImageField(upload_to="vendorcategoryimages/")
	class Meta:
		db_table="VendorsCategoryData"

class VendorsData(models.Model):
	Vendor_Reg_Date=models.DateField(("Date"), default=date.today)
	Vendor_Name=models.CharField(max_length=100)
	Vendor_Category=models.CharField(max_length=100)
	Vendor_Owner=models.CharField(max_length=100)
	Vendor_Address=models.CharField(max_length=1000)
	Vendor_City=models.CharField(max_length=100)
	Vendor_State=models.CharField(max_length=100)
	Vendor_Phone=models.CharField(max_length=100)
	Vendor_Email=models.CharField(max_length=100)
	class Meta:
		db_table="VendorsData"

class UserData(models.Model):
	User_Reg_Date=models.DateField(("Date"), default=date.today)
	User_First_Name=models.CharField(max_length=100)
	User_Last_Name=models.CharField(max_length=100)
	User_Phone=models.CharField(max_length=100)
	User_Email=models.CharField(max_length=100, primary_key=True)
	User_Password=models.CharField(max_length=100)
	class Meta:
		db_table="UserData"