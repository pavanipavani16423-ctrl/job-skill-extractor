import os
from dotenv import load_dotenv
from model import extract_skills

load_dotenv()

def main():
    print("=" * 50)
    print("🧠 Job Description Skill Extractor")
    print("=" * 50)
    
    print("\nPaste your Job Description below.")
    print("(When done, press Enter twice)\n")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    job_description = "\n".join(lines)
    
    if not job_description.strip():
        print("❌ No input provided. Exiting.")
        return
    
    print("\n⏳ Extracting skills... please wait...\n")
    
    result = extract_skills(job_description)
    
    print("✅ Extraction Complete!\n")
    print("=" * 50)
    print(f"🏷️  Job Title       : {result.get('job_title', 'N/A')}")
    print(f"💼 Experience      : {result.get('experience', 'N/A')}")
    print(f"🎓 Education       : {result.get('education', 'N/A')}")
    print(f"\n🛠️  Required Skills :")
    for skill in result.get('required_skills', []):
        print(f"   • {skill}")
    print(f"\n💻 Tools & Tech    :")
    for tool in result.get('tools_technologies', []):
        print(f"   • {tool}")
    print(f"\n🤝 Soft Skills     :")
    for soft in result.get('soft_skills', []):
        print(f"   • {soft}")
    print("=" * 50)

if __name__ == "__main__":
    main()