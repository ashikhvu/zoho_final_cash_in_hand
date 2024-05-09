from django.contrib import admin
from .models import Bill,Expense,PurchaseOrder,RetainerInvoice,payment_made,Payment_details,Payment_recieved
# Register your models here.

admin.site.register(Bill)
admin.site.register(Expense)
admin.site.register(PurchaseOrder)
admin.site.register(RetainerInvoice)
admin.site.register(payment_made)
admin.site.register(Payment_details)
admin.site.register(Payment_recieved)