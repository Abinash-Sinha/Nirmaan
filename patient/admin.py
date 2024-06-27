from django.contrib import admin
from .models import Patient, Representative, Declaration, MOU
# Register your models here.

admin.site.register(Patient)
admin.site.register(Representative)
admin.site.register(Declaration)
admin.site.register(MOU)