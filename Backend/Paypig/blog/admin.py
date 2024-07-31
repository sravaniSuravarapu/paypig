from django.contrib import admin
from .models import VideoUpload,Contact,EarnerImage,Playlist
admin.site.register(VideoUpload)
admin.site.register(Contact)
admin.site.register(EarnerImage)
class PlaylistAdmin(admin.ModelAdmin):
    list_display=['id','title','image']
admin.site.register(Playlist,PlaylistAdmin)