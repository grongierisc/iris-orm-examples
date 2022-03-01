from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer
from rest_framework.response import Response

class PersonAPIView(APIView):

    # READ a single Person
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = Person.objects.all()

        serializer = PersonSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = PersonSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Person Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        Person_to_update = Person.objects.get(pk=pk)
        serializer = PersonSerializer(instance=Person_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Person Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format=None):
        Person_to_delete =  Person.objects.get(pk=pk)

        Person_to_delete.delete()

        return Response({
            'message': 'Person Deleted Successfully'
        })

