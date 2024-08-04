from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import RecruitmentNotice, Applicant, Company
from .serializers import CompanySerializer, RecruitmentNoticeListSerializer, ApplicantSerializer, RecruitmentNoticeDetailSerializer

# 채용공고 목록보기 / 상세보기
class RecruitmentNoticeViewSet(viewsets.ModelViewSet):
    queryset = RecruitmentNotice.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return RecruitmentNoticeListSerializer
        elif self.action == 'create':
            return RecruitmentNoticeDetailSerializer
        return RecruitmentNoticeDetailSerializer

# 채용공고 검색기능
class RecruitmentNoticeSearchView(generics.ListAPIView):
    queryset = RecruitmentNotice.objects.all()
    serializer_class = RecruitmentNoticeListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        position = self.request.query_params.get('position', None)
        company_name = self.request.query_params.get('company_name', None)
        company_country = self.request.query_params.get('company_country', None)
        company_region = self.request.query_params.get('company_region', None)
        compensation = self.request.query_params.get('compensation', None)
        technologies = self.request.query_params.get('technologies', None)

        if position:
            queryset = queryset.filter(position__icontains=position)

        if company_name:
            queryset = queryset.filter(company__name__icontains=company_name)

        if company_country:
            queryset = queryset.filter(company__country__icontains=company_country)

        if company_region:
            queryset = queryset.filter(company__region__icontains=company_region)

        if compensation:
            queryset = queryset.filter(compensation__icontains=compensation)

        if technologies:
            queryset = queryset.filter(technologies__icontains=technologies)
        
        return queryset

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
