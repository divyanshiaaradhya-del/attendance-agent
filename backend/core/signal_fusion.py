# backend/core/signal_fusion.py
from datetime import datetime

class SignalFusion:
    def __init__(self):
        self.synchronized_history = []

    def sync_signals(self, vision_data, audio_data):
        """
        Aggregates vision and audio signals into a unified data representation
        using timestamp-based synchronization.
        """
        unified_signal = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "vision_module": vision_data,
            "audio_module": audio_data
        }
        
        self.synchronized_history.append(unified_signal)
        return unified_signal