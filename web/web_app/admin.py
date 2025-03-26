from django.contrib import admin
from .models import StatusModel, JobTitle, Address

admin.site.register([StatusModel, JobTitle, Address])

