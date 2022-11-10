from django.contrib import admin
from django.urls import path

from .views import home_page, contact, startup, list_user, update, delete, updaterecord, detailed, userinformation, requests, leaveApprove, leaveDecline, AdminleaveApprove, AdminleaveDecline
from accounts.views import RegisterView, login_page, attendance, clockIn, clockOut
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', startup),
    path('home/', home_page, name='home_page'),
    path('contact/', contact, name='contact'),
    path('register/', RegisterView.as_view(), name='register'),
    path('my_info/', detailed, name='my_info'),
    path('user_info/', userinformation, name='userinformation'),
    path('login/', login_page, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="auth/logout.html"), name='logout'),
    path('admin/', admin.site.urls),

    path('users/', list_user, name='list_user'),
    path('update/updaterecord/<int:id>', updaterecord, name='updaterecord'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),

    path('leave-approve/<int:id>', leaveApprove, name='leaveApprove'),
    path('leave-decline/<int:id>', leaveDecline, name='leaveDecline'),
    path('admin-leave-approve/<int:id>', AdminleaveApprove, name='AdminleaveApprove'),
    path('admin-leave-decline/<int:id>', AdminleaveDecline, name='AdminleaveDecline'),

    path('emp_requests/', views.request_leave, name='request_leave'),
    # path('emp_requests/requests', views.requests, name='requests'),

    path('requests/', requests, name='requests'),
    # path('requests/request_leave', request_leave, name='request_leave'),

    path('attendance/', attendance, name='attendance'),
    path('clock-in/', clockIn, name='clock-in'),
    path('clock-out/', clockOut, name='clock-out'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)