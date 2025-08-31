import streamlit as st

st.title("🎓 Student Marks Analysis")

# Function to assign grade
def grade_student(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks > 40:
        return "D"
    else:
        return "F"

# Input: number of students
num_students = st.number_input("Enter number of students:", min_value=1, step=1)

student_data = {}

for i in range(num_students):
    name = st.text_input(f"Enter name of student {i+1}", key=f"name{i}")
    marks = st.number_input(f"Enter marks for {name}", min_value=0, max_value=100, step=1, key=f"marks{i}")
    if name:
        student_data[name] = marks

# Button to generate report
if st.button("Generate Report") and student_data:
    total_marks = sum(student_data.values())
    average_marks = total_marks / len(student_data)
    highest_student = max(student_data, key=student_data.get)
    lowest_student = min(student_data, key=student_data.get)

    st.subheader("📊 Student Reports")
    for name, marks in student_data.items():
        st.write(f"**{name}**: Marks = {marks}, Grade = {grade_student(marks)}")

    st.subheader("📌 Class Summary")
    st.write(f"Total marks of the class: {total_marks}")
    st.write(f"Average marks of the class: {average_marks:.2f}")
    st.write(f"Highest marks: {highest_student} ({student_data[highest_student]} marks)")
    st.write(f"Lowest marks: {lowest_student} ({student_data[lowest_student]} marks)")
