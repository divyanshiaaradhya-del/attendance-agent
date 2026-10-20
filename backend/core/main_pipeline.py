# main_pipeline.py
import time
from backend.core.signal_fusion import SignalFusion
from backend.core.multimodal_agent import MultimodalAgent
from backend.core.scoring_logic import EngagementScorer
from backend.core.ai_suggestion import AISuggestionEngine
from backend.core.analytics_service import AnalyticsService

def run_pipeline():
    print("Starting End-to-End Application Pipeline...\n")
    
    # Initialize all our modules
    fusion = SignalFusion()
    agent = MultimodalAgent()
    scorer = EngagementScorer()
    ai_engine = AISuggestionEngine()
    analytics = AnalyticsService()

    # Simulating a live webcam frame and audio chunk
    print("Capturing live input...")
    vision_data = {"face_count": 1, "movement": "high"}
    audio_data = {"label": "speech", "db": -40}
    time.sleep(1)

    # 1. Signal Fusion
    fused_data = fusion.sync_signals(vision_data, audio_data)
    print(f"[1] Fused Signal Timestamp: {fused_data['timestamp']}")

    # 2. Multimodal Reasoning
    engagement = agent.estimate_engagement(fused_data["vision_module"], fused_data["audio_module"])
    print(f"[2] Real-time Status: {engagement['status']} (Base Score: {engagement['score']})")

    # 3. Temporal Scoring
    profile = scorer.compute_temporal_score([fused_data])
    print(f"[3] Computed Temporal Score: {profile[0]['engagement_score']}")

    # 4. AI Suggestion Engine
    suggestion = ai_engine.generate_suggestions(fused_data)
    print(f"[4] Teaching Suggestion: {suggestion}")

    # 5. Session Analytics
    session_stats = analytics.get_session_trends(session_id=101)
    print(f"[5] End-of-Session Summary: {session_stats['summary']}\n")
    
    print("Pipeline execution completed successfully!")

if __name__ == "__main__":
    run_pipeline()