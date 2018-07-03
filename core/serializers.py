from rest_framework.serializers import HyperlinkedModelSerializer

from core.models import CallRecord


class StartCallRecordModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CallRecord
        fields = ('url', 'type', 'timestamp', 'call_id', 'source', 'destination')


class EndCallRecordModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CallRecord
        fields = ('url', 'type', 'timestamp', 'call_id')