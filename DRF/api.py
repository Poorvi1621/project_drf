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
    
    return render(request,'index.html')