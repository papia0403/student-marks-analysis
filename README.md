# 🎓 Student Marks Analysis (Streamlit App)

## 📌 Project Overview
This is my first project built with **Python** and **Streamlit**.  
It is a simple web app that allows you to:
- Enter student names and marks
- Automatically calculate grades (A–F)
- Generate a class report (total, average, highest, lowest)
- Display results interactively in the browser

---

## 🚀 How to Run the App

### 1. Clone this repository
```bash
git clone https://github.com/YOUR-USERNAME/student-marks-analysis.git
cd student-marks-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
streamlit run student_marks_app.py
```

Then open the link provided (usually `http://localhost:8501`) in your browser.

---

## 📂 Project Structure
```
student-marks-analysis/
│── student_marks_app.py      # Main Streamlit app
│── requirements.txt          # Dependencies
│── README.md                 # Project documentation
│── sample_output.txt         # (Optional) Example program output
```

---

## 📸 Sample Output
Example run from console (before Streamlit version):
```
Student: papia khatun | Marks: 93 | Grade: A
Student: anuriya biswas | Marks: 78 | Grade: C
Student: isha bisal | Marks: 65 | Grade: C

Class Summary:
Total marks = 236
Average marks = 78.67
Highest = papia khatun (93)
Lowest = isha bisal (65)
```

---

## ✨ Future Improvements
- Add data visualization (charts/graphs)
- Save student results in a CSV/Database
- Deploy app to **Streamlit Cloud**

---
