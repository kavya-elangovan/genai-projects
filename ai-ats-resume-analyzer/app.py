import streamlit as st
from resume_parser import extract_resume_text
from ai_analyzer import analyze_resume

st.set_page_config(page_title = "AI ATS REsume Analyzer")

st.title("AI ATS Resume Analyzer")
st.write("Upload your resume and compare it with a job description.")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

job_description = st.text_area("Enter your job description")

if st.button("Analyze Resume"):
	if uploaded_file is not None and job_description != "":
		resume_text = extract_resume_text(uploaded_file)

		with st.spinner("AI is analyzing your resume..."):
			result = analyze_resume(resume_text,job_description)

		st.success("Analysis Completed!")		

		st.subheader("ATS Resume Evaluation")
		st.write(result)
	else:
		st.warning("Please upload resume as PDF and enter the job description")