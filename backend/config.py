"""
Configuration settings for AI Space Debris Tracking System
"""

# ==========================
# API CONFIGURATION
# ==========================
API_TITLE = "AI Space Debris Tracking API"
API_VERSION = "1.0"

# ==========================
# SATELLITE DATA
# ==========================
CELESTRAK_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

# ==========================
# COLLISION PREDICTION
# ==========================
SAFE_DISTANCE = 50  # km
SATELLITES_TO_ANALYZE = 5
PREDICTION_INTERVALS = [0, 5, 10]  # minutes

# ==========================
# DATABASE
# ==========================
DATABASE_NAME = "space_debris.db"

# ==========================
# LOGGING
# ==========================
LOG_FILE = "backend.log"
LOG_LEVEL = "INFO"

# ==========================
# DIGITAL TWIN
# ==========================
DIGITAL_TWIN_ENABLED = True

# ==========================
# REINFORCEMENT LEARNING
# ==========================
RL_ENABLED = True

# ==========================
# EXPLAINABLE AI
# ==========================
XAI_ENABLED = True