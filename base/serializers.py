from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Developers, Company


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