import streamlit as st
from fpdf import FPDF

# -----------------------
# Helper: make text PDF-safe
# -----------------------
def pdf_safe(text: str) -> str:
    replacements = {
        "–": "-",   # en dash
        "—": "-",   # em dash
        "•": "-",   # bullet
        "’": "'",   # smart apostrophe
        "“": '"',
        "”": '"',
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


# -----------------------
# PDF CV CLASS
# -----------------------
class CV(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Yuvaan Bhimsan", ln=True)
        self.ln(2)
        self.set_font("Arial", "", 11)
        self.cell(0, 8, "Aspiring Computational Geneticist | Bioinformatics & Data Science", ln=True)
        self.ln(5)

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, pdf_safe(title), ln=True)
        self.ln(1)

    def section_body(self, text):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, pdf_safe(text))
        self.ln(2)


def generate_cv_pdf():
    pdf = CV()
    pdf.add_page()

    pdf.section_title("Profile")
    pdf.section_body(
        "I hold an honours degree in Genetics and am currently completing my Master's "
        "in Human Genetics. My academic interests lie at the intersection of human "
        "genetics, bioinformatics, and data science, with a focus on improving "
        "population health outcomes in South Africa."
    )

    pdf.section_title("Research Interests")
    pdf.section_body(
        "Human genetics and genomics\n"
        "RNA-seq and variant analysis\n"
        "Bioinformatics and data analysis (R, Python, SQL)\n"
        "Epidemiology and public health\n"
        "Health economics and population health"
    )

    pdf.section_title("Technical Skills")
    pdf.section_body(
        "Programming & Data:\n"
        "Python, R, SQL\n"
        "Pandas, NumPy, Matplotlib, Streamlit\n\n"
        "Bioinformatics:\n"
        "RNA-seq analysis\n"
        "Variant calling pipelines\n"
        "FastQC, Trimmomatic, MultiQC\n\n"
        "Other:\n"
        "Linux & Bash\n"
        "HPC (CHPC – PBS job scripting)"
    )

    pdf.section_title("Projects")
    pdf.section_body(
        "RNA-seq Variant Discovery Project:\n"
        "Identification of pathogenic variants from RNA-seq data.\n\n"
        "Data Analysis & Visualisation Projects:\n"
        "Exploratory data analysis using Python and interactive dashboards."
    )

    return bytes(pdf.output(dest="S"))


# -----------------------
# STREAMLIT UI
# -----------------------
st.set_page_config(
    page_title="Curriculum Vitae | Yuvaan Bhimsan",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Curriculum Vitae")
st.subheader("Yuvaan Bhimsan")

st.markdown(
    """
    **Aspiring Computational Geneticist | Bioinformatics & Data Science**

    This CV can be downloaded as a PDF and used for academic, research,
    or professional applications.
    """
)

st.divider()

st.header("Profile")
st.write(
    "I hold an honours degree in Genetics and am currently completing my Master's "
    "in Human Genetics. My academic interests lie at the intersection of human "
    "genetics, bioinformatics, and data science, with a focus on improving "
    "population health outcomes in South Africa."
)

st.header("Research Interests")
st.markdown(
    """
    - Human genetics and genomics  
    - RNA-seq and variant analysis  
    - Bioinformatics and data analysis (R, Python, SQL)  
    - Epidemiology and public health  
    - Health economics and population health  
    """
)

st.header("Technical Skills")
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

st.header("Projects")
st.markdown(
    """
    **RNA-seq Variant Discovery Project**  
    Identification of pathogenic variants from RNA-seq data.

    **Data Analysis & Visualisation Projects**  
    Exploratory data analysis using Python and interactive dashboards.
    """
)

st.divider()

pdf_bytes = generate_cv_pdf()

st.download_button(
    label="⬇️ Download CV (PDF)",
    data=pdf_bytes,
    file_name="Yuvaan_Bhimsan_CV.pdf",
    mime="application/pdf"
)

st.caption("Generated with Streamlit | Coding Summer School 2026")
