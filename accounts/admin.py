from django.contrib import admin
from django.contrib.auth import get_user_model

from accounts.models import Attendance
from .models import RequestLeave

User= get_user_model()

admin.site.register(User)
admin.site.register(Attendance)
admin.site.register(RequestLeave)