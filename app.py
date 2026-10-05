import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="ScholarAI - Student Learning Assistant",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }

    .title {
        font-size: 42px;
        font-weight: bold;
        color: #4F46E5;
        text-align: center;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #555;
        margin-bottom: 30px;
    }

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    .feature-title {
        font-size: 22px;
        font-weight: bold;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
st.sidebar.title("🎓 ScholarAI")

st.sidebar.write("AI Student Learning Assistant")

menu = st.sidebar.radio(
    "Choose a Feature",
    [
        "🏠 Home",
        "🤖 Academic AI",
        "📝 Notes Generator",
        "❓ Quiz Generator",
        "🔄 Revision Notes",
        "🧠 Mind Map",
        "💻 Coding Assistant",
        "📚 Assignment Helper"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "ScholarAI helps students learn, revise, practice and understand academic topics."
)


# ---------------- HOME ----------------
if menu == "🏠 Home":

    st.markdown(
        '<div class="title">🎓 ScholarAI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">AI Student Learning Assistant</div>',
        unsafe_allow_html=True
    )

    st.write("### Welcome to ScholarAI 👋")

    st.write(
        "ScholarAI is an AI-powered learning platform designed specially "
        "for students. Learn concepts, create notes, practice quizzes, "
        "generate revision material and get coding help."
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            '<div class="card">'
            '<div class="feature-title">🤖 Academic AI</div>'
            '<p>Ask questions and understand difficult academic concepts.</p>'
            '</div>',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div class="card">'
            '<div class="feature-title">📝 Smart Notes</div>'
            '<p>Generate simple and organized notes from any topic.</p>'
            '</div>',
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            '<div class="card">'
            '<div class="feature-title">❓ Quiz Practice</div>'
            '<p>Practice MCQs and test your knowledge.</p>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown("### 📚 What can you learn?")

    subjects = [
        "💻 Programming",
        "📊 Data Structures",
        "🗄️ DBMS",
        "🌐 Web Development",
        "🧮 Mathematics",
        "⚙️ Computer Networks",
        "🏗️ Software Engineering",
        "🖥️ Computer Architecture"
    ]

    cols = st.columns(4)

    for i, subject in enumerate(subjects):
        with cols[i % 4]:
            st.button(subject, use_container_width=True)


# ---------------- ACADEMIC AI ----------------
elif menu == "🤖 Academic AI":

    st.title("🤖 Academic AI")

    st.write(
        "Ask ScholarAI any academic question and get a simple explanation."
    )

    question = st.text_area(
        "Enter your question:",
        placeholder="Example: Explain Operating System in simple words"
    )

    level = st.selectbox(
        "Select your academic level:",
        ["Intermediate", "Degree", "B.Tech"]
    )

    if st.button("✨ Ask ScholarAI"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:
            st.success("ScholarAI is preparing your answer...")

            st.markdown("### 📖 Answer")

            st.write(
                f"""
                **Academic Level:** {level}

                **Topic:** {question}

                ### Simple Explanation

                This is a demo response from ScholarAI.

                ScholarAI will explain the topic in simple language,
                provide important points, examples and key concepts.

                ### 📌 Important Points

                - Understand the basic concept
                - Learn the important terminology
                - Study with real-world examples
                - Practice questions after learning

                ### 🎯 Exam Tip

                Remember the definition, important points and one
                suitable example for your examination.
                """
            )


# ---------------- NOTES GENERATOR ----------------
elif menu == "📝 Notes Generator":

    st.title("📝 AI Notes Generator")

    topic = st.text_input(
        "Enter the topic:",
        placeholder="Example: Python Basics"
    )

    note_type = st.selectbox(
        "Select notes type:",
        [
            "Short Notes",
            "Detailed Notes",
            "5 Marks Answer",
            "10 Marks Answer",
            "Exam Revision Notes"
        ]
    )

    if st.button("📝 Generate Notes"):

        if topic == "":
            st.warning("Please enter a topic.")

        else:

            st.success("Notes generated successfully!")

            st.markdown(f"## 📚 {topic}")

            st.markdown(f"""
### Definition

{topic} is an important concept that students should understand
with its basic principles, applications and examples.

### Key Points

1. Understand the basic concept.
2. Learn important terminology.
3. Study practical examples.
4. Understand its applications.
5. Practice questions related to the topic.

### Advantages

- Easy to understand
- Useful for examinations
- Helps in quick revision
- Improves conceptual knowledge

### Conclusion

Understanding **{topic}** helps students build strong academic
knowledge and prepare effectively for examinations.
""")


# ---------------- QUIZ ----------------
elif menu == "❓ Quiz Generator":

    st.title("❓ AI Quiz Generator")

    topic = st.text_input(
        "Enter quiz topic:",
        placeholder="Example: Python"
    )

    number = st.slider(
        "Number of questions",
        1,
        10,
        5
    )

    if st.button("🎯 Generate Quiz"):

        if topic == "":
            st.warning("Please enter a topic.")

        else:

            st.success(f"{number} questions generated!")

            for i in range(1, number + 1):

                st.markdown(f"### Question {i}")

                st.write(
                    f"Which of the following is related to **{topic}**?"
                )

                answer = st.radio(
                    "Choose your answer:",
                    [
                        "Option A",
                        "Option B",
                        "Option C",
                        "Option D"
                    ],
                    key=f"question_{i}"
                )


# ---------------- REVISION NOTES ----------------
elif menu == "🔄 Revision Notes":

    st.title("🔄 Smart Revision Notes")

    topic = st.text_input(
        "Enter topic for revision:",
        placeholder="Example: Computer Networks"
    )

    if st.button("⚡ Create Revision Notes"):

        if topic == "":
            st.warning("Please enter a topic.")

        else:

            st.markdown(f"## ⚡ Quick Revision: {topic}")

            st.markdown("""
### 🔑 Remember

- Definition
- Important concepts
- Key components
- Advantages
- Disadvantages
- Applications

### 📌 Exam Focus

Focus on definitions, diagrams, important differences,
advantages/disadvantages and real-world applications.

### 🧠 Quick Tip

Revise the topic once, close your notes and try explaining
the concept in your own words.
""")


# ---------------- MIND MAP ----------------
elif menu == "🧠 Mind Map":

    st.title("🧠 AI Mind Map")

    topic = st.text_input(
        "Enter topic:",
        placeholder="Example: Artificial Intelligence"
    )

    if st.button("🧠 Create Mind Map"):

        if topic == "":
            st.warning("Please enter a topic.")

        else:

            st.success("Mind map structure created!")

            st.markdown(f"""
## 🧠 {topic}

**{topic}**
            
├── 📖 Definition  
├── 🔑 Key Concepts  
├── ⚙️ Components  
├── 💡 Applications  
├── ✅ Advantages  
├── ❌ Disadvantages  
└── 🎯 Examples
""")


# ---------------- CODING ASSISTANT ----------------
elif menu == "💻 Coding Assistant":

    st.title("💻 ScholarAI Coding Assistant")

    language = st.selectbox(
        "Select Programming Language:",
        [
            "Python",
            "C",
            "C++",
            "Java",
            "JavaScript",
            "SQL"
        ]
    )

    problem = st.text_area(
        "Describe your coding problem:",
        placeholder="Example: Write a program to find factorial"
    )

    if st.button("💻 Generate Code"):

        if problem == "":
            st.warning("Please enter a coding problem.")

        else:

            st.success("Code generated!")

            st.markdown(
                f"### {language} Solution"
            )

            st.code(
                f"""# ScholarAI Demo

# Programming Language: {language}
# Problem: {problem}

print("This is a demo coding solution")
""",
                language.lower()
            )

            st.info(
                "💡 The complete AI version can connect an LLM API "
                "to generate real solutions."
            )


# ---------------- ASSIGNMENT ----------------
elif menu == "📚 Assignment Helper":

    st.title("📚 Assignment Helper")

    subject = st.text_input(
        "Subject:",
        placeholder="Example: Software Engineering"
    )

    question = st.text_area(
        "Assignment Question:",
        placeholder="Enter your assignment question..."
    )

    marks = st.selectbox(
        "Marks:",
        ["2 Marks", "5 Marks", "10 Marks", "15 Marks"]
    )

    if st.button("📚 Generate Assignment Answer"):

        if subject == "" or question == "":
            st.warning("Please enter subject and question.")

        else:

            st.success("Assignment answer prepared!")

            st.markdown("### 📖 Answer")

            st.write(
                f"""
                **Subject:** {subject}

                **Question:** {question}

                **Marks:** {marks}
                """
            )

            st.markdown("""
### Introduction

This topic is an important part of the subject.
The concept can be understood by studying its
definition, main components and applications.

### Main Explanation

The answer should contain the important concepts,
examples and relevant points required for the selected
marks.

### Conclusion

Therefore, understanding this concept helps students
develop strong academic knowledge and perform better
in examinations.
""")
