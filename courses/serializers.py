from .models import Course, Comment, CourseSection, Episode
from rest_framework import serializers
from users.serializers import UserSerializer

class CourseDisplaySerializer(serializers.ModelSerializer):
    student_no = serializers.IntegerField(source='get_enrolled_student')
    author = UserSerializer()
    image_url=serializers.CharField(source='get_absolute_image_url')

    class Meta:
        model = Course
        fields = [
            'course_uuid',
            'title',
            'student_no',
            'author',
            'price',
            'image_url'
        ]

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True) 

    class Meta:
        model = Comment
        exclude =[
            'id'
        ]

# get_video_length_time
class EpisodeUnPaidSerializer(serializers.ModelSerializer):
    length = serializers.CharField(source="get_video_length_time")

    class Meta:
        model = Episode
        exclude = [
            'file'
        ]

class CourseSectionUnPaidSerializer(serializers.ModelSerializer):
    episodes = EpisodeUnPaidSerializer(many=True)
    total_duration = serializers.CharField(source = 'total_length')
    class Meta:
        model = CourseSection
        fields=[
            'section_title',
            'episodes',
            'total_duration',
        ]
class CourseUnpaidSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    comments = CommentSerializer(many=True)
    course_section = CourseSectionUnPaidSerializer(many=True)
    student_no = serializers.IntegerField(source="get_enrolled_student")
    total_lectures = serializers.IntegerField(source="get_total_lectures")
    total_duration = serializers.CharField(source="total_course_length")
    image_url = serializers.CharField(source="get_absolute_image_url")
    
    class Meta:
        model = Course
        exclude = (
            "id",
        )

class CourseListSerializer(serializers.ModelSerializer):
    student_no = serializers.IntegerField(source="get_enrolled_student")
    author = UserSerializer()
    total_lectures = serializers.IntegerField(source="get_total_lectures")
    description = serializers.CharField(source='get_brief_description')  

    class Meta:
        model = Course
        fields=[
            'course_uuid',
            'title',
            'student_no',
            'author',
            'price',
            'image_url',
            'description',
            'total_lectures'
        ]