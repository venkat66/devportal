from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *


class CompanySerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True)
    class Meta:
        model = Company
        fields = '__all__'

    def get_employee_count(self, obj):
        count = obj.developers_set.count()
        return count

class DevelopersSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Developers
        fields = '__all__'


class EchodataSerializer(ModelSerializer):
    class Meta:
        model = EchoData
        fields = '__all__'