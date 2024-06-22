import pdfplumber
import docx
import re


def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = [page.extract_text() for page in pdf.pages]
    return "\n".join(full_text)


def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    full_text = [para.text for para in doc.paragraphs]
    return "\n".join(full_text)


def extract_personal_info(text):
    personal_info = {"Name": None, "Email": None, "Phone": None, "Address": None}

    # Extract Name
    name_pattern = r"([A-Z][a-z]+\s[A-Z][a-z]+)"
    name_match = re.search(name_pattern, text)
    if name_match:
        personal_info["Name"] = name_match.group(0)

    # Extract Email
    email_pattern = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    email_match = re.search(email_pattern, text)
    if email_match:
        personal_info["Email"] = email_match.group(0)

    # Extract Phone Number
    phone_pattern = r"(\(\d{3}\) \d{3}-\d{4})"
    phone_match = re.search(phone_pattern, text)
    if phone_match:
        personal_info["Phone"] = phone_match.group(0)

    # Extract Address
    address_pattern = r"([A-Z][a-z]+,\s[A-Z]{2})"
    address_match = re.search(address_pattern, text)
    if address_match:
        personal_info["Address"] = address_match.group(0)

    print("Personal Information:")
    print(f"Name: {personal_info['Name']}")
    print(f"Email: {personal_info['Email']}")
    print(f"Phone: {personal_info['Phone']}")
    print(f"Address: {personal_info['Address']}")
    print("\n")


def extract_professional_experience(text):
    job_titles = []
    companies = []
    durations = []

    # Extract job titles
    job_title_pattern = r"([A-Z][a-z]+\s[A-Z][a-z]+\sat\s[A-Z][a-z]+(?:\s[A-Z][a-z]+)*)"
    job_title_matches = re.findall(job_title_pattern, text)
    if job_title_matches:
        job_titles.extend(job_title_matches)
    else:
        print("No job titles found")

    # Extract companies
    company_pattern = r"at\s([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)"
    company_matches = re.findall(company_pattern, text)
    if company_matches:
        companies.extend(company_matches)
    else:
        print("No companies found")

    # Extract durations
    duration_pattern = r"([A-Z][a-z]+\s\d{4}\s-\s(?:Present|\w+\s\d{4}))"
    duration_matches = re.findall(duration_pattern, text)
    if duration_matches:
        durations.extend(duration_matches)
    else:
        print("No durations found")

    print("\nProfessional Experience:")
    print(f"Job Titles: {job_titles}")
    print(f"Companies: {companies}")
    print(f"Durations: {durations}")
    print("\n")


def extract_education(text):
    education_info = {"Degree": None, "Institution": None, "Graduation Year": None}

    # Extract Degree
    degree_pattern = (
        r"(Bachelor|Master|Ph\.D)\sof\s[A-Z][a-z]+\sin\s([A-Z][a-z]+\s[A-Z][a-z]+)"
    )
    degree_match = re.search(degree_pattern, text)
    if degree_match:
        education_info["Degree"] = degree_match.group(0)

    # Extract Institution
    institution_pattern = r"at\s([A-Z][a-z]+\s[A-Z][a-z]+(?:\sCollege)*)"
    institution_match = re.search(institution_pattern, text)
    if institution_match:
        education_info["Institution"] = institution_match.group(0)

    # Extract Graduation Year
    graduation_pattern = r"\s\d{4}\s-\s(?:Present|\d{4})"
    graduation_match = re.search(graduation_pattern, text)
    if graduation_match:
        education_info["Graduation Year"] = graduation_match.group(0)

    print("\nOverall Education:")
    print(f"Degree: {education_info['Degree']}")
    print(f"Institution: {education_info['Institution']}")
    print(f"Graduation Year: {education_info['Graduation Year']}")
    print("\n")


def extract_skills(text):
    programming_languages = {"python", "java", "c++", "javascript"}
    databases = {"mongodb", "sql", "postgresql", "mysql"}
    tools = {"git", "docker", "jenkins", "aws"}

    skills = {"Programming Languages": [], "Databases": [], "Tools": []}

    # Extract programming languages
    for lang in programming_languages:
        if lang in text.lower():
            skills["Programming Languages"].append(lang)

    # Extract databases
    for db in databases:
        if db in text.lower():
            skills["Databases"].append(db)

    # Extract tools
    for tool in tools:
        if tool in text.lower():
            skills["Tools"].append(tool)

    print("\nSkills:")
    for category, skill_list in skills.items():
        print(f"{category}: {skill_list}")
    print("\n")


def extract_information(file_paths):
    for file in file_paths:
        if file.endswith(".pdf"):
            text = extract_text_from_pdf(file)
        elif file.endswith(".docx"):
            text = extract_text_from_docx(file)
        elif file.endswith(".txt"):
            with open(file, "r") as f:
                text = f.read()
                f.close()
        else:
            continue

        # Print extracted information for each file
        print(f"File: {file}")
        extract_personal_info(text)
        extract_professional_experience(text)
        extract_education(text)
        extract_skills(text)


if __name__ == "__main__":
    file_paths = ["resume_sample2.pdf"]  # Replace with your actual file paths
    extracted_data = extract_information(file_paths)
