from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from core.models import CallRecord
from core.serializers import StartCallRecordModelSerializer
from core.serializers import EndCallRecordModelSerializer


class CallStartRecordViewSet(ModelViewSet):
    """
    retrieve:
    Returns a list of all the call records for starting phone calls

    post:
    creates a new CallRecord object with start as it's type
    """

    queryset = CallRecord.objects.filter(type='start')
    serializer_class = StartCallRecordModelSerializer


class CallEndRecordViewSet(ModelViewSet):
    """
    retrieve:
    Returns a list of all the call records for ending phone calls

    post:
    creates a new CallRecord object with end as it's type
    """

    queryset = CallRecord.objects.filter(type='end')
    serializer_class = EndCallRecordModelSerializer


class BillRetrieveView(RetrieveAPIView):
    """

    """
    queryset = CallRecord.objects.all()