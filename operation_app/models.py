from django.db import models
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Complaint(models.Model):
    profile_id = models.PositiveIntegerField()
    subject = models.CharField(max_length=20)
    current_handler = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    priority_id = models.PositiveIntegerField()

    class Meta:
        db_table = 'complaint'


class ComplaintMessage(models.Model):
    profile_id = models.IntegerField()
    message = models.CharField(max_length=255)
    media = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'complaint_message'


class ComplaintStatus(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'complaint_status'


class Department(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'department'


class Designation(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'designation'


class Priority(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'priority'


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    profile_type_id = models.PositiveIntegerField()
    designation_id = models.PositiveIntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()


    class Meta:
         db_table = 'profile'


class ProfileType(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'profile_type'