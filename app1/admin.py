from django.contrib import admin
from app1.models import *

# Register your models here.

@admin.register(purchase_model)
class purchase_admin(admin.ModelAdmin):
    list_display = ('id','comp','itm','name','qnt','brate','bvalue','addcost','totalvalue')

@admin.register(sale_model)
class sale_admin(admin.ModelAdmin):
    list_display = ('id','comp','itm','name','qnt','brate','bvalue','addcost','totalvalue')

@admin.register(analysis_view)
class analysis_admin(admin.ModelAdmin):
    list_display = ('id','comp','particular','iquantity','ieff_rate','ivalue','oquantity','oeff_rate','ovalue')

# noufal

@admin.register(groupanalysismodel)
class grpanalisysadmin(admin.ModelAdmin):
    list_display = ('id','comp','pert','perticular','pquatity','prate','pvalue','squatity','srate','svalue')

@admin.register(salevouchermodel)
class salevoucheradmin(admin.ModelAdmin):
    list_display = ('id','comp','stockitem','udergroup','date','name','quantity','basicrate','basicvalue','addlcost','totalvalue','efsrate')

@admin.register(purchasevouchermodel)
class purchasevoucheradmin(admin.ModelAdmin):
    list_display = ('id','comp','stockitem','udergroup','date','name','quantity','basicrate','basicvalue','addlcost','totalvalue','efsrate')

@admin.register(countrymodel)
class countryadmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(statemodel)
class stateadmin(admin.ModelAdmin):
    list_display = ('id','cname','sname')

@admin.register(ledgeranalysismodel)
class ledgeranalisysadmin(admin.ModelAdmin):
    list_display = ('id','lpert','lperticular','lpquatity','lprate','lpvalue','lsquatity','lsrate','svalue')

@admin.register(purchaseledgervouchermodel)
class purchaseledgervoucheradmin(admin.ModelAdmin):
    list_display = ('id','lstockitem','ludergroup','ldate','lname','lquantity','lbasicrate','lbasicvalue','laddlcost','ltotalvalue','lefsrate')

@admin.register(salesledgervouchermodel)
class salesledgervoucheradmin(admin.ModelAdmin):
    list_display = ('id','lstockitem','ludergroup','ldate','lname','lquantity','lbasicrate','lbasicvalue','laddlcost','ltotalvalue','lefsrate')

admin.site.register(Sales)
admin.site.register(Purchase)
admin.site.register(Journal)
admin.site.register(creditreg)
admin.site.register(debitnote)



# ananthakrishnan

admin.site.register(Companies)


admin.site.register(tally_group)

admin.site.register(Account_Books_Group_under)

admin.site.register(Account_Books_Ledger)




admin.site.register(tally_ledger)


admin.site.register(Account_books_Ledger_Voucher)



admin.site.register(cash_bank_books_Group_Under_closing_balance)

admin.site.register(Months)


admin.site.register(cash_bank_books_Leger_Month_closing)

admin.site.register(cash_bank_books_TotalClosing_balance)

'''----------voucher summary ----------'''

@admin.register(First_Voucher_Summary_Model)
class FirstVoucherSummary_Admin(admin.ModelAdmin):
    list_display = ('id','Voucher_Name','Particular','Debit','Credit')

@admin.register(Second_Voucher_Summary_Model)
class SecondVoucherSummary_Admin(admin.ModelAdmin):
    list_display = ('id','FVoucher_Name','Particular','Debit','Credit')

@admin.register(Stock_Group_Summary_Model)
class StockVoucherSummary_Admin(admin.ModelAdmin):
    list_display = ('id','Stock_Voucher_Forgn','Particular','Quantity','Rate','Value')

@admin.register(Product_Stock_Group_Summary_Model)
class ProVoucherSummary_Admin(admin.ModelAdmin):
    list_display=('id','PStock_Voucher_Forgn','Particular','Quantity','Rate','Value')

@admin.register(Stock_Item_Monthly_Summary_Model)
class StockItemMontlySummary_Admin(admin.ModelAdmin):
    list_display=('id','Pro_Stock_Voucher_Forgn','Open_Balance_Qty','Open_Balance_Value','Particular','Inwards_Qty',"Inwards_Vlu",'Outwards_Qty','Outwards_Vlu','Closing_Bal_Qty','Closing_Bal_Vlu')

@admin.register(Stock_Item_Voucher_Model)
class Stock_Item_Voucher_Admin(admin.ModelAdmin):
    list_display=('id','Pro_Stock_Forgn','Date','Particular','Voucher_Type','Vch_No','Inwards_Qty','Inwards_Vlu','Outwards_Qty','Outwards_Vlu')

@admin.register(Group_Voucher_Model)
class GroupVoucher_Admin(admin.ModelAdmin):
    list_display=('id','Date','Particular','Vch_Type','Vch_No',"DEBIT",'Credit','Open_Balance')

@admin.register(First_Group_Summary_Model)
class FirstGroupSummary_Admin(admin.ModelAdmin):
    list_display = ('id','Group_Name','Particular','Debit','Credit')

@admin.register(Second_Group_Summary_Model)
class SecondGroupSummary_Admin(admin.ModelAdmin):
    list_display=('id','Fgroup_Forng','CName')

@admin.register(Third_Group_Summary_Model)
class ThirdGroupSummary_Admin(admin.ModelAdmin):
    list_display=('id','Sgroup_Forng','PName')

@admin.register(Ledger_Monthly_Summary_Model)
class LedgerMonthlySummary_Admin(admin.ModelAdmin):
    list_display=('id','Tgroup_Forgn','Open_Balance','Particular','Dedit','Credit','Closing_Balance')

@admin.register(Ledger_Voucher_Model)
class LedgerVoucher_Admin(admin.ModelAdmin):
    list_display=('id','Particular','Date','Vch_Type','Vch_No','Debit','Credit','Open_Balance')
    
@admin.register(journal_voucher)
class journal_voucher_Admin(admin.ModelAdmin):
    list_display=('company','voucher','jid','jname','date','debit','credit','narration')
    
@admin.register(journal_particulars)
class journal_particulars_Admin(admin.ModelAdmin):
    list_display=('j_voucher','particular_id','particular','debit','credit')