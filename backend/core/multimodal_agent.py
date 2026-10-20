# backend/core/multimodal_agent.py

class MultimodalAgent:
    def __init__(self):
        # Setting up rule-based thresholds
        self.min_faces = 1

    def estimate_engagement(self, vision_data, audio_data):
        """
        Applies rule-based reasoning to interpret combined multimodal data.
        """
        engagement_score = 0
        status = "Low Engagement"

        faces = vision_data.get("face_count", 0)
        audio_label = audio_data.get("label", "silence")

        # Rule 1: Student is present and speaking (Active Participation)
        if faces >= self.min_faces and audio_label == "speech":
            engagement_score = 100
            status = "High Engagement"
        
        # Rule 2: Student is present but silent (Listening/Focusing)
        elif faces >= self.min_faces and audio_label == "silence":
            engagement_score = 75
            status = "Medium Engagement"
            
        # Rule 3: Background noise but no faces, or empty room (Distracted/Absent)
        else:
            engagement_score = 25
            status = "Low Engagement"

        return {
            "score": engagement_score,
            "status": status,
            "reasoning": f"Faces: {faces}, Audio: {audio_label}"
        }