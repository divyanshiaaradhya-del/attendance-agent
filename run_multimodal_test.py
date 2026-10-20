# run_multimodal_test.py
from backend.core.multimodal_agent import MultimodalAgent

agent = MultimodalAgent()

# Test Case 1: Student present and talking
vision_data_1 = {"face_count": 1}
audio_data_1 = {"label": "speech"}
print("Test 1 (Active):", agent.estimate_engagement(vision_data_1, audio_data_1))

# Test Case 2: Student present but quiet
vision_data_2 = {"face_count": 1}
audio_data_2 = {"label": "silence"}
print("Test 2 (Listening):", agent.estimate_engagement(vision_data_2, audio_data_2))

# Test Case 3: Empty room with noise
vision_data_3 = {"face_count": 0}
audio_data_3 = {"label": "speech"}
print("Test 3 (Distracted/Absent):", agent.estimate_engagement(vision_data_3, audio_data_3))