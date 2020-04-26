from django.contrib import admin

# Register your models here.
from .models import Voter

class VoterAdmin(admin.ModelAdmin):
    #fields = ['first_name','last_name', 'email', 'phone']
    pass

admin.site.register(Voter,VoterAdmin)
