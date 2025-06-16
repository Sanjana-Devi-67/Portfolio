import streamlit as st
from PIL import Image
import base64
from streamlit_lottie import st_lottie
import json

# Page Config
st.set_page_config(page_title="Sanjana Devi | Portfolio", layout="wide")

# Load Assets
profile_pic = Image.open("assets/sanjana_photo.jpg")
resume_file = "Sanjana_1page_resume.pdf"

# Load Lottie Animations
def load_lottie(filepath):
    with open(filepath, "r", encoding="latin-1") as f:
        return json.load(f)


lottie_dev = load_lottie("assets/developer.json")
lottie_skills = load_lottie("assets/skills.json")
lottie_proj = load_lottie("assets/projects.json")

# Background Styling
def set_background(path):
    with open(path, "rb") as img:
        b64 = base64.b64encode(img.read()).decode()
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{b64}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }}
    .section-title {{
        font-size: 36px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 20px;
        border-bottom: 2px solid white;
        padding-bottom: 5px;
    }}
    footer {{
        text-align: center;
        font-size: 14px;
        padding: 10px;
        color: #ccc;
    }}
    .dropdown {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

set_background("assets/background.png")


# Simulated Navbar
st.markdown("""
<div style='text-align: center; background-color: rgba(0,0,0,0.6); padding: 12px; border-radius: 12px; position: sticky; top: 0; z-index: 999;'>
    <a href="#about" style="margin: 15px; font-weight: bold; color: white; text-decoration: none;">About</a>
    <a href="#skills" style="margin: 15px; font-weight: bold; color: white; text-decoration: none;">Skills</a>
    <a href="#projects" style="margin: 15px; font-weight: bold; color: white; text-decoration: none;">Projects</a>
    <a href="#experience" style="margin: 15px; font-weight: bold; color: white; text-decoration: none;">Experience</a>
    <a href="#contact" style="margin: 15px; font-weight: bold; color: white; text-decoration: none;">Contact</a>
</div>
""", unsafe_allow_html=True)



#sidebar
st.markdown("""
<style>

/* Profile image */
.sidebar-img {
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    margin-bottom: 15px;
}

/* Links hover effect */
.sidebar a {
    text-decoration: none;
    font-weight: bold;
    color: #1abc9c;
    position: relative;
}

.sidebar a::after {
    content: "";
    position: absolute;
    width: 0%;
    height: 2px;
    bottom: -2px;
    left: 0;
    background-color: #1abc9c;
    transition: width 0.3s;
}

.sidebar a:hover::after {
    width: 100%;
}

/* Resume button */
button[data-testid="baseButton"] {
    background-color: #1abc9c !important;
    color: white !important;
    font-weight: bold;
    border-radius: 8px;
    transition: transform 0.2s ease;
}

button[data-testid="baseButton"]:hover {
    transform: scale(1.05);
    box-shadow: 0 0 10px #1abc9c88;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image(profile_pic, width=940, output_format="auto")  # Make sure profile_pic is loaded earlier
    st.markdown('<div class="sidebar">', unsafe_allow_html=True)
    st.title("V Sanjana Devi")
    st.write("📍 Bengaluru, India")
    st.write("📧 sanjanadevi.vksy@gmail.com")
    st.write("📱 +91 9590152776")
    st.markdown('[LinkedIn](https://www.linkedin.com/in/sanjana-devi-5712a130a/)', unsafe_allow_html=True)
    st.markdown('[GitHub](https://github.com/Sanjana-Devi-67)', unsafe_allow_html=True)
    with open("Sanjana_1page_resume.pdf", "rb") as file:
        resume_bytes = file.read()
    st.download_button(
        label="📄 My Resume",
        data=resume_bytes,
        file_name="Sanjana_Resume.pdf",
        mime="application/pdf"
    )
    st.markdown('</div>', unsafe_allow_html=True)
# ABOUT SECTION
st.markdown('<h3 id="about" class="section-title">👩‍💻 About Me</h3>', unsafe_allow_html=True)
st_lottie(lottie_dev, height=50, key="dev")

# About Me Card Box
st.markdown("""
<div style="
    background: rgba(0, 0, 0, 0.45);
    backdrop-filter: blur(6px);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 0 12px rgba(0,0,0,0.25);
    font-size: 17px;
    line-height: 1.65;
    color: #eee;
">

<b>Hello! I'm Sanjana Devi</b>, an enthusiastic Information Science Engineering student with a strong passion for building full-stack web applications and solving real-world problems through technology.

I specialize in crafting seamless, data-driven user experiences — from designing e-commerce platforms to integrating cutting-edge technologies like <b>blockchain</b> and <b>AI</b> into finance systems. I love transforming ideas into elegant, scalable, and functional products.

With a solid foundation in <b>data structures</b>, <b>algorithms</b>, and modern <b>web technologies</b>, I aim to join a forward-thinking team where creativity meets engineering. I’m driven by curiosity, collaboration, and a desire to make technology more meaningful and accessible 🚀

<!-- Highlight Tags -->
<div style="margin-top: 20px;">
  <span style="background: rgba(0, 0, 0, 0.45);backdrop-filter: blur(6px); color:white; padding:6px 14px; border-radius:20px; margin:6px; display:inline-block;">💻 Full Stack Developer</span>
  <span style="background: rgba(0, 0, 0, 0.45);backdrop-filter: blur(6px); color:white; padding:6px 14px; border-radius:20px; margin:6px; display:inline-block;">📊 Data Enthusiast</span>
  <span style="background: rgba(0, 0, 0, 0.45);backdrop-filter: blur(6px); color:white; padding:6px 14px; border-radius:20px; margin:6px; display:inline-block;">🚀 Problem Solver</span>
</div> 
<!-- Motivational Quote -->
<p style="font-style: italic; color: #ccc; margin-top: 25px; text-align: center;">
  “Code is not just instructions — it's how I turn ideas into experiences.”
</p>

<!-- Call to Action -->
<div style="margin-top: 20px; padding: 12px; background-color: rgba(26,188,156,0.1); border-left: 4px solid #1abc9c;">
  <b>Currently open to internships and exciting collaborations in software development, AI, or product design. Let’s build something amazing together!</b>
</div>

</div>
""", unsafe_allow_html=True)




# --- SKILLS SECTION ---
st.markdown('<h3 id="skills" class="section-title">🛠️ Skills</h3>', unsafe_allow_html=True)
st_lottie(lottie_skills, height=50, key="skills")

# --- Custom CSS for Badges ---
st.markdown("""
<style>
.skill-block {
    background-color: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 12px;
    margin: 15px 10px 30px 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}
.skill-category {
    font-size: 18px;
    font-weight: 600;
    margin: 15px 0 8px;
    color: #1abc9c;
    display: flex;
    align-items: center;
    gap: 10px;
}
.skill-badge {
    display: inline-block;
    background: rgba(0, 0, 0, 0.45);
    backdrop-filter: blur(6px);
    color: #eee;
    padding: 6px 14px;
    border-radius: 25px;
    font-size: 13px;
    margin: 6px 6px 6px 0;
    transition: all 0.3s ease;
    border: 1px solid transparent;
}
.skill-badge:hover {
    background-color: rgba(26, 188, 156, 0.2);
    color: #1abc9c;
    border: 1px solid #1abc9c;
}
</style>
""", unsafe_allow_html=True)


# --- Three-Column Layout ---
cols = st.columns(3)

# Column 1
with cols[0]:
    st.markdown("<div class='skill-block'>", unsafe_allow_html=True)
    st.markdown("<div class='skill-category'>👩‍💻 Languages & DSA</div>", unsafe_allow_html=True)
    st.markdown("<span class='skill-badge'>C</span><span class='skill-badge'>Python</span><span class='skill-badge'>Java</span><span class='skill-badge'>DSA (Java)</span>", unsafe_allow_html=True)

    st.markdown("<div class='skill-category'>💻 OS & Web</div>", unsafe_allow_html=True)
    st.markdown("<span class='skill-badge'>Ubuntu</span><span class='skill-badge'>Windows</span><span class='skill-badge'>HTML</span><span class='skill-badge'>CSS</span><span class='skill-badge'>JavaScript</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Column 2
with cols[1]:
    st.markdown("<div class='skill-block'>", unsafe_allow_html=True)
    st.markdown("<div class='skill-category'>⚙️ Frameworks & Libraries</div>", unsafe_allow_html=True)
    st.markdown("<span class='skill-badge'>Node.js</span><span class='skill-badge'>Express.js</span><span class='skill-badge'>Bootstrap</span><span class='skill-badge'>React.js</span><span class='skill-badge'>Flask</span><span class='skill-badge'>EJS</span>", unsafe_allow_html=True)

    st.markdown("<div class='skill-category'>🛢️ Databases</div>", unsafe_allow_html=True)
    st.markdown("<span class='skill-badge'>MySQL</span><span class='skill-badge'>MongoDB</span><span class='skill-badge'>MongoDB Atlas</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Column 3
with cols[2]:
    st.markdown("<div class='skill-block'>", unsafe_allow_html=True)
    st.markdown("<div class='skill-category'>🛠️ Tools & Platforms</div>", unsafe_allow_html=True)
    st.markdown("<span class='skill-badge'>VS Code</span><span class='skill-badge'>Eclipse</span><span class='skill-badge'>Jupyter Notebook</span><span class='skill-badge'>LaTeX</span><span class='skill-badge'>Power BI</span><span class='skill-badge'>Render</span>", unsafe_allow_html=True)

    st.markdown("<div class='skill-category'>🔧 DevOps & Versioning</div>", unsafe_allow_html=True)
    st.markdown("<span class='skill-badge'>Git</span><span class='skill-badge'>GitHub</span><span class='skill-badge'>Maven</span><span class='skill-badge'>Gradle</span><span class='skill-badge'>Jenkins</span><span class='skill-badge'>Azure Pipelines (Basics)</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)



# PROJECTS SECTION
st.markdown('<h3 id="projects" class="section-title">🚀 Projects</h3>', unsafe_allow_html=True)
st_lottie(lottie_proj, height=50, key="projects")

project_data = [
    {
        "title": " Chimudra Fee Tracker - Secure Fee Management System  ",
        "desc": "Developed a role-based fee tracking system with JWT authentication for Chimudra Academy, enabling admin-student login, batch-wise payment management, and automated fee alerts via a secure dashboard..",
        "tech": "Node.js, Express.js, MongoDB, EJS, JWT, JavaScript, HTML, CSS",
        "github": "https://github.com/Sanjana-Devi-67/Chimudra-fee-tracker"
    },
    {
        "title": "Mobile Accessories Web App",
        "desc": "E-commerce platform for mobile accessories featuring login, cart functionality, and interactive store locator using Mapbox. Built with dynamic routes, session-based authentication, and responsive UI for seamless user experience.",
        "tech": "HTML, CSS, JavaScript, Node.js, Express.js, MongoDB, Mapbox API ",
        "github": "https://github.com/Sanjana-Devi-67/Mobile-accessories-web-application"
    },
    {
        "title": "Used Cloth Processing & Management System",
        "desc": "A dynamic NGO inventory system using Flask with secure login, AJAX-based form submission, and SQLite for persistent donor and cloth record management.",
        "tech": "Python (Flask), HTML, CSS, JavaScript, AJAX, REST API",
        "github": "https://github.com/yourusername/chimudra-fee-tracker"
    },
    {
        "title": "Wanderlust - Rental Service",
        "desc": "Full-stack rental booking platform with secure login, interactive map views, and a user review system. Built using MVC architecture, session middleware",
        "tech": "Node.js, Express.js, MongoDB Atlas, MapBox-API, Render, MVC",
        "github": "https://github.com/Sanjana-Devi-67/Wanderlust-Website"
    },
]

for i in range(0, len(project_data), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(project_data):
            proj = project_data[i + j]
            with cols[j]:
                st.markdown(f"""
    <style>
        .project-card {{
            background: rgba(0, 0, 0, 0.45);
            backdrop-filter: blur(6px);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.4);
            transition: all 0.3s ease;
            margin-bottom: 20px;
            height: 100%;
        }}

        .project-card:hover {{
              transform: scale(1.02);
               box-shadow: 0 0 25px rgba(26,188,156,0.6);
              background: rgba(0, 0, 0, 0.55);
        }}
    </style>

    <div class="project-card">
        <h4 style="text-align:center;">{proj['title']}</h4>
        <p style="font-size:14px;">{proj['desc']}</p>
        <p style="font-size:13px; color:#ccc;"><strong>Tech:</strong> {proj['tech']}</p>
        <a href="{proj['github']}" target="_blank" style="color:#1abc9c; font-weight:bold; text-decoration:none;">🔗 GitHub Repo</a>
    </div>
""", unsafe_allow_html=True)

# EXPERIENCE SECTION
st.markdown('<h3 id="experience" class="section-title">🏆 Experience</h3>', unsafe_allow_html=True)
st.markdown("""
<style>
.hover-card {
    background: rgba(0, 0, 0, 0.45);
    backdrop-filter: blur(6px);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 0 12px rgba(0,0,0,0.25);
    font-size: 17px;
    line-height: 1.65;
    color: #eee;
    margin-top: 30px;
    transition: all 0.3s ease;
}

.hover-card:hover {
    transform: scale(1.02);
    box-shadow: 0 0 25px rgba(26,188,156,0.6);
    background: rgba(0, 0, 0, 0.55);
}
</style>

<div class="hover-card">
- 🚀 Participated in <b>Full Stack Hackathon</b> @ CMRIT <br>  
- 💼 Developed real-world applications like <b>Fee Management System</b> and <b>Wanderlust</b>  <br>
- 🧠 Completed <b>Full Stack Web Development</b> & <b>DSA with Java</b> certifications  <br>
- 🎨 <b>Designer @ NSS CMRIT</b> – Designed promotional posters for NSS events using Canva  
</div>
""", unsafe_allow_html=True)


# --- CONTACT SECTION ---
st.markdown('<h3 id="contact" class="section-title">📬 Contact </h3>', unsafe_allow_html=True)

# Subheading
st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <p style="font-size:18px; color: #ccc;">
        Have a question, a project idea, or just want to say hello? <br>
        Feel free to drop a message — I’d love to hear from you!
    </p>
</div>
""", unsafe_allow_html=True)

# Stylish Form
st.markdown("""
<style>
form {
    background: rgba(0, 0, 0, 0.45);
    backdrop-filter: blur(6px);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 0 15px rgba(0,0,0,0.3);
    max-width: 600px;
    margin: auto;
}
input, textarea {
    width: 100%;
    padding: 12px;
    margin-top: 10px;
    margin-bottom: 20px;
    border-radius: 8px;
    border: none;
    background-color: rgba(255,255,255,0.1);
    color: white;
    font-size: 15px;
}
input::placeholder, textarea::placeholder {
    color: #aaa;
}
button {
    background-color: #1abc9c;
    color: white;
    padding: 12px 25px;
    font-size: 16px;
    font-weight: bold;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
button:hover {
    background-color: #16a085;
}
</style>

<form action="https://formsubmit.co/sanjanadevi.vksy@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="👤 Your Name" required>
    <input type="email" name="email" placeholder="📧 Your Email" required>
    <textarea name="message" placeholder="💬 Your Message..." rows="5" required></textarea>
    <button type="submit">🚀 Send Message</button>
</form>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<br><br>
<hr style='border: 1px solid white;'>
<footer>
Created with ❤️ by <b>Sanjana</b>
</footer>
""", unsafe_allow_html=True)
