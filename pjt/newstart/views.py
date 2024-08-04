from django.shortcuts import render
from rest_framework import generics
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

class RecruitmentNoticeSearchView(generics.ListAPIView):
    queryset = RecruitmentNotice.objects.all()
    serializer_class = RecruitmentNoticeListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        position = self.request.query_params.get('position', None)
        company_name = self.request.query_params.get('company_name', None)

        # 로그 출력
        print(f"Position: {position}, Company Name: {company_name}")

        if position:
            queryset = queryset.filter(position__icontains=position)
        
        if company_name:
            queryset = queryset.filter(company__name__icontains=company_name)
        
        return queryset

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
