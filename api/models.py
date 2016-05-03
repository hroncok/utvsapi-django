from django.db import models

from .fields import string_filed


StringField = string_filed(50)
LongStringField = string_filed(250)
ShortStringField = string_filed(20)
TinyStringField = string_filed(10)


class Destination(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='id_destination')
    name = StringField()
    url = LongStringField()

    class Meta:
        db_table = 'v_destination'


class Hall(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='id_hall')
    name = StringField()
    url = LongStringField()

    class Meta:
        db_table = 'v_hall'


class Teacher(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='id_lector')
    degrees_before = StringField(db_column='title_before')
    first_name = StringField(db_column='name')
    last_name = StringField(db_column='surname')
    degrees_after = StringField(db_column='title_behind')
    personal_number = models.IntegerField(db_column='pers_number')
    url = LongStringField()

    class Meta:
        db_table = 'v_lectors'


class Sport(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='id_sport')
    shortcut = StringField(db_column='short')
    name = StringField(db_column='sport')
    description = models.TextField()

    class Meta:
        db_table = 'v_sports'


class Course(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='id_subjects')
    shortcut = StringField()
    day = models.SmallIntegerField()
    starts_at = TinyStringField(db_column='begin')
    ends_at = TinyStringField(db_column='end')
    notice = models.TextField()
    semester = models.SmallIntegerField()
    sport = models.ForeignKey(Sport, db_column='sport')
    hall = models.ForeignKey(Hall, db_column='hall')
    teacher = models.ForeignKey(Teacher, db_column='lector')

    class Meta:
        db_table = 'v_subjects'


class Enrollment(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='id_student')
    personal_number = models.IntegerField()
    kos_course_code = ShortStringField(db_column='kos_kod')
    semester = TinyStringField()
    registration_date = models.DateTimeField()
    tour = models.BooleanField()
    _kos_code_flag = models.BooleanField(db_column='kos_code')
    course = models.ForeignKey(Teacher, db_column='utvs')

    class Meta:
        db_table = 'v_students'
