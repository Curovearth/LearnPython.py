# Write a Python function student_data () which will print the id of a student (student_id). 
# If the user passes an argument student_name or student_class the function will print the student name and class.

def student_data(student_id,**kwargs):
    print(f'Student Id: {student_id}')

    # if 'student_class' or 'student_name' in kwargs:
    #     print(f"Student class: {kwargs['student_class']}")
    
    for i in kwargs:
        print(f'{str(i)}: {kwargs[i]}')


student_data(892984,student_class='TT414',student_name='swarupt')
