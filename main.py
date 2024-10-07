from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Models for request and response
class UserProfile(BaseModel):
    name: str
    skills: List[str]
    experience_level: str
    preferences: Dict[str, List[str]]

class JobPosting(BaseModel):
    job_title: str
    company: str
    location: str
    job_type: str
    required_skills: List[str]
    experience_level: str

class RecommendationRequest(BaseModel):
    user: UserProfile
    jobs: List[JobPosting]

@app.post("/recommendations", response_model=List[JobPosting])
def get_recommendations(request: RecommendationRequest):
    user = request.user
    jobs = request.jobs
    
    if not jobs:
        raise HTTPException(status_code=400, detail="No job postings provided")

    recommendations = []

    for job in jobs:
        # Match job title with desired roles
        if job.job_title not in user.preferences['desired_roles']:
            continue
        
        # Match job location
        if job.location not in user.preferences['locations']:
            continue
        
        # Match job type
        if job.job_type != user.preferences['job_type']:
            continue
        
        # Match required skills
        matched_skills = set(user.skills) & set(job.required_skills)
        if not matched_skills:
            continue  # No skill match, skip this job
        
        # Match experience level (assuming a simple equality check)
        if job.experience_level != user.experience_level:
            continue  # Experience level does not match
        
        # If all checks passed, add job to recommendations
        recommendations.append(job)

    return recommendations

# To run the app, use the command:
# uvicorn script_name:app --reload
