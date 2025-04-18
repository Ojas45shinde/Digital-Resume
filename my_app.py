import streamlit as st
from pathlib import Path
from streamlit_option_menu import option_menu
from PIL import Image

current_dir=Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file=Path(r"C:/Users/acer/Desktop/digital resume/styles/main.css")
result=current_dir/"assests"/"Ojas resume.pdf"
profile_pic=current_dir/"assests"/"me.jpg"

print("css file path",css_file)

page_title=" My digital resume"
page_icon=":👋:"
name="Ojas Shinde"
description="Hello there, I'm Ojas Shinde. Computer Engineer student with knowlegde" \
" in Data Science and Machine Learning"
email="ojasshinde45@gmail.com"
socials={
    "linkedIn":"https://www.linkedin.com/in/ojas-shinde-9172b8257",
    "instagram":"https://www.instagram.com/ojas_shinde_8",
    "github":"https://github.com/Ojas45shinde"

}
projects={
    "SVM Model": "SVM Model ",
    "Recommender System": "Movie Recommender System",
    "Data Analysis":"Adidas vs Nike Analysis"
}

st.set_page_config(page_title=page_title,page_icon=page_icon)

st.title("Hello Everyone!!")

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(result,'rb') as pdf_file:
    PDFbyte=pdf_file.read()

profile_pic=Image.open(profile_pic)

st.markdown(
    """
    <div class="fixed-name">Ojas Shinde</div>
    """,
    unsafe_allow_html=True
)



# hero section

col1,col2=st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=440)

with col2:
    #st.title(name)
    st.write(description)
    st.download_button(
        label="📄 Download My Resume",
        data=PDFbyte,
        file_name=result.name,
        mime="application/octet-stream"
    )
    st.write("My Email:",email)    




st.write("#")
cols=st.columns(len(socials))
for index,(platform,link) in enumerate(socials.items()):
    cols[index].write("My "+f"[{platform}]({link})")


# About Me
st.write("---")
st.subheader("About Me")
st.markdown(
    """
    <div class="card">
        <p>I am a Computer Engineering student passionate about Data Science, Machine Learning, and building intelligent systems. I enjoy solving real-world problems using data and code.</p>
    </div>
    """, unsafe_allow_html=True
)

# Education Timeline
st.write("---")
st.subheader("🎓 Education")
st.markdown(
    """
    <div class="card">
        <ul>
            <li><strong>Bachelor of Engineering in Computer</strong> – JSPM University (2022 - Present)</li>
            <li><strong>HSC (12th Grade)</strong> – Bharat Jr. College (2019 - 2021)</li>
            <li><strong>SSC (10th Grade)</strong> – SS English Medium School (2010 - 2019)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True
)

# Experience & Skills Cards
st.write("---")
st.subheader("📌 Quick Highlights")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="card">
            <h4>Experience</h4>
            <ul>
                <li>Internship at Internship Studio</li>
                <li>Virtual Internship @ Quantium</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown(
        """
        <div class="card">
            <h4>Skills</h4>
            <ul>
                <li>Python, SQL, C++</li>
                <li>Data Preprocessing</li>
                <li>Data Analysis</li>
                <li>Machine Learning</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with col3:
    project_items = "".join([f"<li>{proj}</li>" for proj in projects.keys()])
    st.markdown(
        f"""
        <div class="card">
            <h4>Projects</h4>
            <ul>
                {project_items}
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Certifications
st.write("---")
st.subheader("📜 Certifications")
st.markdown(
    """
    <div class="card">
        <ul>
            <li>Python for Data Science – Coursera</li>
            <li>Machine Learning – IBM</li>
            <li>SQL for Beginners – Udemy</li>
        </ul>
    </div>
    """, unsafe_allow_html=True
)

# Contact Form
st.write("---")
st.subheader("📬 Contact Me")

contact_form = """
<form action="https://formsubmit.co/ojasshinde@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Hide default form submit message (optional)
st.markdown(
    """
    <style>
        input, textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin-top: 10px;
            margin-bottom: 10px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 8px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# Thank You Section
st.write("---")
st.markdown(
    """
    <div class="card" style="text-align: center;">
        <h2>🙌 Thank You for Visiting!</h2>
        <p>I appreciate you taking the time to explore my digital resume. Let's connect and collaborate!</p>
        <p style="font-size: 22px;">– Ojas Shinde</p>
    </div>
    """, unsafe_allow_html=True
)





#hiding footer and header too
hide_st_style="""
            <style>
            #MainMenu {visibility :hidden;}
            footer {visibility :hidden;}
            </style>
            """
st.markdown(hide_st_style,unsafe_allow_html=True)

