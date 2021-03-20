def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Calculus', 'Algebra', 'chemistry', 'Art']
uniqueInfo = {'name': 'Jane', 'age':25}

student_info(*courses, **uniqueInfo)
