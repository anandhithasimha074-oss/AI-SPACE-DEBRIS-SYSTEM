class ExplainableAI:

    def __init__(self):
        self.explanations = []

    def analyze(self, distance, risk_status):

        self.explanations = []

        # Risk Analysis
        if distance < 50:
            self.explanations.append(
                "Distance between satellites is below the minimum safe threshold."
            )
            confidence = "99%"

        elif distance < 200:
            self.explanations.append(
                "Satellites are approaching each other and require close monitoring."
            )
            confidence = "90%"

        elif distance < 500:
            self.explanations.append(
                "Moderate separation detected. Continue monitoring orbital paths."
            )
            confidence = "75%"

        else:
            self.explanations.append(
                "Satellites are maintaining a safe separation distance."
            )
            confidence = "99%"

        # Trajectory Analysis
        if risk_status == "Collision Risk":
            self.explanations.append(
                "Future orbital trajectory indicates a possible collision."
            )

            recommendation = (
                "Perform a small orbital maneuver to increase separation."
            )

        else:
            self.explanations.append(
                "Current orbital trajectory is stable with no immediate collision risk."
            )

            recommendation = (
                "Continue normal monitoring."
            )

        return {
            "risk_status": risk_status,
            "confidence": confidence,
            "distance_km": float(round(distance, 2)),
            "explanation": self.explanations,
            "recommended_action": recommendation
        }


def explain_collision(distance, risk_status):

    xai = ExplainableAI()

    return xai.analyze(distance, risk_status)