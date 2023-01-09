from django.urls import path
from testapp import views
urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login_view , name='login_view'),
    path('logout/',views.logout_view,name='logout_view'),
    path('report_master',views.report_master,name='report_master'),
    path('render-to-pdf/',views.render_pdf_view, name='render_pdf'),
    path('list-view',views.CustomerListView.as_view(),name='cunser_list_view'),
]