from django.conf.urls import url, include

from rest_framework import routers
from api import views as myapp_views



router = routers.DefaultRouter()
router.register(r'names', myapp_views.CognoViewset)

'''
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='API name')
from django.urls import path
urlpatterns = [
    path('', schema_view)
] 

urlpatterns += [
	url(r'^docs/', include('rest_framework_swagger.urls')),
]

urlpatterns += router.urls
'''
