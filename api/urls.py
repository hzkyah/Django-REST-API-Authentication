'''
#from django.conf.urls import url, include
#from rest_framework.urlpatterns import format_suffix_patterns
#from .views import CreateView
from django.urls import path

from . import views 

urlpatterns = [
	path('', views.CreateView.as_view()),
	path('<int:pk>/', views.Detail.as_view()),
    #url(r'^names/$', CreateView.as_view(), name="create"),
]
'''

#urlpatterns = format_suffix_patterns(urlpatterns)