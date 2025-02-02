from rest_framework import serializers
from .models import Company, RecruitmentNotice, Applicant

# 회사 목록 보기
class CompanySerializer(serializers.ModelSerializer):
    회사_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = Company
        fields = ['회사_id', 'country', 'region']

# 채용공고 목록보기
class RecruitmentNoticeListSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField(source='id', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    company_country = serializers.CharField(source='company.country', read_only=True)
    company_region = serializers.CharField(source='company.region', read_only=True)

    class Meta:
        model = RecruitmentNotice
        fields = ['company','post_id', 'company_name', 'company_country', 'company_region', 'position', 'compensation', 'technologies']

# 채용공고 상세보기
class RecruitmentNoticeDetailSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField(source='id', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    company_country = serializers.CharField(source='company.country', read_only=True)
    company_region = serializers.CharField(source='company.region', read_only=True)

    class Meta:
        model = RecruitmentNotice
        fields = ['company','post_id', 'company_name', 'company_country', 'company_region', 'position', 'compensation', 'technologies', 'content']

# 지원자 보기
class ApplicantSerializer(serializers.ModelSerializer):
    지원자_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = Applicant
        fields = ['지원자_id', 'position', 'technologies', 'experience']