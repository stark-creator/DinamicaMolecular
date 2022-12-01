
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length = 200) #para almacenar un título
    uploadedFile = models.FileField(upload_to = "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True) #dice la fecha y hora de la carga



