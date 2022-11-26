from django import forms  
from django.forms.widgets import NumberInput 
from reg.models import *
  
HOME = (('MotherTeresa','MotherTeresa'),('AnnaiTeresa','AnnaiTeresa'),('BlindSchool','BlindSchool'),('Henry','Henry'),('DonBoscoAnbuIllam','DonBoscoAnbuIllam'))
#CATEGORY = (('Egg','Egg'),('Food','Food'),('BedSheets','BedSheets'),('Stationary','Stationary'),('Dress','Dress'))



class RegForm(forms.ModelForm):  
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placefolder':'Enter Your Name '}))
    mobile=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placefolder':'Enter Your Mobile Number '}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placefolder':'Enter Your Email '}))
    events=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placefolder':'Enter For Example: Birthday, Festival, Wedding, etc.,'}))
    address=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placefolder':'Enter Your Address '}))
    pincode=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placefolder':'Enter Your Pincode '}))
    date = forms.DateField(widget = NumberInput(attrs={'type':'date','class':'form-control',}))  
    egg = forms.MultipleChoiceField(choices=HOME,widget=forms.CheckboxSelectMultiple,required=False)
  
    food = forms.MultipleChoiceField(choices=HOME,widget=forms.CheckboxSelectMultiple,required=False)
   
    stationary = forms.MultipleChoiceField(choices=HOME,widget=forms.CheckboxSelectMultiple,required=False)
  
    dress = forms.MultipleChoiceField(choices=HOME,widget=forms.CheckboxSelectMultiple,required=False)
  
    bedsheets = forms.MultipleChoiceField(choices=HOME,widget=forms.CheckboxSelectMultiple,required=False)
   # category = forms.MultipleChoiceField(choices=CATEGORY,widget=forms.CheckboxSelectMultiple)
    eggquantity=forms.CharField(required=False,widget=forms.NumberInput(attrs={'class':'form-control','id':'quantity','placefolder':'Enter The Count Of Egg'}))
    eggprice=forms.CharField(required=False,widget=forms.NumberInput(attrs={'class':'form-control','id':'price','placefolder':'Enter The Total Price'}))
    foodquantity=forms.CharField(required=False,widget=forms.NumberInput(attrs={'class':'form-control','id':'quantity','placefolder':'Enter The Number Of Kg'}))
    foodprice=forms.CharField(required=False,widget=forms.NumberInput(attrs={'class':'form-control','id':'price','placefolder':'Enter The Total Price'}))
    stationaryquantity=forms.CharField(required=False,widget=forms.NumberInput(attrs={'class':'form-control','id':'quantity','placefolder':'Enter The Stationary Name'}))
    stationaryprice=forms.CharField(required=False,widget=forms.NumberInput(attrs={'class':'form-control','id':'price','placefolder':'Enter The Total Price'}))
    dressquantity=forms.CharField(required=False,widget=forms.NumberInput(attrs={'class':'form-control','id':'quantity','placefolder':'Enter The Count Of Dress'}))
    dressprice=forms.CharField(required=False,widget=forms.NumberInput(attrs={'class':'form-control','id':'price','placefolder':'Enter The Total Price'}))
    bedsheetsquantity=forms.CharField(required=False,widget=forms.NumberInput(attrs={'class':'form-control','id':'quantity','placefolder':'Enter The Count Of Bedsheets'}))
    bedsheetsprice=forms.CharField(required=False,widget=forms.NumberInput(attrs={'class':'form-control','id':'price','placefolder':'Enter The Total Price'}))


    class Meta:  
        model = Details  
        fields = "__all__"  
