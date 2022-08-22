from django.urls import path
from .views import (CoursesHomeView, 
                    CourseDetail, 
                    SectorCourse,
                    SearchCourse)

urlpatterns = [
    path('detail/<uuid:course_uuid>/', CourseDetail.as_view()),
    path('search/<str:search_term>/', SearchCourse.as_view()),
    path('', CoursesHomeView.as_view()),
    path('<uuid:sector_uuid>/',SectorCourse.as_view())
]