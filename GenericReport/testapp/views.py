from django.shortcuts import render , redirect
# import os
# from django.contrib.staticfiles import finders
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from testapp.models import *
from testapp.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime
from django.contrib import messages
from django.core.serializers import serialize
# from django.forms import formset_factory
# Create your views here.
class CustomerListView(ListView):
    model=Customer
    template_name='testapp/customer.html'

def customer_render_pdf_view(request,*args,**kwargs):
    pass
def home(request):
    template_name='testapp/home.html'
    return render(request,template_name)
def render_pdf_view(request):
    if not request.user.is_authenticated:
        
        return redirect('login_view')
    else:
        user_id=request.user.id
        first_name=request.user.first_name
        last_name=request.user.last_name
        email_address=request.user.email
        login_at=request.user.last_login
        report_generated_at=datetime.today()
        records=Customer.objects.all()
        template_path = 'testapp/user_printer.html'
        context = {
            'user_id':user_id,'first_name':first_name,'last_name':last_name,'email_address':email_address,'login_at':login_at,
            'msg': 'This is our template block','report_generated_at':report_generated_at,
            'title':'Customer PDF',
            'records':records,
        }
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        #if download :
        #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        # if disable :
        response['Content-Disposition'] = 'filename="report.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        #, link_callback=link_callback
        pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
def report_master(request):
    if not request.user.is_authenticated:
        
        return redirect('login_view')
    else:
        form=ReportMasterForm()
        extra_form=ExtraDetailForm()
        if request.method == 'POST':
            form=ReportMasterForm(data=request.POST)
            if form.is_valid():
                #list_display = ['id','report_name','table_name','pre_report_function_name','report_generated_by','extra_detail','create_at']
                report_name=form.cleaned_data['report_name']
                table_name=form.cleaned_data['table_name']
                column_position=request.POST.getlist('column_position')
                body_column_name=request.POST.getlist('body_column_name')
                table_column_name=request.POST.getlist('table_column_name')
                string_function_for_report_column_name=request.POST.getlist('string_function_for_report_column_name')
                print(f'report_name {report_name} | table_name  : {table_name} | column_position : {column_position}')
                print(f'body_column__name : {body_column_name} | table_column_name : {table_column_name}')
                print(f'string_function_for_report_column_name : {string_function_for_report_column_name}')
                if str(table_name) == 'Customer':
                    print('This is customer')
                    column_list = ['id','name','mobile_no','email_address','address','create_at','update_at']
                    check = all(item in column_list for item in table_column_name)
                    records=Customer.objects.values()
                elif str(table_name) == 'Agent':
                    print('This is agent')
                    column_list = ['id','agent_name','role','email_address','create_at']
                    check = all(item in column_list for item in table_column_name)
                    print('Table ')
                    records=Agent.objects.values()
                '''
                here need to defined all table like line no. 90 to 95 how coded...
                '''
                if check is True:
                    print('Records ',records)
                    for data in records:
                        for key in table_column_name:
                            print('data',data[key])
                    user_id=request.user.id
                    first_name=request.user.first_name
                    last_name=request.user.last_name
                    email_address=request.user.email
                    login_at=request.user.last_login
                    report_generated_at=datetime.today()
                    template_path = 'testapp/pdf.html'
                    context = {
                        'user_id':user_id,'first_name':first_name,'last_name':last_name,'email_address':email_address,'login_at':login_at,
                        'msg': 'This is our template block','report_generated_at':report_generated_at,
                        'title':'Customer PDF',
                        'records':list(records),
                        'body_column_name':body_column_name,
                        'table_column_name':table_column_name,
                        'report_name':report_name,
                    }
                    # Create a Django response object, and specify content_type as pdf
                    response = HttpResponse(content_type='application/pdf')
                    #if download :
                    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
                    # if disable :
                    response['Content-Disposition'] = 'filename="report.pdf"'
                    # find the template and render it.
                    template = get_template(template_path)
                    html = template.render(context)

                    # create a pdf
                    #, link_callback=link_callback
                    pisa_status = pisa.CreatePDF(
                    html, dest=response)
                    # if error then show some funny view
                    if pisa_status.err:
                        return HttpResponse('We had some errors <pre>' + html + '</pre>')
                    return response

                else:
                    messages.error(request,'Unmatched Fields...!!!')
                    return redirect('report_master')            
            else:
                print('form error ',form.errors)

        context={
            'form':form,'extra_form':extra_form,
        }
        template_name='testapp/report_master.html'
        return render(request,template_name,context)
def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            un=form.cleaned_data['username']
            pwd=form.cleaned_data['password']
            user=authenticate(username=un,password=pwd)
            if user is not None:
                login(request=request,user=user)
                return redirect('home')
        else:
            print('form.error ',form.errors)
            context={
            'form':form,
            }
            template_name='testapp/login.html'
            return render(request,template_name,context)

    context={
        'form':form,
    }
    template_name='testapp/login.html'
    return render(request,template_name,context)

def logout_view(request):
    logout(request)
    return redirect('home')

    