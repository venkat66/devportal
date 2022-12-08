from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views


urlpatterns = [
    # path('', views.endpoints, name='home'),
    path('',views.endpoints,name='index'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('developers/', views.developers, name='developers'),
    # path('developers/<str:username>',views.developer_details, name='developer_details')
    path('developers/<str:username>/', views.DeveloperDetail.as_view()),

    # Companies
    path('companies/',views.companies),
    path('echodata/',views.echodata,name='echodata')
 ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)