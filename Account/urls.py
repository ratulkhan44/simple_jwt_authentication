from django.urls import path
from .views import LoginView,RegistrationApiView,BookListView

urlpatterns = [
    # path('api-token/', MyTokenObtainPairView.as_view(),name='api_token'),
    path('api-registration/', RegistrationApiView.as_view(),name='api_register'),
    path('api-login/', LoginView.as_view(),name='api_login'),
    path('api-booklist/', BookListView.as_view(),name='api_booklist'),
]