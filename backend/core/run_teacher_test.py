# run_teacher_test.py
from backend.core.teacher_profiles import TeacherProfileService

service = TeacherProfileService()

print("Fetching Teacher Profile...")
profile = service.get_profile(teacher_id="TCH-001")

print(f"Teacher ID: {profile['teacher_id']}")
print(f"Effectiveness Score: {profile['effectiveness_score']}")
print("Class History:")
for cls in profile['class_history']:
    print(f" - {cls['name']}: {cls['engagement']}% engagement")