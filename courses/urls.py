from django.urls import path
from .views import CoursesHomeView, CourseDetail

urlpatterns = [
    path('detail/<uuid:course_uuid>/', CourseDetail.as_view()),
    path('', CoursesHomeView.as_view())
]