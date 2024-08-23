# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import UserProfile, App, UserTask





class AppPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'name', 'points']

class UserPointsSerializer(serializers.Serializer):
    total_points = serializers.IntegerField()
    app_points = serializers.SerializerMethodField()

    def get_app_points(self, obj):
        user = obj['user']
        tasks = UserTask.objects.filter(user=user, completed=True)
        app_points = {}
        for task in tasks:
            if task.app.id not in app_points:
                app_points[task.app.id] = {
                    'app': AppPointsSerializer(task.app).data,
                    'points': 0
                }
            app_points[task.app.id]['points'] += task.points
        return list(app_points.values())



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'profile_image', 'total_points']





class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = ['id', 'app', 'screenshot', 'points', 'completed']
        extra_kwargs = {
            'points':{'required':True},
            'completed':{'required':True}
        }

    def validate(self, data):
        app = data.get('app')
        user = self.context['request'].user

        if not App.objects.filter(id=app.id).exists():
            raise serializers.ValidationError("App does not exist.")

        if UserTask.objects.filter(user=user, app=app, completed=True).exists():
            raise serializers.ValidationError("Task for this app has already been completed.")

        return data



class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id','name', 'app_link', 'app_icon', 'category', 'sub_category', 'points']
        extra_kwargs = {
            'app_link': {'required': True},
            'points':{'required':True},
            'app_icon':{'required':True}
        }

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    profile_image = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'profile_image']
        extra_kwargs = {
            'email': {'required': True},
            'profile_image': {'required': True},
        }

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already taken.")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        profile_image = validated_data.pop('profile_image', None)
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        UserProfile.objects.create(user=user, profile_image=profile_image)

        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active and user.is_superuser:
            return user
        raise serializers.ValidationError("Incorrect Credentials or not an admin")


class UserCompletedTaskSerializer(serializers.ModelSerializer):
    app = AppSerializer()  # Use the nested serializer for the app field

    class Meta:
        model = UserTask
        fields = ['id', 'app', 'screenshot', 'points', 'completed']