from rest_framework import generics
from rest_framework import views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from sibdev.models import Client
from sibdev.services import parse_data
from sibdev.serializers import TopFiveSerializer


class TopFiveList(generics.ListAPIView):
    queryset = Client.get_top_five()
    serializer_class = TopFiveSerializer


class FileUploadView(views.APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        file_obj = request.data['deals']
        response_text, response_status = parse_data(file_obj)

        return Response(response_text, status=response_status)