from django.urls import path
from .views import CoursesHomeView, CourseDetail, SectorCourse

urlpatterns = [
    path('detail/<uuid:course_uuid>/', CourseDetail.as_view()),
    path('', CoursesHomeView.as_view()),
    path('<uuid:sector_uuid>/',SectorCourse.as_view())
]