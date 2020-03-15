from django.db import models


class MetaData(models.Model):
    table_name = models.CharField(max_length=500)
    numeric_column = models.CharField(max_length=500)

    class Meta:
        unique_together = ['table_name', 'numeric_column']
