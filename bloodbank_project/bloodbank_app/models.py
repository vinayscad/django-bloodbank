from django.db import models

# Create your models here.
from django.db import models

class BloodDonor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'blood_donor'   # EXACT table name
        managed = False            # 🔥 VERY IMPORTANT

    def __str__(self):
        return self.name
