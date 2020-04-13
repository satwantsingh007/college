from django.db import models

class Studentregister(models.Model):
    name = models.CharField(max_length=60)
    contact = models.IntegerField()
    email = models.EmailField(max_length=30,primary_key=True)
    department = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Facultyregister(models.Model):
    name = models.CharField(max_length=60)
    contact = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField(max_length=30,primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=60)
    size = models.DecimalField(decimal_places=4,max_digits=10)

    def __str__(self):
        return self.name

class Document(models.Model):
    name = models.CharField(max_length=60)
    documentformat = models.CharField(max_length=50)
    size = models.DecimalField(decimal_places=4,max_digits=10)

    def __str__(self):
        return self.name

class Report(models.Model):
    name = models.CharField(max_length=50)
    report = models.CharField(max_length=10000)

    def __str__(self):
        return self.name