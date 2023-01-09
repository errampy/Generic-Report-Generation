from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=20)
    email_address=models.EmailField(max_length=100)
    address=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
class Agent(models.Model):
    agent_name=models.CharField(max_length=40)
    ROLE=(('Manager','Manager'),('TeamLeader','TeamLeader'),('SeniorAgent','SeniorAgent'),('JuniorAgent','JuniorAgent'))
    role=models.CharField(max_length=40,choices=ROLE,default='JuniorAgent')
    email_address=models.EmailField(max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
class TableMaster(models.Model):
    table_name=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return str(self.table_name)
class ReportMaster(models.Model):
    report_name=models.CharField(max_length=100)
    table_name=models.ForeignKey(TableMaster,on_delete=models.CASCADE,related_name='tn')
    pre_report_function_name=models.CharField(max_length=100)
    report_generated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_id',editable=False)
    extra_detail=models.TextField(editable=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

class TableColumnDetail(models.Model):
    table_name=models.ForeignKey(TableMaster,on_delete=models.CASCADE,related_name='table_n')
    table_column_name=models.CharField(max_length=50)

    def __str__(self):
        return str(self.table_column_name)