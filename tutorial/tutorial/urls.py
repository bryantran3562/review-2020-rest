"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

####################################################################
#BT - @api_view
####################################################################
# from django.urls import path
# from snippets import views

# from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

####################################################################
#BT - Class base view
####################################################################

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
#from snippets.views import SnippetList, SnippetDetail
#from automobile.views import PersonList, PersonDetail, CarList, CarDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    #BT - Understanding: Step 1: User entered a url: localhost/8000/
    #     It matched here. See Step 2 in snippets.urls.
    path('', include('snippets.urls')),
    
]
#BT - Adding authentication from rest_framework
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

