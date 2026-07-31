class ExplainableAI:

    def __init__(self):
        self.explanations = []


    def analyze(self, distance, risk_status):

        self.explanations = []

        if distance < 50:
            self.explanations.append(
                "Distance between satellite and debris is below safe threshold"
            )

        else:
            self.explanations.append(
                "Distance between objects is within safe limits"
            )


        if risk_status == "Collision Risk":
            self.explanations.append(
                "Trajectory analysis indicates possible collision risk"
            )

        else:
            self.explanations.append(
                "Current orbital path does not indicate immediate collision"
            )


        return {
            "risk_status": risk_status,
            "explanation": self.explanations
        }


def explain_collision(distance, risk_status):

    xai = ExplainableAI()

    return xai.analyze(distance, risk_status)