import requests

def analyze_resume(resume_text,job_description):
	url = "http://localhost:11434/api/generate"

	prompt = f"""
	Role: You are an expert ATS system used by large tech companies.

	Task:
	Evaluate how well the candidate's resume matches the job description.

	Instructions:
	1. Calculate ATS match score (0-100).
	2. Identify key strengths in the resume.
	3. Identify missing skills compared to the job description.
	4. Suggest improvements to increase ATS score.

	Output Format:
	ATS Score:
	Strengths:
	Missing Skills:
	Suggestions:

	Resume:
	{resume_text}

	Job Description:
	{job_description}
	"""

	payload = {
		"model": "llama3",
		"prompt": prompt,
		"stream": False
	}

	response = requests.post(url, json=payload)

	if response.status_code != 200:
		return "Error contacting AI Model."

	try:
		result = response.json()
		return result.get("response", "No response from model.")

	except Exception:
		return "Error: Invalid response from AI model."