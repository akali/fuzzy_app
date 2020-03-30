from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=500)
    creator = models.CharField(max_length=1_000)

    class Meta:
        unique_together = ['name', 'creator']


class MetaData(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='numeric_columns')
    numeric_column = models.CharField(max_length=500)

    class Meta:
        unique_together = ['table', 'numeric_column']
