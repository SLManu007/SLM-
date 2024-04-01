from django.db import models

# Create your models here.
Branch_CHOICES = (
    ("ECE", "Electronics and Communication Engineering"),
    ("CSE", "Computer Science and Engineering"),
    ("IT", "Information Technology"),
    ("EEE", "Electrical and Electronic Engineering "),
    ("CE", "civil Engineering "),
    ("AIML", "Artifical Intelligence and Machine Learning"),
    ("DS", "Data Science"),
    ("CS", "CyberSecurity"),
)
class studentmodels(models.Model):
    Name = models.CharField(max_length=100)
    Hallticket = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    Branch = models.CharField(max_length=100,choices = Branch_CHOICES)
    CasteCategory = models.CharField(max_length=100)
    Fathername = models.CharField(max_length=1000)
    Mothername = models.CharField(max_length=100)
    aadhar = models.CharField(max_length=100)
   
    profileimg = models.ImageField()

    def __str__(self):
        return self.Hallticket  

    class Meta:
        db_table = 'studentmodels'
