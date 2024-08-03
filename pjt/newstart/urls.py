from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecruitmentNoticeViewSet, ApplicantViewSet, CompanyViewSet

router = DefaultRouter()
router.register(r'Recruitment-Notice', RecruitmentNoticeViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'applicants', ApplicantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

