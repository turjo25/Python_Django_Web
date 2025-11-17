from django.shortcuts import render
from .import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

# Create your views here.

#category
@api_view(['GET','POST'])
def category_list_create(request):
    if request.method == 'GET':
        categories = models.Category.objects.all() #queryset, dictionarty
        serializer = serializers.CategorySerializer(categories,many=True)#dictionary --> json
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if not request.user.is_authenticated or request.user.role != 'admin':
            return Response({'detail' :'only admin can create catagories'})
        
        serializer = serializers.CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','POST'])
def course_list_create(request):
    if request.method == 'GET':
        #category , search
        category = request.query_params.get('category')# GET er poriborte query_params cz api ashbe
        search = request.query_params.get('search')
        queryset = models.Course.objects.all()

        if category:
            queryset = queryset.filter(category__title__icontains = category)
        
        if search:
            queryset = queryset.filter(
                Q(title__icontains = search) |
                Q(description__icontains = search)
            )
        
        if request.user.is_authenticated and request.user.role == 'teacher':
            queryset = queryset.filter(instructor = request.user)# teacher just tar nijer build kora course get korte parbe
        
        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_queryset = paginator.paginate_queryset(queryset,request)
        
        serializer = serializers.CourseSerializer(
            paginated_queryset,
            many=True,
            context = {'request': request}
            )
        return paginator.get_paginated_response(serializer.data)
    
    elif request.method == 'POST':
        if request.user.is_authenticated and request.user.role != 'teacher':
            return Response({'detail':'only teachers can create course'})
        serializer = serializers.CourseSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#course details banayte hbe

@api_view(['GET','POST'])
def lesson_list_create(request):
    #GET
    if request.method == 'GET':
        course = request.query_params.get('courseId')
        if not course:
            return Response({'detail':'course is required'})
        try:
            course = models.Course.objects.get(pk=course)
        except models.Course.DoesNotExist:
            return Response({'detail':'Course not found'})
        
        is_teacher = request.user.is_authenticated and request.user.role == 'teacher' and request.user == course.instructor
        is_admin = request.user.is_authenticated and request.user.role == 'admin'
        is_enrolled = models.Enrollment.objects.filter(
            student = request.user,
            course = course,
            status = 'active'
        ).exists() if request.user.is_authenticated and request.user.role == 'student' else False
        #student jde api te request kore then dekhte hocce je shey enrolled kina, na hole access pabe na
        
        if not (is_teacher or is_admin or is_enrolled):
            return Response({'detail':"You don't have permissions to view these lessons"})
        lessons = models.Lesson.objects.filter(course=course)
        serializer = serializers.LessonSerializer(lessons,many=True)
        return Response(serializer.data)
    
    #POST
    elif request.method == 'POST':
        course = request.query_params.get('courseId')
        if not course:
            return Response({'detail':'course is required'})
        try:
            course = models.Course.objects.get(pk=course)
        except models.Course.DoesNotExist:
            return Response({'detail':'Course not found'})
    
        if request.user != course.instructor:
            return Response({'detail':'You can only add lessons to your own courses'})
        serializer = serializers.LessonSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#lesson details create korte hobe


@api_view(['GET','POST'])
def material_list_create(request):
    #GET
    if request.method == 'GET':
        lesson = request.query_params.get('lessonId')
        if not lesson:
            return Response({'detail':'lesson id is required'})
        try:
            lesson = models.Lesson.objects.get(pk=lesson)
        except models.Lesson.DoesNotExist:
            return Response({'detail':'lesson not found'})
        
        course = lesson.course
        is_teacher = request.user.is_authenticated and request.user.role == 'teacher' and request.user == course.instructor
        is_admin = request.user.is_authenticated and request.user.role == 'admin'
        is_enrolled = models.Enrollment.objects.filter(
            student = request.user,
            course = course,
            status = 'active'
        ).exists() if request.user.is_authenticated and request.user.role == 'student' else False
        #student jde api te request kore then dekhte hocce je shey enrolled kina, na hole access pabe na
        
        if not (is_teacher or is_admin or is_enrolled):
            return Response({'detail':"You don't have permissions to view these material"})
        materials = models.Material.objects.filter(course=course)
        serializer = serializers.MaterialSerializer(materials,many=True)
        return Response(serializer.data)
    
    #POST
    elif request.method == 'POST':
        course = request.query_params.get('courseId')
        if not course:
            return Response({'detail':'course is required'})
        try:
            course = models.Course.objects.get(pk=course)
        except models.Course.DoesNotExist:
            return Response({'detail':'Course not found'})
    
        if request.user != course.instructor:
            return Response({'detail':'You can only add lessons to your own courses'})
        serializer = serializers.LessonSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#enrollment list
@api_view(['GET'])
def enrollment_list(request):
    if request.user.role == 'teacher':
        course = request.query_params.get('courseId')
        if not course:
            return Response({'detail':'course is required'})
        try:
            course = models.Course.objects.get(pk=course)
        except models.Course.DoesNotExist:
            return Response({'detail':'Course not found'})
        
        if request.user != course.instructor:
            return Response({'detail':'You can only view your enrollment course'})

        enrollments = models.Enrollment.objects.filter(course=course)
        serializer = serializers.EnrollmentSerializer(enrollments,many=True)
        return Response(serializer.data)
    elif request.user.role == 'student':
        enrollments = models.Enrollment.objects.filter(student=request.user)
        serializer = serializers.EnrollmentSerializer(enrollments,many=True)
        return Response(serializer.data)
    
    elif request.user.role == 'admin':
        return Response({'detail':'GO to admin dashboard'})
    else:
        return Response({'detail':'Unauthorized access'})
    
    
#enrollcourse
@api_view(['POST'])
def enroll_course(request):
    if request.user.role != 'student':
        return Response({'detail':'Only students can enroll'})
    
    course = request.data.get('course')
    payment_method = request.data.get('payment_method','free')
    price = request.data.get('price')
    
    try:
        course = models.Course.objects.get(pk=course)
    except models.Course.DoesNotExist:
        return Response({'detail':'Course not found'})
    
    if models.Enrollment.objects.filter(student = request.user, course=course).exists():
        return Response({'detail':'Your are already enrolled'})
    
    enrollment = models.Enrollment.objects.create(
        student = request.user,
        course = course,
        price = price
    )
    serializer = serializers.EnrollmentSerializer(enrollment)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

#question answer