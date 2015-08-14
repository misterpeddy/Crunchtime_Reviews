from django.db import models
from .statics import SESSION_STATUS
from datetime import datetime

class Session(models.Model):
	course = models.ForeignKey('Course')
	date = models.DateField()
	instructor = models.ForeignKey('Instructor')
	location = models.CharField(max_length=40, null=True)
	present = models.IntegerField(null=True)
	status = models.CharField(max_length='5', choices=SESSION_STATUS, default=SESSION_STATUS[0])
	rating = models.FloatField( default=0.0)
	rating_num = models.IntegerField(default=0)

	def __str__(self):
		return "Session taught by %s for %s" % (self.instructor.name, self.course.name)

	class Meta:
		ordering = ['-date']

class Course(models.Model):
	name = models.CharField(max_length=30)
	code = models.CharField(max_length=10)

	def __str__(self):
		return "Course %s: %s" % (self.code, self.name)

class Instructor(models.Model):
	student_id = models.CharField(max_length=10)
	name = models.CharField(max_length=30)
	date_joined = models.DateField(default=datetime.now)
	courses = models.ManyToManyField('Course')
	rating = models.FloatField( default=0.0)
	rating_num = models.IntegerField(default=0)

	def __str__(self):
		return "Instructor %s(%s) teaching %s with rating %s" % (self.student_id,self.name, self.courses.all(),self.rating)

class Video(models.Model):
	course = models.ForeignKey('Course')
	title = models.CharField(max_length=50)
	description = models.TextField(default=None)
	unit = models.CharField(max_length=30, default="Miscellaneous")
	section = models.CharField(max_length=30)
	video_url = models.CharField(max_length=100)
	picture_url = models.CharField(max_length=100)

	def __str__(self):
		return "%s for %s(%s - %s)" % (self.title, self.course, self.unit, self.section)

	class Meta:
		ordering= ['unit', 'title']

class Request(models.Model):
	course = models.ForeignKey('Course')
	student_id = models.CharField(max_length=10)
	date = models.DateField()
	description = models.TextField(default=None)
	note = models.TextField(default=None)

	def __str__(self):
		return "Request by %s for %s " % (self.student_id, self.course)