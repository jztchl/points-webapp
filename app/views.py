# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserLoginSerializer, AdminLoginSerializer, UserRegistrationSerializer, AppSerializer, UserTaskSerializer, UserProfileSerializer, UserPointsSerializer, UserCompletedTaskSerializer
from .models import App, UserProfile,UserTask
from django.shortcuts import render
from rest_framework.permissions import BasePermission,IsAuthenticated


def adminP(requests):
    return render(requests,'admin.html')

def userP(requests):
    return render(requests,'user.html')


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, *args, **kwargs):
        return Response({'message': 'This endpoint is only accessible to admin users.'}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Your admin-only logic here
        return Response({'message': 'Admin-only POST request processed.'}, status=status.HTTP_200_OK)


class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

class AdminLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AdminLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

#User APIs
class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'User registered successfully.',
                'user': {
                    'username': user.username,
                    'email': user.email,
                    'profile_image': user.userprofile.profile_image.url if hasattr(user, 'userprofile') else None
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Admin APIs
class AppCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = AppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, pk, *args, **kwargs):
        try:
            app = App.objects.get(pk=pk)
            app.delete()
            return Response({'message': 'App deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except App.DoesNotExist:
            return Response({'message': 'App not found.'}, status=status.HTTP_404_NOT_FOUND)
        
class AppListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        apps = App.objects.all()
        serializer = AppSerializer(apps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UserTaskUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = UserTaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
    
class UserPointsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        data = {
            'user': user,
            'total_points': profile.total_points
        }
        serializer = UserPointsSerializer(data)
        return Response(serializer.data)
    

class UserCompletedTaskListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = UserTask.objects.filter(user=self.request.user, completed=True)
        serializer = UserCompletedTaskSerializer(data, many=True)
        return Response(serializer.data)