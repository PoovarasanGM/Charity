from django.db import models
from multiselectfield import MultiSelectField
import random

def code(request):
#     upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     lower = 'abcdefghijklmnopqrstuvwxyz'
#     symbols = '!@#$%^&*?'
    numbers = '0123456789'
    string = numbers
    length = 8
    coupon = ''.join(random.sample(string,length))
    print(coupon)



HOME = (('MotherTeresa','MotherTeresa'),('AnnaiTeresa','AnnaiTeresa'),('BlindSchool','BlindSchool'),('Henry','Henry'),('DonBoscoAnbuIllam','DonBoscoAnbuIllam'))
CATEGORY = (('Egg','Egg'),('Food','Food'),('BedSheets','BedSheets'),('Stationary','Stationary'),('Dress','Dress'))

class Details(models.Model):
    name = models.CharField(max_length = 200,null=False)
    mobile = models.CharField(max_length = 200,null=True)
    email = models.EmailField(max_length = 200,null=True)
    date = models.DateField(auto_now = False,null=True,auto_now_add=False)
    image = models.ImageField(upload_to="images/",null=True,blank=True)
    events = models.CharField(max_length = 200,null=True,blank = False)
    egg = MultiSelectField(choices=HOME,max_length=200,null=True,default='0000000')
    food = MultiSelectField(choices=HOME,max_length=200,null=True,default='none')
    stationary = MultiSelectField(choices=HOME,max_length=200,null=True,default='none')
    dress = MultiSelectField(choices=HOME,max_length=200,null=True,default='none')
    bedsheets = MultiSelectField(choices=HOME,max_length=200,null=True,default='none')
    address = models.CharField(max_length = 200,null=True,blank = False)
    pincode = models.PositiveIntegerField(null=True,blank = False)

    eggquantity = models.CharField(max_length=20,null=True,blank=True,default='none')
    eggprice = models.CharField(max_length = 200,null=True,blank=True,default='none')
    foodquantity = models.CharField(max_length=20,null=True,blank=True,default='none')
    foodprice = models.CharField(max_length = 200,null=True,blank=True,default='none')
    stationaryquantity = models.CharField(max_length=20,null=True,blank=True,default='none')
    stationaryprice = models.CharField(max_length = 200,null=True,blank=True,default='none')
    dressquantity = models.CharField(max_length=20,null=True,blank=True,default='none')
    dressprice = models.CharField(max_length = 200,null=True,blank=True,default='none')
    bedsheetsquantity = models.CharField(max_length=20,null=True,blank=True,default='none')
    bedsheetsprice = models.CharField(max_length = 200,null=True,blank=True,default='none')




class Image(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="images/gallery",null=True)
    def __str__(self):
        return self.title


class Event(models.Model):
    date = models.DateField(auto_now = False,auto_now_add=False)
    home = models.CharField(max_length = 200,null=True,)
    event = models.CharField(max_length = 200,null=True)
    code = models.CharField(max_length = 200,null=True)
    price = models.CharField(max_length = 200,null=True)
    complete = models.BooleanField(default = False)
    def __str__(self):
        return self.home