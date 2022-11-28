from django.db import models
import datetime
from datetime import timedelta

class Language(models.Model):
    name = models.CharField(max_length=50)
    month_to_learn = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Курс {self.name} продолжительностью {self.month_to_learn} месяцев успешно сохранен!')

    def get_gender(self):
        name_leng = str(self.name)
        if name_leng('java script'):
            name_l = 'Java Script'
        return name_l

    def __str__(self):
        return self.name

class AbstractPerson(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Студент {self.name} с {self.phone_number} успешно сохранен!')

    def get_phone_number(self):
        phone_number_gen = str(self.phone_number)
        if phone_number_gen.startswith('0'):
            number = f'+996{self.phone_number}'
        return number


    def __str__(self):
        return self.name

class Student(AbstractPerson):
    os_choices = [('w', 'windows'),
                  ('m', 'macOS'),
                  ('l', 'linux')]
    work_study_place = models.CharField(max_length=50, null=True)
    has_own_notebook = models.BooleanField()
    preferred_os = models.CharField(max_length=1, choices= os_choices)

class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=50, null=True)
    experience = models.DateField()
    student = models.ManyToManyField(Student, through="Course")

    def __str__(self):
        return self.main_work

class Course(models.Model):
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def get_end_date(self):
        days = self.months * 30
        date = datetime.datetime.now() + datetime.timedelta(days=days)
        return date.strftime('%d.%m.%Y')



