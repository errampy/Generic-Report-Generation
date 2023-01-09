from django import forms
from testapp.models import *

class ReportMasterForm(forms.ModelForm):
    class Meta:
        model = ReportMaster
        fields = '__all__'
class ExtraDetailForm(forms.Form):
    table_column = TableColumnDetail.objects.all().values_list('table_column_name', 'table_column_name')

    
    NUMERIC_FIELDS=(('','--------'),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8,),(9,9),(10,10))
    column_position=forms.ChoiceField(choices=NUMERIC_FIELDS)
    table_column_name = forms.CharField(widget=forms.Select(choices=table_column, attrs={'class': 'form-control'}))
    body_column_name=forms.CharField()
    string_function_for_report_column_name=forms.CharField()