from django.shortcuts import render
from .serializers import ContactSerializer,EarnerImageSerializer,PlaylistSerializer,VideoSerializer
from rest_framework.views import APIView
from .models import Contact,EarnerImage,Playlist,VideoUpload
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import Http404
from rest_framework import generics

    
class ContactView(APIView):
    permission_classes=(IsAdminUser,)
    def get(self,request):
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,pk):
       try :
         contact = Contact.objects.get(pk=pk)
         contact.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
       except Contact.DoesNotExist:
           return Response({"message":"Message Does not exist"},status=status.HTTP_404_NOT_FOUND)
    
    permission_classes =(IsAuthenticated,)
    def post(self,request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Message sent successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EarnerView(APIView):
    def get_object(self, pk):
        try:
            return EarnerImage.objects.get(pk=pk)
        except EarnerImage.DoesNotExist:
            raise Http404  

    def get(self,request):
        earner = EarnerImage.objects.all()
        serializer = EarnerImageSerializer(earner,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        earner = self.get_object(pk)
        serializer = EarnerImageSerializer(earner,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Successfully updated"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class PlaylistView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def get(self,request):
        playlist = Playlist.objects.all()
        serializer = PlaylistSerializer(playlist,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer= PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Successfully Created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PlaylistDestroyAPIView(generics.DestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
  
    
class PlayListVideoView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def get_object(self,pk):
      try:
         return Playlist.objects.get(id=pk)
      except Playlist.DoesNotExist:
          raise Http404
    def get(self,request,pk):
        playlist = self.get_object(pk)
        video = VideoUpload.objects.filter(playlist=playlist)
        serializer = VideoSerializer(video,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,pk):
        playlist = self.get_object(pk)
        request.data['playlist']=playlist.id
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Successfully uploaded"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)      