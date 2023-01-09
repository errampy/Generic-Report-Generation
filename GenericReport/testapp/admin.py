from django.contrib import admin
from testapp.models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile_no','email_address','address','create_at','update_at']
admin.site.register(Customer,CustomerAdmin)

class AgentAdmin(admin.ModelAdmin):
    list_display = ['id','agent_name','role','email_address','create_at']
admin.site.register(Agent,AgentAdmin)

class ReportMasterAdmin(admin.ModelAdmin):
    list_display = ['id','report_name','table_name','pre_report_function_name','report_generated_by','extra_detail','create_at']
admin.site.register(ReportMaster,ReportMasterAdmin)


class TableMasterAdmin(admin.ModelAdmin):
    list_display = ['id','table_name']
admin.site.register(TableMaster,TableMasterAdmin)

class TableColumnDetailAdmin(admin.ModelAdmin):
    list_display = ['id','table_name','table_column_name','table_name_id']
admin.site.register(TableColumnDetail,TableColumnDetailAdmin)

