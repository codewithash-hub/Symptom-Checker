from django.contrib import admin
from .models import Interaction

# Register your models here.
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_input', 'ai_response', 'timestamp')

admin.site.register(Interaction, InteractionAdmin)