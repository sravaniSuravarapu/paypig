from rest_framework import serializers
from .models import Contact,EarnerImage,Playlist,VideoUpload
# VideoUpload,
# class VideoUploadSerializer(serializers.ModelSerializer):
#     video = serializers.FileField()
#     class Meta:
#         model = VideoUpload
#         fields = "__all__"
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
    
class EarnerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EarnerImage
        fields ="__all__"

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoUpload
        fields="__all__"

class PlaylistSerializer(serializers.ModelSerializer):
    video = VideoSerializer(many=True,required=False)
    class Meta:
        model = Playlist
        fields = ['id', 'title', 'image', 'video']

