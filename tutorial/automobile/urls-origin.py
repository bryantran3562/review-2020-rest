from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
#from snippets.views import SnippetList, SnippetDetail
#from automobile.views import PersonList, PersonDetail, CarList, CarDetail

# urlpatterns = [
#     path('car', CarList.as_view()),
#     path('car/<int:pk>/', CarDetail.as_view()),
#     path('person/', PersonList.as_view()),
#     path('person/<int:pk>/', PersonDetail.as_view()),
    
# ]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from automobile.views import CarViewSet, PersonViewSet

# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'car', CarViewSet)
# router.register(r'person', PersonViewSet)

# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]