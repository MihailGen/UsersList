from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, home, SignUp
from datetime import time

# ----------------- Prometheus encapsulate --------------------------

from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

app = FastAPI()

REQUEST_COUNT = Counter('request_count', 'Total number of requests', ['UsersList', 'endpoint'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency', ['UsersList', 'endpoint'])


class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        endpoint = request.url.path
        REQUEST_COUNT.labels(app_name='UsersList', endpoint=endpoint).inc()
        with REQUEST_LATENCY.labels(app_name='UsersList', endpoint=endpoint).time():
            response = await call_next(request)
        return response


app.add_middleware(MetricsMiddleware)


@app.get('/metrics')
async def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)


@app.get('/compute')
def compute():
    time.sleep(2)
    return {"message": "Completed a complex computation"}


@app.get('/heavy_compute')
def heavy_compute():
    for t in range(150):
        time.sleep(2)
    return {"message": "Completed a series of computations"}


# --------------- Prometheus End ---------------------------------


urlpatterns = [
    path('', home, name="home"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('metrics/', metrics(), name='prometheus_metrics'),
    #path('compute/', compute(), name='prometheus_compute'),
    #path('heavy_compute/', heavy_compute(), name='prometheus_heavy_compute'),

]
