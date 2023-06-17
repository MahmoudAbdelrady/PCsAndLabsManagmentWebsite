from django.shortcuts import redirect, render
from django.contrib import messages
from pyparsing import empty
from .models import AddLab,ReportInfo,AddNewPC
import json
from django.http import JsonResponse
from django.utils import timezone
def PHome(request):
    return render(request,'pages/first_page.html')

def LabH(request):
    return render(request,'pages/LaboratoryTrackingWebsite.html')

def PcsList(request):
    return render(request,'pages/PcsList.html' , {'ReportInfo':ReportInfo.objects.all()})




def ListLab(request):
    return render(request,'pages/list_lab.html' , {'LabI':AddLab.objects.all()})

def search_Labs(request):
    if request.method == 'POST':
        search_str=json.loads(request.body).get('searchText')
    labs=AddLab.objects.filter(Laboratory_Name__istartswith=search_str)
    data = labs.values()
    return JsonResponse(list(data),safe=False)

def EditL(request,Lab_ID):
    UpdateObj = AddLab.objects.get(Laboratory_ID = Lab_ID)
    context = {
        'UpdateObj':UpdateObj,
    }
    return render(request,'pages/edit_labs.html',context)

def EditLa(request,Lab_ID):
    if request.method=='POST':
        UpdateLName = request.POST.get('name')
        UpdateLNum = request.POST.get('number')
        UpdateFNum = request.POST.get('floor_no')
        UpdatePCsNum = request.POST.get('PCs_no')
        UpdateCap = request.POST.get('capacity')
        UpdateChNum = request.POST.get('chair_no')
        UpdateSt = request.POST.get('Status')
        UObj = AddLab.objects.get(Laboratory_ID = Lab_ID)
        UObj.Laboratory_Name = UpdateLName
        UObj.Laboratory_Number = UpdateLNum
        UObj.Floor_Number = UpdateFNum
        UObj.NumOfPcs = UpdatePCsNum
        UObj.LabCapacity = UpdateCap
        UObj.NumOfChairs = UpdateChNum
        UObj.LabStatus = UpdateSt
        UObj.save()
        messages.info(request,"Edited lab information successfully")
        return redirect('/EditLabs')
    return render(request,'pages/edit_labs.html')

def delete(request,LID):
    obj = AddLab.objects.filter(Laboratory_ID = LID)
    obj.delete()
    return redirect('/ListLab')

def EditPcs(request):
    if request.method=='POST':
        EPC_ID = request.POST.get('Eid')
        ELab_ID = request.POST.get('Elab_id')
        EPC_Status = request.POST.get('Estatus')
        if AddNewPC.objects.filter(PC_ID = EPC_ID).exists() and AddNewPC.objects.filter(Lab_ID = ELab_ID).exists():
            ANPObj = AddNewPC.objects.get(Lab_ID = ELab_ID)
            ANPObj.PCStatus = EPC_Status
            ANPObj.save()
            messages.info(request,"Edited Pc status successfully")
            return redirect('/EditPcs')
        else:
            messages.info(request,"Pc or lab does not exist")
            return redirect('/EditPcs')
    return render(request,'pages/edit_pcs.html')

def EditLabs(request):
    if request.method=='POST':
        ELabID = request.POST.get('id')
        EditLabName = request.POST.get('name')
        EditBuildNum = request.POST.get('number')
        EditLabFloorNum = request.POST.get('floor_no')
        EditLabNumofPcs = request.POST.get('PCs_no')
        EditLabCap = request.POST.get('capacity')
        EditLabChairNum = request.POST.get('chair_no')
        EditLabStatus = request.POST.get('Status')
        if AddLab.objects.filter(Laboratory_ID = ELabID).exists():
            ALObj = AddLab.objects.get(Laboratory_ID = ELabID)
            ALObj.Laboratory_Name = EditLabName
            ALObj.Laboratory_Number = EditBuildNum
            ALObj.Floor_Number = EditLabFloorNum
            ALObj.NumOfPcs = EditLabNumofPcs
            ALObj.LabCapacity = EditLabCap
            ALObj.NumOfChairs = EditLabChairNum
            ALObj.LabStatus = EditLabStatus
            ALObj.save()
            messages.info(request,"Edited lab information successfully")
            return redirect('/EditLabs')
        else:
            messages.info(request,"This Lab does not exist")
            return redirect('/EditLabs')
    return render(request,'pages/edit_labs.html')

def AddL(request):
    if request.method=='POST':
        NewLabID = request.POST.get('NewLabID')
        NewLabName = request.POST.get('NewLabName')
        NewLabNum = request.POST.get('NewLabNum')
        NewLabFloorNum = request.POST.get('NewLabFloorNum')
        NewLabNumofPcs = request.POST.get('NewLabNumofPcs')
        NewLabCap = request.POST.get('NewLabCap')
        NewLabChairNum = request.POST.get('NewLabChairNum')
        NewLabStatus = request.POST.get('raf')
        LabInfo = AddLab(Laboratory_ID = NewLabID,Laboratory_Name = NewLabName,Laboratory_Number = NewLabNum, Floor_Number = NewLabFloorNum,NumOfPcs = NewLabNumofPcs,LabCapacity = NewLabCap,NumOfChairs = NewLabChairNum,LabStatus = NewLabStatus)
        LabInfo.save()
        return redirect('/AddLab')
    return render(request,'pages/new.html')

def AddP(request):
    if request.method=='POST':
        NewPC_ID = request.POST.get('PCID')
        Lab_ID = request.POST.get('LabID')
        PC_Status = request.POST.get('status')
        NewPC_Info = AddNewPC(PC_ID = NewPC_ID , Lab_ID = Lab_ID , PCStatus = PC_Status)
        NewPC_Info.save()
        return redirect('/AddPC')
    return render(request,'pages/new_html.html')

def Report(request):
    if request.method=='POST':
        LabID = request.POST.get('RepLabID')
        PCNum = request.POST.get('RepPcNum')
        ProbType = request.POST.get('Repoption')
        ProbDate = request.POST.get('RepProblemDate')
        if(ProbDate==empty):
           ProbDate=timezone.now() 
        ProbDesc = request.POST.get('RepDescription')
        ProblemInfo = ReportInfo(RLaboratory_ID = LabID , RPcNum = PCNum , RProblemType = ProbType , RDate = ProbDate , RDescription = ProbDesc)
        ProblemInfo.save()
        return redirect('/Report')
    return render(request,'pages/report_problem.html')
def Rep(request,RID):
    ReportObj = AddLab.objects.get(Laboratory_ID = RID)
    context = {
        'ReportObj':ReportObj,
    }
    return render(request,'pages/report_problem.html',context)
def Repo(request,RID):
    if request.method =='POST':
        Report_PCNum = request.POST.get('RepPcNum')
        Report_ProbType = request.POST.get('Repoption')
        Report_ProbDate = request.POST.get('RepProblemDate')
        Report_ProbDesc = request.POST.get('RepDescription')
        RObj = ReportInfo(RLaboratory_ID = RID , RPcNum = Report_PCNum , RProblemType = Report_ProbType , RDate = Report_ProbDate , RDescription = Report_ProbDesc)
        RObj.save()
        return redirect('/Report')
    return render(request,'pages/report_problem.html')
def Login(request):
    return render(request,'pages/login.html')

