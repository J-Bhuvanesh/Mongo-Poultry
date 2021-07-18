from django.db import models

# Create your models here.
from django.db import models

class NewBatch(models.Model):

    user_id = models.AutoField(primary_key=True)
    total_chicks=models.IntegerField(blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table="all_batch"
