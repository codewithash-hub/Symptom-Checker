from django.contrib import admin
from .models import Interaction, Feed

# Register your models here.
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_input', 'ai_response', 'timestamp')

admin.site.register(Interaction, InteractionAdmin)

class FeedAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'description', 'date_added', 'images')
    
admin.site.register(Feed, FeedAdmin)