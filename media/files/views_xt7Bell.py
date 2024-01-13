# from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Lesson
from .serializers import LessonSerializer, StudentSerializer


# Lesson

@api_view(["GET"])
def lesson_list(request):
    lessons = Lesson.objects.all()
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def lesson_detail(request, pk):
    try:
        lesson = Lesson.objects.get(pk=pk)
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)
    except Lesson.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def lesson_update(request, pk):
    lesson = Lesson.objects.get(pk=pk)
    serializer = LessonSerializer(lesson, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def lesson_create(request):
    serializer = LessonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def lesson_delete(request, pk):
    lesson = Lesson.objects.get(pk=pk)
    lesson.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Student

@api_view(["GET"])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def student_create(request):
    serializer = StudentSerializer(data=request)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# class LessonViewSet(viewsets.ModelViewSet):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonSerializer
#
#
# class LessonDetailViewSet(viewsets.ModelViewSet):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonSerializer
#
#
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDetailViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
