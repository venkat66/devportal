from django.db.models import Q
from django.http import Http404, JsonResponse
from django.core.paginator import Paginator
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render, redirect

from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = ['/developers', 'developers/:username', 'companies']
    return Response(data)

# def index(request):
#     return render(request, 'base/index.html')

@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def developers(request,format=None):
    # data = ['Saddam', 'Rajesh', 'Sravani']
    # Handles the get request
    if request.method == "GET":
        query = request.GET.get('query')
        print(query,'queryyy')
        if query:
            developers = Developers.objects.filter(Q(username__icontains=query) | Q(bio__contains=query))
        else:
            developers = Developers.objects.all().order_by('-id')
        pagination = Paginator(developers,6)
        page_num = request.GET.get('page')
        print(page_num)
        page_obj = pagination.get_page(page_num)
        print(page_obj)
        serializer = DevelopersSerializer(page_obj,many=True)
        # different Pagination

        # paginator = PageNumberPagination()
        # paginator.page_size = 5
        # result_page = paginator.paginate_queryset(developers, request)
        # serializer = DevelopersSerializer(result_page, many=True)
        # return paginator.get_paginated_response(serializer.data)
        return Response(serializer.data)
    if request.method == "POST":
        print(request.data,'all data')
        advocate = Developers.objects.create(
            username = request.data['username'],
            bio = request.data['bio'],
            picture = request.data['picture']
        )
        serializer = DevelopersSerializer(advocate, many=False)
        return Response(serializer.data)

# @api_view(['GET','PUT','DELETE'])
# def developer_details(request,username):
#     advocate = Developers.objects.get(username__iexact=username)

#     if request.method == "GET":
#         serializer = DevelopersSerializer(advocate,many=False)
#         return Response(serializer.data)

#     if request.method == "PUT":
#         advocate.username = request.data["username"]
#         advocate.bio = request.data['bio']

#         advocate.save()

#         serializer = DevelopersSerializer(advocate,many=False)
#         return Response(serializer.data)

#     if request.method == "DELETE":
#         advocate.delete()
#         return Response('User Deleted Successfully')

class DeveloperDetail(APIView):
    def get_object(self,username):
        try:
            return Developers.objects.get(username__iexact=username)
        except Developers.DoesNotExist:
            raise Http404
    def get_comapy(self,company):
        try:
            return Company.objects.get(name__iexact=company)
        except Company.DoesNotExist:
            raise Http404
    def get(self, request, username):
        developer = self.get_object(username)
        serializer = DevelopersSerializer(developer, many=False)
        return Response(serializer.data)
    
    def put(self, request, username,format=None):
        developer = self.get_object(username)
        developer.username = request.data['username']
        developer.bio = request.data['bio']
        developer.picture = request.data['picture']
        developer.company = self.get_comapy(request.data['company'])
        developer.save()
        serializer = DevelopersSerializer(developer,many=False)
        return Response(serializer.data)
    
    def delete(self, request, username):
        developer = self.get_object(username)
        developer.delete()
        return Response('user has been deleted')


@api_view(['GET'])
def companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def echodata(request,format=None):
    aid = request.GET.get('aid')
    lat = request.GET.get('lat')
    log = request.GET.get('longitude')
    time = request.GET.gett('time')
    gps_data, created = EchoData.objects.get_or_create(aid=aid)
    gps_data.lat = lat
    gps_data.log =log
    gps_data.time=time
    gps_data.save()
    companies = EchoData.objects.all()
    serializer = EchodataSerializer(companies, many=True)
    if request.method == 'POST':
        data = request.data
        obj = EchoData.objects.create(data=data)
        print(request.data,'dddddd')
        serializer = EchodataSerializer(obj,many=False)

        return Response(serializer.data)
    return Response(serializer.data)