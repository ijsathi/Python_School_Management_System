from school import School
from person import Student, Teacher
from subject import Subject
from classRoom import ClassRoom

school = School("ABC", "Dhaka")

# adding classroom
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# adding student 
rahim = Student("Rahim", eight)
karim = Student("Karim", nine)
lily = Student("Lily", ten)
maschura = Student("Maschura", ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(lily)
school.student_admission(maschura)

# adding teacher
abul = Teacher("Abul Akon")
jadob = Teacher("Jadob shikdar")
kakuli = Teacher("Kakuli")
kabul = Teacher("Kabul khan")

# adding subject
bangla = Subject("Bangla", kabul)
english = Subject("English", jadob)
physics = Subject("Physics", abul)
ict = Subject("ICT", kakuli)

eight.add_subject(bangla)
eight.add_subject(english)
eight.add_subject(ict)
nine.add_subject(bangla)
nine.add_subject(ict)
nine.add_subject(english)
nine.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(ict)
ten.add_subject(english)
ten.add_subject(physics)

ten.take_semester_final_exam()

print(school)