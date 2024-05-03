from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume = current_dir / "assets" / "Jeric Dela Cruz Resume.pdf"
profile_pic = current_dir / "assets" / "photo.jpeg"

# ----------------- GENERAL SETTINGS ----------

PAGE_TITLE = "Digital CV | Jeric Dela Cruz"
PAGE_ICON = ":computer:"
NAME = "Jeric Dela Cruz"
DESCRIPTION = """ 🔧 Experienced IT Leader | Network & Security Specialist | Incident Resolution Expert 🔧 """
EMAIL = "jericdelacruz1991@gmail.com"
SOCIAL_MEDIA = {
    "Youtube":  "https://youtube.com",
    "LinkedIn": "https://linkedin.com/in/jeric-dela-cruz-597420166/",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
    }
PROJECTS = {
    "Sales Dashboard - Lurem ipsum": "https//youtube.com",
    "Sales Dashboard - Lurem ipsum": "https//youtube.com",
    "Sales Dashboard - Lurem ipsum": "https//youtube.com",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# -- LOAD CSS, PDF & PROFILE PIC
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ----
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
    
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label= ":open_file_folder: Download Resume" ,
        data=PDFbyte,
        file_name=resume.name,
        mime="application/octet-stream",
    )
    st.write(":email:", EMAIL) 


# ---- SOCIAL LINKS -----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    



# --- EXPERIENCE & QUALIFICATIONS -----

st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- :white_check_mark: Proven track record in incident resolution and management, ensuring minimal downtime and uninterrupted service delivery.
- :white_check_mark: Strong background in implementing and managing cybersecurity measures to safeguard organizational assets against threats.
- :white_check_mark: Demonstrated ability to analyze complex technical issues and develop innovative solutions to ensure optimal performance and reliability.
- :white_check_mark: Proven ability to lead and manage teams effectively, fostering a collaborative and productive work environment. Skilled in setting clear objectives, providing guidance and support, and empowering team members to achieve their full potential.
- :white_check_mark: Demonstrated proficiency in strategic planning, prioritization, and decision-making, with a focus on aligning IT initiatives with organizational goals and objectives. Capable of analyzing complex situations, identifying opportunities, and implementing effective strategies to drive business success.
- :white_check_mark: Effective communicator and collaborator, capable of working closely with cross-functional teams to achieve common goals and objectives in challenging environments.
"""
)

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(""" 
- :desktop_computer: Scipting and Automation: Python, Bash, SQL, MongoDB, PostgreSQL.
- ☁️ Network Infrastructure Management: Configuration and maintenance of firewalls, routers, switches and servers.
- 🕥 Incident Management and Resolution: Incident triage and prioritization, SLA management and adherence, Dcoumentation of incident reports and resolutions.
- 🛡️ Cybersecurity: Intrusion detection and prevention systems, Secuirty auditing and compliance, Security awareness training for employees.
- 🏅 Networking Technologies: TCP/IP networking fundamentals, Wireless networking, Network security protocols (SSL/TLS.IPsec)
""")



# --- CERTIFICATIONS ---
st.write("#")
st.subheader("Certifications")
st.write(""" 
- 🎖️ Cisco Certified Network Associate
- 🎖️ Data Protection Officer Certified
- 🎖️ Network Security Expert L1
- 🎖️ Network Security Expert L2
- 🎖️ Network Security Expert L4
- 🎖️ Service Delivery Training Certified
- 🎖️ Customer Service Excellence Certified
- 🎖️ Computer System Servicing Certified NCII
- 🎖️ MongoDB,ExpressJS,ReactJS and NodeJS Certification
""")





# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# ---- 1st Job
st.write("💼", "**L3 Incident Manager | CloudCover IT")
st.write("📌", "California, USA")
st.write("📅", "12/2023 - Present")
st.write(""" 
- ➡️ Led incident management efforts, coordinating with cross-functional teams to restore services and mitigate impact effectively.   
- ➡️ Facilitated prompt resolution of critical incidents, ensuring minimal service disruption and high availability of cloud services.
- ➡️ Ensured adherence to SLAs by meeting response and resolution targets consistently, maintaining service quality and reliability.
- ➡️ Collaborated closely with clients to understand their needs and address technical challenges, fostering strong client relationships and loyalty.
- ➡️ Prioritized customer satisfaction and feedback, implementing initiatives to improve service quality and exceed customer expectations.
- ➡️ Provided training and mentorship to junior team members, fostering their professional growth and development within the organization.
- ➡️ Worked closely with vendors and partners to troubleshoot issues and implement solutions, ensuring timely resolution and minimal impact on service delivery.
- ➡️ Prioritized customer satisfaction and feedback, implementing initiatives to improve service quality and exceed customer expectations.
         """)

# ---- 2nd Job
st.write("💼", "**Wireless Network Engineer | GigFire")
st.write("📌", "Minnesota, USA")
st.write("📅", "04/2022 - 11/2023")
st.write(""" 
- ➡️ Proficient in designing, deploying, and optimizing wireless networks to ensure seamless connectivity and optimal performance for clients.
- ➡️ Experienced in conducting comprehensive RF surveys and site assessments to identify optimal placement of access points and mitigate interference for maximum coverage and reliability.
- ➡️ Skilled in implementing robust security measures for wireless networks, including WPA2/WPA3 encryption, VLAN segmentation, and rogue AP detection, to safeguard against unauthorized access and data breaches.
- ➡️ Proven ability to fine-tune wireless network settings and configurations to optimize performance, minimize latency, and enhance user experience, resulting in improved network efficiency and productivity.
- ➡️ Adept at diagnosing and resolving complex wireless network issues, including coverage gaps, interference, and connectivity issues, using tools such as Wireshark and spectrum analyzers to identify root causes and implement effective solutions.
- ➡️ Familiarity with emerging wireless technologies such as Wi-Fi 6 (802.11ax), 5G, and IoT connectivity, with a focus on integrating these technologies into existing network infrastructure to support future scalability and innovation.
- ➡️ Experience working with wireless equipment vendors and service providers to evaluate products, negotiate contracts, and coordinate installations, ensuring timely delivery of solutions that meet client requirements and expectations.
- ➡️ •	Committed to staying abreast of industry trends and best practices in wireless networking through ongoing training and certification programs, including Cisco CCNA Wireless and CWNP certifications, to enhance skills and expertise in the field.
""")





# ---- 3nd Job
st.write("💼", "**Network and Security Specialist | International Business Machines (IBM)") 
st.write("📌", "New York, USA")
st.write("📅", "06/2018 - 04/2022")
st.write(""" 
- ➡️ Spearheaded the design and implementation of intricate firewall routing policies, ensuring robust network security while optimizing data traffic flow.
- ➡️ Implemented cutting-edge security protocols, including intrusion detection systems (IDS) and intrusion prevention systems (IPS), enhancing network defense against cyber threats.
- ➡️ Led successful efforts to identify and neutralize potential security threats, conducting thorough analyses of vulnerabilities and deploying countermeasures promptly.
- ➡️ Pioneered the adoption of Zero Trust principles, redefining network access policies and bolstering security by enforcing strict identity verification and least privilege access.
- ➡️ Orchestrated efficient incident response protocols, swiftly containing and mitigating security breaches to minimize impact and maintain data integrity.
- ➡️ Leveraged in-depth knowledge of firewall technologies to fine-tune rule sets, resulting in a 70 Percent improvement in network performance without compromising security.
- ➡️ Executed comprehensive security audits, ensuring adherence to industry standards and regulatory requirements while proactively identifying and addressing potential vulnerabilities.
- ➡️ Conducted rigorous penetration tests to simulate real-world attacks, identifying weak points and implementing robust solutions to fortify network resilience.
- ➡️ Secure Remote Access Solutions: Designed and implemented secure remote access solutions, allowing authorized users to connect seamlessly while maintaining stringent security controls.
- ➡️ Spearheaded workshops to enhance employee awareness of security best practices, reducing the risk of social engineering attacks and fostering a culture of cybersecurity.
- ➡️ Kept abreast of evolving cyber threats and emerging security trends, implementing preemptive measures to defend against zero-day vulnerabilities.
- ➡️ Cultivated strong partnerships with security solution vendors, optimizing support and leveraging the latest tools to enhance network defense strategies.
""")


# ---- 4th Job
st.write("💼", "**IT Network Specialist | DOIT SECURITY") 
st.write("📌", "California, USA")
st.write("📅", "11/2017 - 04/2018")
st.write(""" 
- ➡️ Led successful efforts to identify and neutralize potential security threats, conducting thorough analyses of vulnerabilities and deploying countermeasures promptly.
- ➡️ Pioneered the adoption of Zero Trust principles, redefining network access policies and bolstering security by enforcing strict identity verification and least privilege access.
- ➡️ High Availability Setup: Designed and implemented high-availability configurations for key systems, minimizing downtime and ensuring continuous availability of services.
- ➡️ Leveraged in-depth knowledge of firewall technologies to fine-tune rule sets, resulting in a 70% improvement in network performance without compromising security.
- ➡️ Security Enhancements: Implemented stringent security measures for servers and POS systems, including regular patching, intrusion detection, and access controls, fortifying data protection and regulatory compliance.
- ➡️ Adept at diagnosing and resolving network issues, including connectivity issues, performance bottlenecks, and security breaches, utilizing troubleshooting methodologies and tools to minimize downtime and disruption.
- ➡️ Experience working with network equipment vendors and service providers to evaluate products, negotiate contracts, and coordinate installations and maintenance activities, ensuring alignment with organizational objectives and budgetary constraints.
- ➡️ Knowledgeable in deploying and managing wireless networks, including access point placement, RF optimization, and security configurations, to provide seamless connectivity for users across diverse environments.
- ➡️ Inventory Management Integration: Successfully integrated POS systems with inventory management software, optimizing stock control and inventory accuracy for streamlined operations.
- ➡️ Remote Monitoring: Implemented remote monitoring tools to proactively detect and address potential issues, ensuring preemptive actions and minimizing service interruptions.
- ➡️ Compliance Adherence: Ensured adherence to relevant industry regulations, including data privacy standards, by implementing appropriate security measures and documentation.
""")



# ---- 5th Job
st.write("💼", "**IT Support Specialist | Perry's Group Of Companies") 
st.write("📌", "Manila, Philippines")
st.write("📅", "03/2016 - 08/2017")
st.write(""" 
- ➡️ Desktop and Laptop Support: Provided expert technical assistance for desktop and laptop systems, diagnosing and resolving hardware and software issues promptly to minimize user downtime.
- ➡️ Remote Assistance: Demonstrated exceptional remote troubleshooting skills, efficiently resolving technical problems for remote users through clear communication and remote desktop tools.
- ➡️ Windows Server Management: Proficiently managed and maintained Windows Server environments, including Active Directory, DNS, DHCP, and Group Policy settings, ensuring reliable and secure network operations.
- ➡️ Mobile Device Management: Successfully implemented and managed mobile device management solutions, ensuring secure access to company resources while maintaining data integrity.
- ➡️ Hardware and Software Upgrades: Strategically planned and executed hardware and software upgrades, enhancing system performance, and ensuring compatibility with the latest technologies.
- ➡️ User Training and Guidance: Delivered user training sessions and created user-friendly documentation, empowering employees to effectively use technology tools and minimize common issues.
- ➡️ Worked closely with vendors and partners to troubleshoot issues and implement solutions, ensuring timely resolution and minimal impact on service delivery.
- ➡️ •	Software Deployment: Skillfully deployed and managed software applications using automated deployment tools, ensuring consistent software configurations across the organization.
""")


# ---- 6th Job
st.write("💼", "**Technical Sales Representative | Asia Technology Solutions") 
st.write("📌", "Manila, Philippines")
st.write("📅", "01/2015 - 01/2016")
st.write(""" 
- ➡️ Demonstrated in-depth understanding of security hardware products, enabling clear communication of product features, benefits, and technical specifications to clients.
- ➡️ Built strong relationships with clients by actively listening to their requirements, understanding their concerns, and offering tailored technical solutions that met their needs.
- ➡️ Provided expert technical assistance for desktop and laptop systems, diagnosing and resolving hardware and software issues promptly to minimize user downtime.
- ➡️ Offered consultative technical advice to clients during the sales process, ensuring they made informed decisions that aligned with their security requirements.
- ➡️ Effectively resolved technical issues raised by clients, diagnosing problems with CCTV and door access systems, and providing step-by-step guidance for troubleshooting.
- ➡️ Collaborated with clients to customize security solutions based on their specific needs, ensuring optimal integration of CCTV and door access systems within their environments.
- ➡️ Worked closely with vendors and partners to troubleshoot issues and implement solutions, ensuring timely resolution and minimal impact on service delivery.
- ➡️ Prioritized customer satisfaction and feedback, implementing initiatives to improve service quality and exceed customer expectations.
- ➡️ Conducted comprehensive product demonstrations, showcasing the functionality and ease of use of security hardware, resulting in increased client confidence and sales.
- ➡️ Provided clients with training on operating and maintaining security hardware, empowering them to maximize the benefits of their purchased systems.
- ➡️ Created and shared technical documentation and user guides, enhancing client understanding and ensuring smooth operation of security hardware.
- ➡️ Identified opportunities to upsell and cross-sell additional security hardware solutions to clients based on their evolving needs and requirements.
""")


# ----- Porjects & Accomplishments -----
