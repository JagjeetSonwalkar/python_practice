from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

'''
class StudentAPI(APIView):
    # read all or single data
    def get(self, request, student_id = None):
        # read single
        if student_id:
            try:
                student = Student.objects.get(id = student_id)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"error":"Student not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # read all
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, student_id):
        try:
            student = Student.objects.get(id = student_id)
        except Student.DoesNotExist:
            return Response({"error":"Student not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, student_id):
        try:
            student = Student.objects.get(id = student_id)
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
'''

'''
from rest_framework import generics, mixins
# curd operations usings GenericAPIView and Mixins
class StudentListCreateAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # read all data
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    # create data
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StudentRetriveUpdateDeleteAPI(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # get single data
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    # update data
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # delete data
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
'''

from rest_framework import viewsets
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer