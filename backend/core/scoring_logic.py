# backend/core/scoring_logic.py

class EngagementScorer:
    def __init__(self):
        # Predefined thresholds for rule-based logic
        self.base_score = 50
        
    def compute_temporal_score(self, fused_signals):
        """
        Transforms a list of fused multimodal signals into a temporal engagement profile.
        """
        temporal_profile = []
        
        for signal in fused_signals:
            score = self.base_score
            vision = signal.get("vision_module", {})
            audio = signal.get("audio_module", {})
            
            # Rule-based scoring
            if vision.get("face_count", 0) > 0:
                score += 20
            
            if vision.get("movement") == "high":
                score += 10
            elif vision.get("movement") == "low":
                score -= 10
                
            if audio.get("label") == "speech":
                score += 20
            elif audio.get("label") == "silence":
                score -= 5
                
            # Cap the score between 0 and 100
            final_score = max(0, min(100, score))
            
            temporal_profile.append({
                "timestamp": signal.get("timestamp"),
                "engagement_score": final_score
            })
            
        return temporal_profile