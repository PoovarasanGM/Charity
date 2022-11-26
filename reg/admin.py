from django.contrib import admin
from .models import *


class DetailsAdmin(admin.ModelAdmin):
    list_display= ('name','date','egg','eggquantity','eggprice','food','foodquantity','foodprice','dress','dressquantity','dressprice','stationary','stationaryquantity','stationaryprice','bedsheets','bedsheetsquantity','bedsheetsprice',)
    list_filter = ('date',)
    list_per_page = 5
    list_max_show_all = 50

class EventAdmin(admin.ModelAdmin):
    list_display = ('date','home','price','code','complete')
    list_filter = ('date',)
    search_fields = ('date',)
    list_per_page = 7
    list_max_show_all = 50

admin.site.register(Details,DetailsAdmin)
admin.site.register(Image)
admin.site.register(Event,EventAdmin)
