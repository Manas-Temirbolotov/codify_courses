leng = Language(name='Python', month_to_learn = '6')
leng.save()
leng1 = Language(name='Java Script', month_to_learn = '6')
leng1.save()
leng2 = Language(name='UX-UI', month_to_learn = '2')
leng2.save()

stud = Student.objects.create(name = 'Amanov Aman', email = 'aman@mail.ru', phone_number = '+996700989898', work_study_place = 'School №13', has_own_notebook = True, preferred_os = 'w')







mentor_1 = Mentor.objects.create(name='Ilona Maskova',email='imask@gmail.com',phone_number='0500545454',
                                 main_work=None,experience=datetime.date(year=2021, month=10, day=23))

mentor_2 = Mentor.objects.create(name='Halil Nurmuhametov',email='halil@gmail.com',phone_number='0709989876',
                                 main_work='University of Fort Collins',experience=datetime.date(year=2010, month=9, day=18))