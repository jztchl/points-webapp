# urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserLoginView, AdminLoginView, AdminOnlyView, UserRegistrationView, AppCreateView, AppDeleteView, AppListView, UserTaskUploadView, adminP, userP, UserProfileView, UserPointsView, UserCompletedTaskListView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('userp/',userP,name='user-panel'),
    path('adminp',adminP,name='admin-panel'),
    path('user-login/', UserLoginView.as_view(), name='user-login'),
    path('admin-login/', AdminLoginView.as_view(), name='admin-login'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),


    path('app/create/', AppCreateView.as_view(), name='app-create'),
    path('app/delete/<int:pk>/', AppDeleteView.as_view(), name='app-delete'),


     path('register/', UserRegistrationView.as_view(), name='register'),
     path('apps-list/', AppListView.as_view(), name='app-list'),
      path('task/upload/', UserTaskUploadView.as_view(), name='task-upload'),
      path('user/profile/', UserProfileView.as_view(), name='user-profile'),
       path('user/points/', UserPointsView.as_view(), name='user-points'),
       path('completed-tasks/', UserCompletedTaskListView.as_view(), name='user-completed-task-list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)