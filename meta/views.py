import sqlite3

from django.db import connection
from django.shortcuts import get_object_or_404

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

from meta.models import Table, MetaData
from utils.file_utils import read_file, get_table_name
from meta.serializer import TableSerializer


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser, )

    def post(self, request, format=None):
        file = request.data['file']
        try:
            df = read_file(file)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        table_name = get_table_name(file)
        numeric_columns = df.select_dtypes('number').columns.tolist()

        db_name = connection.settings_dict['NAME']
        conn = sqlite3.connect(db_name)
        df.to_sql(name=table_name, con=conn)

        table = Table.objects.create(name=table_name, creator=request.data['creator'])
        table.save()
        MetaData.objects.bulk_create([
            MetaData(table=table, numeric_column=column) for column in numeric_columns
        ])
        return Response({'table_name': table_name}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_files_list(request, creator):
    tables = Table.objects.filter(creator=creator)
    serializer = TableSerializer(tables, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_fuzzy_set(request):
    table_name = request.data['table_name']
    table = get_object_or_404(Table, table_name=table_name)
    with connection.cursor() as cursor:
        cursor.execute(f"select * from {table_name}")
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
