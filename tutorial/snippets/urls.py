# from django.urls import path
# from snippets import views
# from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
#     path('', views.api_root),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),

# ]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# API endpoints
# urlpatterns = format_suffix_patterns([
#     #BT - Right here is where our path goes to views.api_root
#     path('', views.api_root),
#     path('snippets/',
#         views.SnippetList.as_view(),
#         name='snippet-list'),
#     path('snippets/<int:pk>/',
#         views.SnippetDetail.as_view(),
#         name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight'),
#     path('users/',
#         views.UserList.as_view(),
#         name='user-list'),
#     path('users/<int:pk>/',
#         views.UserDetail.as_view(),
#         name='user-detail')
# ])

# urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
#BT - The DefaultRouter will automatically create an API root for you where it contained
#     all the api endponts below here.
router = DefaultRouter()


router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

#BT - Register for different app here.
from automobile.views import CarViewSet, PersonViewSet

#BT - Understand - Step 3: Matched one of this API endpoint and a corresponding views will be called.
#                          Take a look at automobile/views.py for the next step.
router.register(r'car', CarViewSet)
router.register(r'person', PersonViewSet)

# The API URLs are now determined automatically by the router.

#BT - Understand: Step 2: It will matched this and calls the DefaultRouter() above to display
#                         an API root where it shows all the api end points above there. So that,
#                         the user can click on the HyperLink.
urlpatterns = [
    path('', include(router.urls)),
]