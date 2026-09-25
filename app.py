import streamlit as st

# ============================================
# PAGE CONFIG - Same as original website
# ============================================
st.set_page_config(
    page_title="PNPI Campus Chronicles",
    page_icon="⚓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================
# VIP STYLING - Navy Blue + Gold Theme
# ============================================
st.markdown("""
<style>
    .stApp { background: linear-gradient(180deg, #f8f9fa 0%, #ffffff 100%); }
    .hero-section {
        background: linear-gradient(135deg, #0a1f44 0%, #1a3a6b 50%, #c9a227 100%);
        padding: 60px 30px; border-radius: 20px; text-align: center; color: white;
        box-shadow: 0 15px 35px rgba(10, 31, 68, 0.4); margin-bottom: 30px;
    }
    .hero-section h1 { color:#ffd700; font-size:52px; font-weight:900; margin:0;
        text-shadow:3px 3px 8px rgba(0,0,0,.6); letter-spacing:2px; }
    .hero-section p { color:#fff; font-size:20px; margin-top:15px; font-weight:300; }
    .hero-badge { display:inline-block; background:rgba(255,215,0,.2); border:2px solid #ffd700;
        color:#ffd700; padding:8px 20px; border-radius:30px; margin-top:15px; font-weight:bold; }
    .nav-bar { background:linear-gradient(90deg,#0a1f44,#1a3a6b); padding:15px; border-radius:12px;
        text-align:center; box-shadow:0 5px 15px rgba(0,0,0,.2); margin-bottom:25px; }
    .nav-bar span { color:#ffd700; font-weight:bold; font-size:16px; padding:0 15px; }
    .section-title { background:linear-gradient(90deg,#0a1f44,#1a3a6b); color:#ffd700;
        padding:18px 30px; border-radius:12px; font-size:30px; font-weight:900; margin:35px 0 20px;
        border-left:8px solid #ffd700; box-shadow:0 6px 20px rgba(10,31,68,.3); }
    .info-card { background:white; border-left:6px solid #c9a227; padding:25px; border-radius:12px;
        margin:15px 0; box-shadow:0 6px 20px rgba(0,0,0,.08); }
    .info-card h3 { color:#0a1f44; font-weight:800; margin-top:0; }
    .info-card p { color:#333; font-size:16px; line-height:1.7; }
    .stat-card { background:linear-gradient(135deg,#0a1f44,#1a3a6b); color:#ffd700; padding:25px 15px;
        border-radius:15px; text-align:center; box-shadow:0 8px 20px rgba(10,31,68,.3); border:2px solid #c9a227; }
    .stat-card h2 { color:#ffd700; font-size:42px; margin:0; font-weight:900; }
    .stat-card p { color:#fff; margin:8px 0 0; font-size:15px; font-weight:500; }
    .result-pass,.result-fail,.result-reexam { border-radius:15px; padding:30px; font-size:22px;
        font-weight:bold; text-align:center; }
    .result-pass { background:linear-gradient(135deg,#28a745,#20c997); color:white; box-shadow:0 10px 30px rgba(40,167,69,.4); border:3px solid #155724; }
    .result-fail { background:linear-gradient(135deg,#dc3545,#c82333); color:white; box-shadow:0 10px 30px rgba(220,53,69,.4); border:3px solid #721c24; }
    .result-reexam { background:linear-gradient(135deg,#ffc107,#ff9800); color:#000; box-shadow:0 10px 30px rgba(255,193,7,.4); border:3px solid #856404; }
    .subject-chip { display:inline-block; background:linear-gradient(135deg,#0a1f44,#1a3a6b); color:#ffd700;
        padding:10px 20px; border-radius:25px; margin:6px; font-weight:600; font-size:14px;
        border:2px solid #c9a227; box-shadow:0 4px 10px rgba(10,31,68,.2); }
    .footer { background:linear-gradient(135deg,#0a1f44,#1a3a6b); color:#ffd700; text-align:center;
        padding:40px 20px; border-radius:15px; margin-top:50px; border-top:5px solid #c9a227; }
    .footer h3 { color:#ffd700; font-size:26px; margin-bottom:10px; }
    .footer p { color:#fff; margin:5px 0; }
    .stButton > button { background:linear-gradient(135deg,#0a1f44,#1a3a6b); color:#ffd700;
        border:2px solid #c9a227; border-radius:10px; padding:12px 30px; font-weight:bold; font-size:16px;
        width:100%; }
    [data-testid="stSidebar"] { background:linear-gradient(180deg,#0a1f44 0%,#1a3a6b 100%); }
    [data-testid="stSidebar"] * { color:#ffd700 !important; }
    [data-testid="stSidebar"] .stRadio label { color:#fff !important; font-weight:600; }
    h2,h3 { color:#0a1f44; font-weight:800; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-section">
<h1>⚓ PAKISTAN NAVY POLYTECHNIC INSTITUTE ⚓</h1>
<p>📍 West Wharf Road, Karachi</p>
<div class="hero-badge">🎓 Excellence in Technical Education</div>
</div>
<div class="nav-bar">
<span>🏠 Home</span> | <span>🎓 Technology</span> | <span>📚 Courses</span> |
<span>🏫 Campus</span> | <span>📊 Results</span> | <span>📍 Contact</span>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("# ⚓ PNPI")
st.sidebar.markdown("### Campus Chronicles")
st.sidebar.markdown("---")

page = st.sidebar.radio("**Navigate:**", [
    "🏠 Home", "🎓 Technology & Semesters", "📚 Courses & Faculty",
    "🏫 Campus & Facilities", "📊 Student Results", "📍 Location & Contact"
])

st.sidebar.markdown("---")
st.sidebar.markdown("### 📞 Contact Info")
st.sidebar.markdown("""
**📍 Address:** West Wharf Road, Karachi

**📧 Email:** info@pnpi.edu.pk

**☎ Phone:** +92-21-XXXXXXX
""")
st.sidebar.markdown("---")
st.sidebar.success("✅ Mechatronic Engineering\n\n5 Semesters | 40 Students")

# ============================================
# HOME
# ============================================
if page == "🏠 Home":
    st.image("https://images.unsplash.com/photo-1562774053-701939374585?w=1400",
             caption="PNPI Campus - West Wharf Road, Karachi", use_container_width=True)

    st.markdown('<div class="section-title">🏛️ About Our Institute</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="info-card"><h3>🎯 Who We Are</h3>
        <p><b>Pakistan Navy Polytechnic Institute (PNPI)</b> is a premier technical institution
        located at <b>West Wharf Road, Karachi</b>. Established under the Pakistan Navy, we are
        dedicated to producing highly skilled technical professionals for the nation's industrial
        and defense sectors.</p></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="info-card"><h3>🌟 Our Mission</h3>
        <p>To provide world-class technical education that combines <b>theoretical knowledge</b>
        with <b>hands-on practical training</b>, preparing our students to excel in modern
        engineering environments.</p></div>""", unsafe_allow_html=True)
    with col2:
        st.image("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=800",
                 caption="Our Students - Future Engineers", use_container_width=True)
        st.image("https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=800",
                 caption="Campus Building", use_container_width=True)

    st.markdown('<div class="section-title">📊 Institute at a Glance</div>', unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    for col, num, label in [(c1,"20","Classrooms"),(c2,"1","Technology"),(c3,"5","Semesters"),(c4,"40","Students")]:
        with col:
            st.markdown(f'<div class="stat-card"><h2>{num}</h2><p>{label}</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">⚓ Official Logo</div>', unsafe_allow_html=True)
    lc1,lc2,lc3=st.columns(3)
    with lc2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Pakistan_Navy_emblem.png/400px-Pakistan_Navy_emblem.png",
                 caption="PNPI Official Emblem", use_container_width=True)

# ============================================
# TECHNOLOGY
# ============================================
elif page == "🎓 Technology & Semesters":
    st.markdown('<div class="section-title">🎓 Mechatronic Engineering Technology</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1400",
             caption="Mechatronic Engineering - Robotics & Automation", use_container_width=True)
    st.markdown("""<div class="info-card"><h3>🤖 What is Mechatronic Engineering?</h3>
    <p><b>Mechatronic Engineering</b> is a multidisciplinary branch of engineering that combines
    <b>Mechanical</b>, <b>Electronics</b>, <b>Computer</b>, and <b>Control Systems</b>.
    It's the backbone of modern robotics, automation, and smart manufacturing industries.</p></div>""",
    unsafe_allow_html=True)

    semesters = [
        ("Semester 1 (8 Subjects)", ["Applied Mathematics-I","Applied Physics","Basic Electrical Engineering","Engineering Drawing","Workshop Practice","Computer Fundamentals","English Communication","Islamic Studies"]),
        ("Semester 2 (7 Subjects)", ["Applied Mathematics-II","Electronic Devices & Circuits","Mechanical Engineering Fundamentals","Programming Fundamentals","Engineering Materials","Technical Report Writing","Pakistan Studies"]),
        ("Semester 3 (7 Subjects)", ["Digital Logic Design","Microprocessor & Microcontroller","Fluid Mechanics","Sensors & Transducers","CAD/CAM","Thermodynamics","Industrial Safety"]),
        ("Semester 4 (5 Subjects)", ["Robotics & Automation","PLC & Industrial Control","Hydraulics & Pneumatics","Embedded Systems","Mechatronic System Design"]),
        ("Semester 5 (5 Subjects)", ["Advanced Robotics","Industrial IoT","Project Management","Final Year Project","Industrial Internship"])
    ]
    for i,(title, subjects) in enumerate(semesters,1):
        st.markdown(f'<div class="section-title">📘 {title}</div>', unsafe_allow_html=True)
        st.markdown("**Students: 8 | Duration: 6 Months**")
        for s in subjects:
            st.markdown(f'<span class="subject-chip">📖 {s}</span>', unsafe_allow_html=True)
        if i == 1:
            st.image("https://images.unsplash.com/photo-1580582932707-520aed937b7b?w=1000",
                     caption="Classroom - Semester 1", use_container_width=True)

    st.markdown('<div class="section-title">🏫 20 Modern Classrooms</div>', unsafe_allow_html=True)
    col1,col2=st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=800",
                 caption="Smart Classroom with Projector", use_container_width=True)
    with col2:
        st.image("https://images.unsplash.com/photo-1509062522246-3755977927d7?w=800",
                 caption="Air-Conditioned Lecture Hall", use_container_width=True)
    st.image("https://images.unsplash.com/photo-1580894732444-8ecded7900cd?w=1200",
             caption="Computer Lab Classroom", use_container_width=True)
    st.info("🏫 PNPI features **20 fully-equipped classrooms** with modern teaching aids, projectors, and comfortable seating.")

# ============================================
# COURSES
# ============================================
elif page == "📚 Courses & Faculty":
    st.markdown('<div class="section-title">📚 Complete Study Course</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=1400",
             caption="PNPI Academic Block", use_container_width=True)
    st.markdown("### 📋 Mechatronic Engineering - Course Structure")
    course_data = {
        "Semester":["Semester 1","Semester 2","Semester 3","Semester 4","Semester 5"],
        "Subjects":[8,7,7,5,5],"Students":[8,8,8,8,8],
        "Duration":["6 Months"]*5,"Status":["✅ Active"]*5
    }
    st.table(course_data)
    st.markdown("---")
    st.markdown('<div class="section-title">👨‍🏫 Our Distinguished Faculty</div>', unsafe_allow_html=True)

    teachers = [
        ("Capt. Engr. Ahmed Raza","Applied Mathematics-I & II","M.Sc Mathematics, PN Retd.","https://images.unsplash.com/photo-1560250097-0b93528c311a?w=400"),
        ("Engr. Fatima Khan","Applied Physics","M.Phil Physics, NED UET","https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400"),
        ("Lt. Engr. Bilal Hussain","Basic Electrical Engineering","B.E Electrical, PN Retd.","https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=400"),
        ("Engr. Sana Malik","Electronic Devices & Circuits","M.E Electronics, KU","https://images.unsplash.com/photo-1580489944761-15a19d654956?w=400"),
        ("Engr. Usman Tariq","Programming Fundamentals","M.Sc Computer Science","https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400"),
        ("Engr. Ayesha Siddiqui","Digital Logic Design","M.E Mechatronics, NUST","https://images.unsplash.com/photo-1594744803329-e58b31de8bf5?w=400"),
        ("Engr. Hassan Ali","Microprocessor & Microcontroller","M.Sc Embedded Systems","https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400"),
        ("Engr. Zainab Sheikh","Robotics & Automation","Ph.D Robotics (Scholar)","https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400"),
        ("Engr. Kamran Akmal","PLC & Industrial Control","M.E Control Systems","https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400"),
        ("Engr. Maria Noor","CAD/CAM","M.Sc Mechanical Engineering","https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=400"),
        ("Cdr. Engr. Imran Shah","Mechatronic System Design","M.E Mechatronics, PN Retd.","https://images.unsplash.com/photo-1566492031773-4f4e44671857?w=400"),
        ("Engr. Rabia Aslam","Industrial IoT & Embedded","M.Sc IoT, NED UET","https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400")
    ]
    cols=st.columns(3)
    for idx,t in enumerate(teachers):
        with cols[idx%3]:
            st.image(t[3], use_container_width=True)
            st.markdown(f"**{t[0]}**")
            st.caption(f"📖 {t[1]}")
            st.caption(f"🎓 {t[2]}")
            st.markdown("---")

# ============================================
# CAMPUS
# ============================================
elif page == "🏫 Campus & Facilities":
    st.markdown('<div class="section-title">🏫 Campus Facilities</div>', unsafe_allow_html=True)
    st.markdown("### 🤖 Mechatronic Laboratory")
    st.image("https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=1400",
             caption="Mechatronic Engineering Laboratory", use_container_width=True)
    c1,c2=st.columns(2)
    with c1:
        st.image("https://images.unsplash.com/photo-1567789884554-0b844b597180?w=800",
                 caption="Robotics & Automation Lab", use_container_width=True)
    with c2:
        st.image("https://images.unsplash.com/photo-1518770660439-4636190af475?w=800",
                 caption="Electronics & Embedded Lab", use_container_width=True)
    st.markdown("---")
    st.markdown("### 📚 Central Library")
    st.image("https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=1400",
             caption="PNPI Central Library", use_container_width=True)
    l1,l2=st.columns(2)
    with l1:
        st.image("https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=800",
                 caption="Reading Hall", use_container_width=True)
    with l2:
        st.image("https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800",
                 caption="Reference Section", use_container_width=True)
    st.info("📖 Library contains **10,000+ books** on Engineering, Mathematics, Physics, and Technical subjects.")
    st.markdown("---")
    st.markdown("### 🏏 PNPI Cricket Group")
    st.image("https://images.unsplash.com/photo-1531415074968-036ba1b575da?w=1400",
             caption="PNPI Cricket Team", use_container_width=True)
    st.image("https://images.unsplash.com/photo-1624526267942-ab0ff8a3e972?w=1400",
             caption="Cricket Ground - Practice Session", use_container_width=True)
    st.markdown("---")
    st.markdown("### 🍽️ College Canteen")
    st.image("https://images.unsplash.com/photo-1567521464027-f127ff144326?w=1400",
             caption="PNPI Canteen - Hygienic Food", use_container_width=True)
    n1,n2=st.columns(2)
    with n1:
        st.image("https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800",
                 caption="Dining Area", use_container_width=True)
    with n2:
        st.image("https://images.unsplash.com/photo-1600891964092-4316c288032e?w=800",
                 caption="Fresh Menu", use_container_width=True)

# ============================================
# RESULTS
# ============================================
elif page == "📊 Student Results":
    st.markdown('<div class="section-title">📊 Student Result Portal</div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=1400",
             caption="Result Portal - Login to view your result", use_container_width=True)
    st.warning("🔐 **Login Required** — Apna Naam aur Roll Number enter karein.")

    students_db = {
        "Ahmed Ali":{"roll":"PNPI-2024-001","marks":{"Applied Mathematics-I":78,"Applied Physics":82,"Basic Electrical Engineering":65,"Engineering Drawing":71,"Workshop Practice":88,"Computer Fundamentals":55,"English Communication":68,"Islamic Studies":75}},
        "Bilal Khan":{"roll":"PNPI-2024-002","marks":{"Applied Mathematics-I":45,"Applied Physics":52,"Basic Electrical Engineering":58,"Engineering Drawing":48,"Workshop Practice":62,"Computer Fundamentals":55,"English Communication":50,"Islamic Studies":60}},
        "Sara Ahmed":{"roll":"PNPI-2024-003","marks":{"Applied Mathematics-I":88,"Applied Physics":91,"Basic Electrical Engineering":85,"Engineering Drawing":79,"Workshop Practice":92,"Computer Fundamentals":87,"English Communication":84,"Islamic Studies":90}},
        "Hassan Raza":{"roll":"PNPI-2024-004","marks":{"Applied Mathematics-I":55,"Applied Physics":48,"Basic Electrical Engineering":62,"Engineering Drawing":71,"Workshop Practice":75,"Computer Fundamentals":58,"English Communication":65,"Islamic Studies":72}},
        "Fatima Noor":{"roll":"PNPI-2024-005","marks":{"Applied Mathematics-I":92,"Applied Physics":89,"Basic Electrical Engineering":94,"Engineering Drawing":88,"Workshop Practice":95,"Computer Fundamentals":91,"English Communication":86,"Islamic Studies":93}},
        "Usman Tariq":{"roll":"PNPI-2024-006","marks":{"Applied Mathematics-I":42,"Applied Physics":55,"Basic Electrical Engineering":38,"Engineering Drawing":60,"Workshop Practice":65,"Computer Fundamentals":48,"English Communication":52,"Islamic Studies":58}},
        "Ayesha Malik":{"roll":"PNPI-2024-007","marks":{"Applied Mathematics-I":76,"Applied Physics":81,"Basic Electrical Engineering":73,"Engineering Drawing":68,"Workshop Practice":85,"Computer Fundamentals":79,"English Communication":82,"Islamic Studies":88}},
        "Kamran Shah":{"roll":"PNPI-2024-008","marks":{"Applied Mathematics-I":61,"Applied Physics":58,"Basic Electrical Engineering":66,"Engineering Drawing":72,"Workshop Practice":68,"Computer Fundamentals":64,"English Communication":70,"Islamic Studies":75}}
    }

    col1,col2=st.columns(2)
    with col1: student_name=st.text_input("👤 Student Name:")
    with col2: roll_number=st.text_input("🔢 Roll Number:")

    if st.button("📊 Show My Result"):
        found=False
        for name,data in students_db.items():
            if name.lower()==student_name.lower().strip() and data["roll"]==roll_number.strip():
                found=True
                st.success(f"✅ Welcome, {name}!")
                st.markdown("---")
                st.markdown(f"### 📋 Result Card — {name}")
                st.markdown(f"**Roll Number:** `{data['roll']}`  |  **Technology:** Mechatronic Engineering  |  **Semester:** 1st")
                marks=data["marks"]; failed_subjects=[]; total_marks=0; result_rows=[]
                for subj,m in marks.items():
                    status="✅ Pass" if m>=60 else "❌ Fail"
                    if m<60: failed_subjects.append(subj)
                    total_marks+=m
                    result_rows.append({"Subject":subj,"Marks":m,"Percentage":f"{m}%","Status":status})
                st.markdown("#### 📝 Subject-wise Marks")
                st.table(result_rows)
                percentage=total_marks/len(marks)
                st.markdown(f"#### 📊 Overall Percentage: **{percentage:.2f}%**")
                st.markdown("---")
                st.markdown("### 🎯 Final Result Status")
                fail_count=len(failed_subjects)
                if fail_count==0:
                    st.markdown(f"""<div class="result-pass">🎉 STATUS: PASS<br>Congratulations {name}!<br>
                    Aap ne tamam subjects mein 60% ya us se zyada marks hasil kiye hain.<br>
                    Overall Percentage: {percentage:.2f}%</div>""", unsafe_allow_html=True)
                    st.balloons()
                elif fail_count>=3:
                    st.markdown(f"""<div class="result-fail">❌ STATUS: FAIL<br>
                    Afsos! Aap {fail_count} subjects mein 60% se kam marks hasil kiye hain.<br>
                    Failed Subjects: {', '.join(failed_subjects)}<br>
                    Overall Percentage: {percentage:.2f}%</div>""", unsafe_allow_html=True)
                else:
                    st.markdown(f"""<div class="result-reexam">⚠️ STATUS: RE-EXAM<br>
                    Aap {fail_count} subject(s) mein 60% se kam marks hasil kiye hain.<br>
                    Re-Exam Subjects: {', '.join(failed_subjects)}<br>
                    Overall Percentage: {percentage:.2f}%<br><b>Note:</b>
                    Sirf {fail_count} subject(s) ka re-exam dena hoga.</div>""", unsafe_allow_html=True)
                break
        if not found:
            st.error("❌ Student not found! Please check your Name and Roll Number.")
            st.info("💡 **Demo Login Details:**")
            st.markdown("""
            | Name | Roll Number | Result |
            |---|---|---|
            | Ahmed Ali | PNPI-2024-001 | ✅ PASS |
            | Bilal Khan | PNPI-2024-002 | ❌ FAIL |
            | Sara Ahmed | PNPI-2024-003 | ✅ PASS |
            | Hassan Raza | PNPI-2024-004 | ⚠️ RE-EXAM |
            | Fatima Noor | PNPI-2024-005 | ✅ PASS |
            | Usman Tariq | PNPI-2024-006 | ❌ FAIL |
            | Ayesha Malik | PNPI-2024-007 | ✅ PASS |
            | Kamran Shah | PNPI-2024-008 | ⚠️ RE-EXAM |
            """)

# ============================================
# LOCATION & CONTACT
# ============================================
elif page == "📍 Location & Contact":
    st.markdown('<div class="section-title">📍 Location & Contact</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-card">
    <h3>⚓ Pakistan Navy Polytechnic Institute</h3>
    <p><b>📍 Address:</b> West Wharf Road, Karachi</p>
    <p><b>📧 Email:</b> info@pnpi.edu.pk</p>
    <p><b>☎ Phone:</b> +92-21-XXXXXXX</p>
    </div>
    """, unsafe_allow_html=True)
    st.map({"lat":[24.847], "lon":[66.994]}, zoom=13)

# ============================================
# FOOTER
# ============================================
st.markdown("""
<div class="footer">
<h3>⚓ PAKISTAN NAVY POLYTECHNIC INSTITUTE</h3>
<p>🎓 Excellence in Technical Education</p>
<p>📍 West Wharf Road, Karachi | 📧 info@pnpi.edu.pk</p>
<p>© 2026 PNPI Campus Chronicles | Prepared by Mazhar Abbas</p>
</div>
""", unsafe_allow_html=True)
