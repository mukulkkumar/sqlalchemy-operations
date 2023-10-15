from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///student.db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

'''
Create table
'''
Base.metadata.create_all(engine)

'''
Insert data
'''
student_data = Student(name="Mukul", age="32", grade="First")
session.add(student_data)
session.commit()

'''
Read data
'''
# Get all the data
students = session.query(Student)

for student in students:
    print(student.name)

# Get data in order
students = session.query(Student).order_by(Student.name)

for student in students:
    print(student.name)


# Get data by filter
student = session.query(Student).filter(Student.name=="Mukul").first()
print(student.name, student.age)

# Get data by filter with or condition
students = session.query(Student).filter(or_(Student.name=="Mukul", Student.name=="Abhinash"))
for student in students:
    print(student.name, student.age)

# Get the count of data
student_count = session.query(Student).count()
print(f"The student count is {student_count}")

'''
Update data
'''
student = session.query(Student).filter(Student.name=="Mukul").first()
student.age = 31
session.commit()

'''
Delete data
'''
student = session.query(Student).filter(Student.name=="Abhinash").first()
session.delete(student)
session.commit()
