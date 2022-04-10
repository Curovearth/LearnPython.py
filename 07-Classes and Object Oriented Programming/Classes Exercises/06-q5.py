# Define a Python function student(). Using function attributes display the names of all arguments.

def student(student_name, student_course, student_reg):
    return f'Student Name: {student_name}\nCourse: {student_course}\nReg: {student_reg}'    # F-strings or Literal String Interpolation much faster that other string formatting.

print(student('Swarup','Biomedical Instrumentation','0167'))
