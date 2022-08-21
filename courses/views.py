from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from courses.models import Sector, Course
from .serializers import (
        CourseDisplaySerializer, 
        CourseUnpaidSerializer,
        CourseListSerializer,
    )
from django.http import HttpResponseBadRequest

class CoursesHomeView(APIView): 

    def get(self, request, *args, **kwargs):
        sectors = Sector.objects.order_by("?")[:6]

        sector_response = []

        for sector in sectors:
            sector_courses = sector.releted_course.order_by("?")[:4]
            course_Serializer = CourseDisplaySerializer(sector_courses, many=True)

            sector_obj={
                'sector_name': sector.name,
                'sector_uuid': sector.sector_uuid,
                'featured_course': course_Serializer.data,
                'sector_image': sector.get_image_absolute_url(),
            }

            sector_response.append(sector_obj)

        return Response(data=sector_response, status=status.HTTP_200_OK)

class CourseDetail(APIView):
    def get(self, request, course_uuid, *args, **kwargs):
        course = Course.objects.filter(course_uuid=course_uuid)

        if not course:
            return HttpResponseBadRequest("Kurs topilmadi!")

        serializer = CourseUnpaidSerializer(course[0])

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class SectorCourse(APIView):
    def get(self, request, sector_uuid, *args, **kwargs):
        sector = Sector.objects.filter(sector_uuid=sector_uuid)

        if not sector:
            return HttpResponseBadRequest('Sector does not exist')

        sector_courses = sector[0].releted_course.all()
        serializer = CourseListSerializer(sector_courses, many=True)

        total_students = 0

        for course in sector_courses:
            total_students+=course.get_enrolled_student()

        return Response({
            'data': serializer.data,
            'sector_name': sector[0].name,
            'total_students': total_students,
        }, status=status.HTTP_200_OK)

