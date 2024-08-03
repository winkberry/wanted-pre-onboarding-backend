from django.shortcuts import render

from rest_framework import viewsets
from .models import RecruitmentNotice, Applicant, Company
from .serializers import CompanySerializer, RecruitmentNoticeListSerializer, ApplicantSerializer, RecruitmentNoticeDetailSerializer


class RecruitmentNoticeViewSet(viewsets.ModelViewSet):
    queryset = RecruitmentNotice.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return RecruitmentNoticeListSerializer
        elif self.action == 'create':
            return RecruitmentNoticeDetailSerializer
        return RecruitmentNoticeDetailSerializer

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
