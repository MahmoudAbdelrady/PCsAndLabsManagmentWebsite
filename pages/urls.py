from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('', views.PHome , name='PHome'),
    path('LabH',views.LabH, name='LabH'),
    path('PcsList',views.PcsList, name='PcsList'),
    path('ListLab',views.ListLab,name='ListLab'),
    path('EditPcs',views.EditPcs,name='EditPcs'),
    path('EditLabs',views.EditLabs,name='EditLabs'),
    path('DeleteLab/<int:LID>' , views.delete , name='delete'),
    path('EditLabs/<int:Lab_ID>',views.EditL,name='update'),
    path('EditLabs/Elab/<int:Lab_ID>',views.EditLa , name='updaterecord'),
    path('Report',views.Report,name='Report'),
    path('Report/<int:RID>',views.Rep , name='RP'),
    path('Report/Rep/<int:RID>',views.Repo , name='RPS'),
    path('Login',views.Login,name='Login'),
    path('AddLab',views.AddL,name='AddLab'),
    path('AddPC',views.AddP,name='AddPC'),
    path('labs/search',csrf_exempt(views.search_Labs),name='search_Labs'),
]
