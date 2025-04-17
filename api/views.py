from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from .modules.login import *
from .modules.imageDB import addImage
from  .modules.utility import checkReq 


# {"username":username, "password":password, "name":name, "phno":phno}

@api_view(['GET'])
def home(request):
    data={"Status": "Ok"}
    return Response(data)




class LoginAPI(APIView):
    
    
    def post(self,request):
        try:
            username,password=request.data["username"],request.data["password"]
            
        except Exception as e:
            return Response({"status":False,"error": f"required: {str(e)}"})
        
        profile,TOKEN=validateUserProfile(username,password)
      
        if profile:
            profile.pop("password",None)
            return Response({"status":True,"result":profile,"TOKEN":TOKEN})
        
        return Response({"status":False,"error": f"Invalid Credentials"})
        
 
class UserAPI(APIView):
    
    def get(self,request,*args, **kwargs):
        TOKEN = request.headers.get('TOKEN')
        
        try:
            username=request.query_params.get("username")
            if not username:
                return Response({"status":False,"error": f"required: username"})
                
        except Exception as e:
            return Response({"status":False,"error": f"required: {str(e)}"})
        
        if not TOKEN:
            return Response({"status":False,"error": f"TOKEN: Login to get data"})
        
        if not validateUserToken(username,TOKEN):
            return Response({"status":False,"error": f"TOKEN: Invalid TOKEN, Login to get data"})
            
            
        result=getUserProfile(username)
        if result:
            result.pop("password",None)
            return Response({"status":True,"result":result})
        
        return Response({"status":False,"error":f"Username not found"})
  
    def post(self,request):
        data=request.data
        try:
            username,password,name,phno=data["username"],data["password"],data["name"],int(data["phno"])
        except Exception as e:
            return Response({"status":False,"error": f"required: {str(e)}"})
        
        status,req=checkReq([username,password,name,phno])
        if not status:
            return Response(req)
        
        data={"username":username,"password":password,"name":name,"phno":phno}
        status,e=createUserProfile(data)
        if not status:
            return Response({"status":False,"error":f"Somthing Went Wrong : {e}"})
  
        return Response({"status":True})
    
    def delete(self,request):
        TOKEN = request.headers.get('TOKEN')
        
        try:
            username=request.data["username"]
        except Exception as e:
            return Response({"status":False,"error": f"required: {str(e)}"})
        
        if not TOKEN:
            return Response({"status":False,"error": f"TOKEN: Login to delete data"})
        
        if not validateUserToken(username,TOKEN):
            return Response({"status":False,"error": f"TOKEN: Invalid TOKEN, Login to delete data"})
        
        status,e=deleteUserProfile(username)
        if not status:
            return Response({"status":False,"error":f"Somthing Went Wrong : {e}"})
  
        return Response({"status":True})
    
    def put(self,request):
        TOKEN = request.headers.get('TOKEN')
        
        data=request.data
        try:
            username,password,name,phno=data["username"],data["password"],data["name"],int(data["phno"])
        except Exception as e:
            return Response({"status":False,"error": f"required: {str(e)}"})
        
        if not TOKEN:
            return Response({"status":False,"error": f"TOKEN: Login to edit data"})
        
        if not validateUserToken(username,TOKEN):
            return Response({"status":False,"error": f"TOKEN: Invalid TOKEN, Login to edit data"})
        
        status,req=checkReq([username,password,name,phno])
        if not status:
            return Response(req)
        
        data={"username":username,"password":password,"name":name,"phno":phno}
        status,e=updateUserProfile(data)
        if not status:
            return Response({"status":False,"error":f"Somthing Went Wrong : {e}"})
  
        return Response({"status":True})
            

class SimpleUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        uploaded_file = request.FILES.get("image")

        if not (uploaded_file):
            return Response({"status":False,"error": f"required: Missing fields"})

        file_url,e=addImage(uploaded_file)
        
        if not file_url:
            return Response({"status":False,"error": f"Somthing went wrong--> {e}"})
            
        return Response({"status":True})
     

    




