from functools import partial
from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            student = Student.objects.get(pk=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created successfully'})
        else:
            return Response(serializer.errors)
    if request.method == 'PUT':
        id = request.data.get('id')
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated successfully'})
        else:
            return Response(serializer.errors)
    if request.method == 'DELETE':
        id = request.data.get('id')
        Student.objects.get(pk=id).delete()
        return Response({'msg': 'Data Deleted successfully'})
