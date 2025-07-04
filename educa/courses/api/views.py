# courses/api/views.py

from rest_framework import generics
from courses.api.serializers import SubjectSerializer, CourseSerializer
from courses.models import Subject, Course

from django.db.models import Count

from courses.api.pagination import StandardPagination

from rest_framework import viewsets

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.authentication import BasicAuthentication

from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import action

from courses.api.permissions import IsEnrolled
from courses.api.serializers import CourseWithContentsSerializer



class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.prefetch_related('modules')
    serializer_class = CourseSerializer
    pagination_class = StandardPagination


    @action(
        detail=True,
        methods=['post'],
        authentication_classes=[BasicAuthentication],
        permission_classes = [IsAuthenticated]
    )
    
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})
    
    
    @action(
        detail=True,
        methods=['get'],
        serializer_class=CourseWithContentsSerializer,
        authentication_classes=[BasicAuthentication],
        permission_classes=[IsAuthenticated, IsEnrolled]
    )
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# class SubjectListView(generics.ListAPIView):
    
#     # queryset = Subject.objects.all()
    
#     queryset = Subject.objects.annotate(total_courses=Count('courses'))
#     serializer_class = SubjectSerializer
#     pagination_class = StandardPagination
    
    
    
# class SubjectDetailView(generics.RetrieveAPIView):
    
#     # queryset = Subject.objects.all()
    
#     queryset = Subject.objects.annotate(total_courses=Count('courses'))
#     serializer_class = SubjectSerializer


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.annotate(total_courses=Count('courses'))
    serializer_class = SubjectSerializer
    pagination_class = StandardPagination
    
    
# API view to allow users enroll in a course
# class CourseEnrollView(APIView):
    
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk)
#         course.students.add(request.user)
#         return Response({'enrolled': True})