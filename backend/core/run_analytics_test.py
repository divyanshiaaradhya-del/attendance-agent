# run_analytics_test.py
from backend.core.analytics_service import AnalyticsService

service = AnalyticsService()

print("Generating Student Session Analytics...")
analytics = service.get_session_trends(session_id=101)

print(f"\nSession ID: {analytics['session_id']}")
print(f"Attendance Duration: {analytics['attendance_duration_mins']} mins")
print(f"Engagement Consistency: {analytics['engagement_consistency']}")
print("\nEngagement Timeline:")
for event in analytics['timeline']:
    print(f" - [{event['timestamp']}] {event['status']}")
    
print(f"\nSummary: {analytics['summary']}")