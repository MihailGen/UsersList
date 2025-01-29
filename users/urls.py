from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, home, SignUp, metrics, compute, heavy_compute



urlpatterns = [
    path('', home, name="home"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('metrics/', metrics, name='prometheus_metrics'),
    #path('compute/', compute, name='prometheus_compute'),
    #path('heavy_compute/', heavy_compute, name='prometheus_heavy_compute'),

]
