from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response

from .models import LogEntry
from .serializers import LogEntrySerializer


class IpLogView(CreateModelMixin, ListModelMixin, GenericAPIView):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer

    def get(self, request, *args, **kwargs):
        """ Lists LogEntry records. """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ Creates LogEntry record from either HTTP_X_FORWARDED_FOR
        header (if available) or REMOTE_ADDR. """

        real_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        # HTTP_X_FORWARDED_FOR can be a comma-separated list of IPs.
        # In this case we will use the first one.
        real_ip = real_ip.split(",")[0] if real_ip else request.META['REMOTE_ADDR']
        data = {'ip': real_ip}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
