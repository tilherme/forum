from django.urls import include
from django.urls import path
from .views import *
# from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'user', UserViewSet)
router.register(r'subject', SubjectViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'answer', AnswerViewSet)

urlpatterns = [
    # path('auth/',  CustomAuthToken.as_view()),
    path('', include(router.urls)),
]
