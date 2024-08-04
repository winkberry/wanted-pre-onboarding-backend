from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecruitmentNoticeViewSet, ApplicantViewSet, CompanyViewSet, RecruitmentNoticeSearchView

router = DefaultRouter()
router.register(r'Recruitment-Notice', RecruitmentNoticeViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'applicants', ApplicantViewSet)

urlpatterns = [
    path('api/', include(router.urls)), 
    # 채용공고 검색 url
    path('search/Recruitment-Notice/', RecruitmentNoticeSearchView.as_view(), name='recruitment-notice-search'),
]
