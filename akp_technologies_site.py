import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="AKP Technologies Pvt. Ltd.", layout="wide")

# --- LIGHT MODE CUSTOM CSS WITH BACKGROUND COLOR ---
custom_css = """
<style>
    body {
        background-color: #f1f3f5;  /* Background Color */
        color: #212529;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3, h4, h5 {
        color: #0056b3;
    }
    .stTextInput > div > div > input,
    .stTextArea textarea {
        background-color: #ffffff;
        color: #212529;
        border: 1px solid #ced4da;
        border-radius: 0.375rem;
    }
    .stButton button {
        background-color: #0056b3;
        color: white;
        border-radius: 0.375rem;
    }
    .stMarkdown {
        font-size: 1.1rem;
    }
    .stSubheader {
        color: #0056b3;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- HEADER + LOGO ---
st.image("logo_akp.png", width=100)
st.markdown("<h1 style='text-align: center;'>AKP Technologies Pvt. Ltd.</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Empowering Your Business Through Intelligent Automation</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- ABOUT SECTION ---
st.subheader("About Us")
st.write("""
**AKP Technologies Pvt. Ltd.** is an innovative IT services and automation company at the forefront of **digital transformation**. Our expertise lies in integrating **Robotic Process Automation (RPA)** with AI technologies to create **intelligent, automated systems** that improve business efficiency, scalability, and reliability.

We specialize in globally recognized tools like [UiPath](https://en.wikipedia.org/wiki/UiPath), [Automation Anywhere](https://en.wikipedia.org/wiki/Automation_Anywhere), and [Microsoft Power Automate](https://en.wikipedia.org/wiki/Microsoft_Power_Automate) to bring the future of work into the present.

- **Mission:** Drive businesses toward automation with scalable, AI-driven RPA solutions.
- **Vision:** To be the most trusted partner for digital transformation worldwide.
- **Core Values:** Innovation | Efficiency | Trust
""")

# --- AGENTIC PROCESS AUTOMATION (APA) SECTION ---
st.markdown("---")
st.subheader("What is Agentic Process Automation (APA)?")

st.write("""
Agentic Process Automation (APA) is a futuristic concept where **AI** and **RPA** work in tandem to create **autonomous systems** capable of not only performing manual tasks but also making intelligent decisions based on data. This goes beyond traditional RPA, where bots are only rule-based, and introduces **self-learning bots** that can **adapt** and **optimize processes** with minimal human intervention.

APA enhances business operations by:
- **Autonomous Decision-Making:** Using AI and machine learning algorithms, APA bots can autonomously analyze data and make decisions in real-time.
- **Context-Aware Automation:** APA integrates **natural language processing (NLP)** and **computer vision**, allowing bots to interpret and act on unstructured data.
- **Cognitive Automation:** APA bots understand and learn from human interactions, adapting workflows to improve over time.
- **Faster Time to Market:** Intelligent automation through APA accelerates the implementation of complex workflows, allowing businesses to move faster than ever before.

The **future of RPA** is **AI-powered**. The combination of AI and RPA is transforming industries, and companies that embrace this change are positioned to lead in the digital era.
""")

# --- FUTURE OF RPA & AI IN BUSINESS ---
st.markdown("---")
st.subheader("The Future of RPA & AI in Business")

st.write("""
As we move into the next decade, **RPA and AI** will become more intertwined, enabling businesses to fully automate end-to-end processes and optimize operations across various sectors.

Here’s how **RPA and AI** are shaping the future:

- **AI-Powered RPA (Cognitive Automation):** Traditional RPA handles repetitive tasks, but AI-powered bots bring cognitive abilities to automation, enabling them to analyze complex datasets, predict trends, and make smarter decisions.
  
- **Hyperautomation:** Hyperautomation takes RPA and AI to the next level by automating as many business processes as possible across the enterprise. **Process Mining**, **AI-enabled bots**, and **Intelligent Document Processing** (IDP) will enable organizations to continuously optimize workflows.

- **End-to-End Automation:** With AI, businesses can automate entire processes, from customer service to supply chain management. The integration of AI with RPA will automate not just repetitive tasks but also more complex, decision-making tasks.

- **Improved Customer Experiences:** AI and RPA will allow businesses to handle customer interactions with **chatbots**, **virtual assistants**, and **automated email responses**, offering a seamless and personalized experience for users.

- **Increased Efficiency and Cost Savings:** By leveraging AI and RPA together, organizations can **reduce operational costs**, enhance accuracy, and increase throughput. Businesses can deliver faster services, innovate quickly, and maintain a competitive edge.

**Industries Transforming with AI & RPA:**
- **Finance & Banking**: Automating regulatory reporting, compliance checks, and customer onboarding.
- **Healthcare**: Automating patient records management, claims processing, and telemedicine.
- **Retail**: Enhancing inventory management, order fulfillment, and customer support through automation.
- **Manufacturing**: AI-driven bots for predictive maintenance, production scheduling, and logistics optimization.

The future of automation is about enhancing human potential by offloading routine tasks to bots, allowing employees to focus on strategic activities that drive business growth. AI will empower RPA to become more intelligent, autonomous, and capable of transforming industries globally.

By 2030, **over 70% of businesses** are expected to be using AI-driven automation at scale, providing **AI-powered solutions** for tasks ranging from decision-making to managing complex workflows.
""")

# --- SERVICES SECTION ---
st.markdown("---")
st.subheader("Our Services")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🤖 RPA Solutions")
    st.write("""
    - Business Process Mapping  
    - **UiPath**, **Automation Anywhere**, **Power Automate** Bot Development  
    - Attended & Unattended Automation  
    - Cognitive Automation & Hyperautomation
    """)

    st.markdown("### 💼 IT Consulting")
    st.write("""
    - Digital Transformation Roadmaps  
    - Architecture & Systems Review  
    - Cloud Readiness & Migration  
    - ERP & CRM Strategy  
    """)

with col2:
    st.markdown("### 💻 Custom Software Development")
    st.write("""
    - Web & Mobile App Development  
    - Internal Workflow Tools  
    - API & Legacy System Integration  
    - Secure, Scalable Cloud Applications  
    """)

    st.markdown("### 🔧 Business Process Optimization")
    st.write("""
    - Process Discovery & Mining  
    - Re-engineering with Lean/Six Sigma  
    - Performance Metrics & Analytics  
    - Automation Readiness Assessment  
    """)

# --- WHY US SECTION ---
st.markdown("---")
st.subheader("Why Choose AKP Technologies?")
st.write("""
✅ End-to-End RPA Expertise with AI Integration  
✅ Scalable Automation Solutions  
✅ Agile, Fast-Track Delivery for Complex Projects  
✅ AI & RPA Synergy for Seamless Automation  
✅ 24/7 Support & Maintenance  
✅ Transparent, ROI-Focused Engagements  
""")

# --- TESTIMONIALS (Static for Now) ---
st.markdown("---")
st.subheader("Client Testimonial")
st.info("“Partnering with AKP Technologies has revolutionized our business. By integrating **AI** and **RPA**, we increased productivity by 60% in just 4 months!” — Chief Digital Officer, Manufacturing Client")

# --- CONTACT FORM ---
st.markdown("---")
st.subheader("Contact Us")
with st.form(key="contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success("Thank you! Our team will connect with you shortly.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<h5 style='text-align: center;'>📧 contact@akptechnologies.com | 📞 +91-9200155833</h5>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 0.85rem;'>© 2025 AKP Technologies Pvt. Ltd. | All rights reserved.</p>", unsafe_allow_html=True)
