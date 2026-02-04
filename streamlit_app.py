import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Researcher Profile | Yuvaan Bhimsan",
    page_icon="🧬",
    layout="centered"
)

# Header
st.title("🧬 Researcher Profile")
st.subheader("Yuvaan Bhimsan")

st.markdown(
    """
    **Aspiring Computational Geneticist | Bioinformatics & Public Health**  
    Interested in population health, genomics, and data-driven decision making.
    """
)

st.divider()

# About section
st.header("👨‍🔬 About Me")
st.markdown(
    """
    I hold an honours degree in Genetics and currently completing my Master's in Human Genetics. My academic interests lie at the intersection of **human genetics,
    bioinformatics, and data science**, with a focus on improving
    population health outcomes in South Africa.
    """
)

# Research interests
st.header("🔬 Research Interests")
st.markdown(
    """
    - Human genetics and genomics  
    - RNA-seq and variant analysis  
    - Bioinformatics and data analysis (R, Python, SQL)  
    - Epidemiology and public health  
    - Health economics and population health  
    """
)

# Skills
st.header("🛠️ Technical Skills")
st.markdown(
    """
    **Programming & Data**
    - Python, R, SQL  
    - Pandas, NumPy, Matplotlib, Streamlit  

    **Bioinformatics**
    - RNA-seq analysis  
    - Variant calling pipelines  
    - FastQC, Trimmomatic, MultiQC  

    **Other**
    - Linux & Bash  
    - HPC (CHPC – PBS job scripting)  
    """
)

# Projects
st.header("📂 Projects")
st.markdown(
    """
    - **RNA-seq Variant Discovery Project**  
      Identification of pathogenic variants from RNA-seq data.

    - **Data Analysis & Visualisation Projects**  
      Exploratory data analysis using Python and interactive dashboards with Streamlit.
    """
)

# Contact
st.header("📬 Contact")
st.markdown(
    """
    - **Email:** yuvaanb@example.com  
    - **GitHub:** https://github.com/yuvaanb
    """
)

st.divider()
st.caption("Built with Streamlit ☁️ | Coding Summer School 2026")
