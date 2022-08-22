from django.urls import path
from .views import (CoursesHomeView, 
                    CourseDetail, 
                    SectorCourse,
                    SearchCourse,
                    AddComent,
                    GetCartDetail)

urlpatterns = [
    path('cart/', GetCartDetail.as_view()),
    path('detail/<uuid:course_uuid>/', CourseDetail.as_view()),
    path('search/<str:search_term>/', SearchCourse.as_view()),
    path('comment/<uuid:course_uuid>/', AddComent.as_view()),
    path('', CoursesHomeView.as_view()),
    path('<uuid:sector_uuid>/',SectorCourse.as_view())
]