from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class AboutView(View):
    def get(self,request):
        data = {
            "iD" : 1,
            "Full_Name" : "Devana K",
            "Title" : "Python Django Intern",
            "Bio" : "A passionate hardwokring achevier",
            "DOB" : "04/12/2000",
            "Email" : "Devana@gmail.com",
            "Conatct" : "09876543287",
            "Location" : "Kannur",
            "Github_URL" : "https://github.com/in/devana08",
            "linkedin_URL" : "https://Linkedin.com/in/devana08",
            
        }
        return JsonResponse(data)
    
class EducationView(View):
    def get(self,request):
        data = {
            "id": 101, 
            "institution": "Luminar", 
            "course": "Python Full Stack", 
            "university": "ABC University", 
            "location": "Cochin", 
            "starting_year": "June 2026", 
            "ending_year": "January 2027", 
            "cgpa": "9.5", 
            "description": "Completed Python Full Stack Development." 
            
        }
        return(JsonResponse(data))
    
class ProjectView(View):
    def get(self,request):
        projects = [
            { 
            "id": 1, 
            "title": "DietLense", 
            "short_description": "AI-powered food recognition application.", 
            "long_description": "An application that analyzes food images and provides nutritional information.", 
            "technologies_used": [ 
                "Python", 
                "Django", 
                "Google GenAI SDK" ], 
            "live_url": "https://dietlense.example.com", 
            "github_url": "https://github.com/username/dietlense", 
            "image_url": "https://example.com/dietlense.jpg", 
            "featured": "true",
                                }, 
            { 
                "id": 2, 
                "title": "Interview Prep Blog", 
                "short_description": "Educational application for programming interviews.", 
                "long_description": "A platform for practicing technical interview questions and reading programming articles.", 
                "technologies_used": [ 
                    "Python", 
                    "Django", 
                "JavaScript" 
                            ], 
                "live_url": "https://prep.example.com", 
                "github_url": "https://github.com/username/interview-prep", 
                "image_url": "https://example.com/interview.jpg", 
                "featured": "true", 
                                     },
            {
                "id": 3,
                "title": "Student Management System",
                "short_description": "Web application for managing student information.",
                "long_description": "A system for adding, updating, deleting, and viewing student records with an easy-to-use interface.",
                "technologies_used": [
                            "Python",
                            "Django",
                            "MySQL",
                            "HTML",
                            "CSS",
                            "JavaScript"
                                            ],
                "live_url": "https://student.example.com",
                "github_url": "https://github.com/username/student-management",
                "image_url": "https://example.com/student.jpg",
                "featured": "true",
                                     },
        ]
        return JsonResponse(projects, safe=False)
    
class skillsView(View):
    def get(self,request):
        data =[ 
               { 
                    "id": 1, 
                    "skill_name": "Python", 
                    "category": "Programming Language", 
                    "proficiency": "Advanced", 
                    "years_of_experience": 4 },
               {
                   "id": 2, 
                    "skill_name": "Django", 
                    "category": "Backend", 
                    "proficiency": "Advanced", 
                    "years_of_experience": 3
                   
               },
               {
                   "id": 3, 
                "skill_name": "React", 
                "category": "Frontend", 
                "proficiency": "Intermediate", 
                "years_of_experience": 2 
               },
        ]
        return JsonResponse(data, safe=False)
            
            
            
    
    

