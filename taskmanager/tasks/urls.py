# urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register, login_view, TaskListCreate, TaskDetail
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Task Management API",
        default_version='v1',
        description="API documentation for the Task Management System",
    ),
    public=True,
)

urlpatterns = [
    path('api/register/', register, name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
