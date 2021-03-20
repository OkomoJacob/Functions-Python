def student_info(*args, **kwargs): #To accept arbitrary positional args
    print(args)
    print(kwargs)

courses = ['Math', 'Calculus', 'Algebra', 'chemistry', 'Art']
uniqueInfo = {'name': 'Jane', 'age':25}

student_info(*courses, **uniqueInfo) #*, ** to unpack the values
