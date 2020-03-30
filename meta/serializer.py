from rest_framework import serializers
from meta.models import Table, MetaData


class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaData
        fields = ('id', 'numeric_column')


class TableSerializer(serializers.ModelSerializer):
    numeric_columns = MetaDataSerializer(read_only=True, many=True)

    class Meta:
        model = Table
        fields = ('id', 'name', 'numeric_columns')
