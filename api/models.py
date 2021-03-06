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
    first_name = StringField(db_column='name')
    last_name = StringField(db_column='surname')
    personal_number = models.IntegerField(db_column='pers_number')
    url = LongStringField()

    _degrees_before = StringField(db_column='title_before')
    _degrees_after = StringField(db_column='title_behind')

    def _no_nbsp(self, f):
        field = getattr(self, f)
        return field if field != '&nbsp;' else None

    @property
    def degrees_before(self):
        return self._no_nbsp('_degrees_before')

    @property
    def degrees_after(self):
        return self._no_nbsp('_degrees_after')

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
    semester = TinyStringField()
    registration_date = models.DateTimeField()
    tour = models.BooleanField()
    course = models.ForeignKey(Course, db_column='utvs')

    _kos_course_code = ShortStringField(db_column='kos_kod')
    _kos_code_flag = models.BooleanField(db_column='kos_code')

    @property
    def kos_course_code(self):
        return self._kos_course_code if self._kos_code_flag else None

    class Meta:
        db_table = 'v_students'
