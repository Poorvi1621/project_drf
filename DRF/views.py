from django.shortcuts import render
from .models import detailsForm
from .serializers import detailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class DetailsTable(APIView):
    

    def get(self,request):
        detailobj=detailsForm.objects.all()
        dlserializeobj=detailSerializer(detailobj,many=True)
        return Response(dlserializeobj.data)

    def post(self,request):
        serializeobj=detailSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        
        return Response(serializeobj.errors)



class DetailsUpdate(APIView):
    def put(self,request,pk):
        try:
          detailobj=detailsForm.objects.get(pk=pk)
        except:
            return ("Not found in database")    
            
        serializeobj=detailSerializer(detailobj,data=request.data)    
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        
        return Response(serializeobj.errors)

    def delete(self,request,pk):
        try:
          detailobj=detailsForm.objects.get(pk=pk)
        except:
            return ("Not found in database")    
        detailobj.delete()
        return Response(200)


def home(request):
    data=detailsForm.objects.all()
    return render(request,'index.html',{'data':data})


def addemp(request):
    name=request.POST['Name']
    age=request.POST['Age']
    age=int(age)
    gender=request.POST['Gender']
    country=request.POST['Country']
    e=detailsForm()
    e.Name=name
    e.Age=age
    e.Gender=gender
    e.Country=country
    e.save()
    data=detailsForm.objects.all()
    return render(request,'index.html',{'data':data})


def delt(request):
    eid=request.GET['eid']
    detailsForm.objects.get(id=eid).delete()
    data=detailsForm.objects.all()
    return render(request,'index.html',{'data':data})

def update(request):
    e=detailsForm()
    e.id=request.POST['eid']
    e.Name=request.POST['Name']
    e.Age=request.POST['Age']
    e.Gender=request.POST['Gender']
    e.Country=request.POST['Country']
    e.save()
    data=detailsForm.objects.all()
    return render(request,'index.html',{'data':data})
    