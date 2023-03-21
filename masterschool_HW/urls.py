"""masterschool_HW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('flow', views.get_flow),
    path('state', views.get_state),
    path('status', views.get_status),
    path('complete_step', views.make_step)
]

"""
1. Get - The entire flow (so that we can write to the user ”you are in step 3 / 8” and what steps are left).
2. Get - Current step and task for a specific user.
3. Post - Step completed (step_name, user_id, step_payload)
4. Get - Whether the user is accepted, rejected or in progress.
"""
