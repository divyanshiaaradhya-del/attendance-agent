# run_scoring_test.py
from backend.core.scoring_logic import EngagementScorer

scorer = EngagementScorer()

print("Testing Engagement Scoring Logic...")

# Simulating 3 different time segments of a class
mock_fused_signals = [
    {
        "timestamp": "12:15:00",
        "vision_module": {"face_count": 1, "movement": "high"},
        "audio_module": {"label": "speech"}  # Active participation
    },
    {
        "timestamp": "12:15:05",
        "vision_module": {"face_count": 1, "movement": "low"},
        "audio_module": {"label": "silence"} # Listening quietly
    },
    {
        "timestamp": "12:15:10",
        "vision_module": {"face_count": 0, "movement": "none"},
        "audio_module": {"label": "silence"} # Absent/Distracted
    }
]

# Generate the temporal profile
temporal_profile = scorer.compute_temporal_score(mock_fused_signals)

for profile in temporal_profile:
    print(f"Time: {profile['timestamp']} | Score: {profile['engagement_score']}")