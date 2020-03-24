# ####################################################################
# #BT - @api_view
# ####################################################################
# from django.urls import path
# from snippets import views

# from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     path('', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

# ####################################################################
# #BT - Class base view - ApiView
# ####################################################################

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)