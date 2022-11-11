from rest_framework import status
from .serializers import TutorialsSerializer
from .models import Tutorials
from rest_framework.views import APIView

from django.http import JsonResponse
from rest_framework.response import Response
import logging

logger = logging.getLogger('user')


class TutorialList(APIView):

    def get(self, request):
        tutorials = Tutorials.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = TutorialsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        tutorial_serializer = TutorialsSerializer(data=request.data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_200_OK)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TutorialDetail(APIView):

    def get_object(self, pk):
        try:
            # print(User.objects.filter(id=pk))
            return Tutorials.objects.filter(id=pk)
        except Tutorials.DoesNotExist:
            raise Tutorials

    def get(self, request, pk):
        data = self.get_object(pk)
        tutorials_serializer = TutorialsSerializer(data, many=True, context={'request': request})
        logger.error("GET data")
        return Response(tutorials_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        data = self.get_object(pk).first()
        print(data, request.data)
        tutorial_serializer = TutorialsSerializer(data, data=request.data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_200_OK)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        data = self.get_object(pk).first()
        if data is None:
            return Response({'message': 'No object Found'}, status=status.HTTP_200_OK)
        data.delete()
        return Response({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_200_OK)


class TutorialPublished(APIView):
    tutorial_data = Tutorials.objects.filter(published=False)

    def get(self, request):
        tutorials_serializer = TutorialsSerializer(self.tutorial_data, many=True, context={'request': request})
        return Response(tutorials_serializer.data, status=status.HTTP_200_OK)
