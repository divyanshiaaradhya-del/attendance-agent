# run_ai_test.py
from backend.core.signal_fusion import SignalFusion
from backend.core.ai_suggestion import AISuggestionEngine

fusion = SignalFusion()
ai_engine = AISuggestionEngine()

print("Testing Fusion + AI...")

# 1. Create mock data and fuse it
vision_data = {"face_count": 1, "movement": "low"}
audio_data = {"label": "silence", "db": -45}
fused_data = fusion.sync_signals(vision_data, audio_data)

# 2. Get AI suggestion based on the fused data
print("Fused Data:", fused_data)
suggestion = ai_engine.generate_suggestions(fused_data)
print("Result:", suggestion)