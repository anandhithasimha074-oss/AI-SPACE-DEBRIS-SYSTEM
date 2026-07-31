class ReinforcementAgent:

    def __init__(self):

        self.actions = [
            "No Maneuver",
            "Increase Altitude",
            "Decrease Altitude",
            "Change Orbit"
        ]


    def choose_action(self, risk_status, distance):

        if risk_status == "Collision Risk":

            if distance < 20:
                action = "Change Orbit"
                fuel = "High"

            elif distance < 50:
                action = "Increase Altitude"
                fuel = "Medium"

            else:
                action = "No Maneuver"
                fuel = "Low"

        else:
            action = "No Maneuver"
            fuel = "Zero"


        return {
            "recommended_action": action,
            "fuel_consumption": fuel,
            "reason": self.get_reason(action)
        }


    def get_reason(self, action):

        reasons = {

            "No Maneuver":
                "Current trajectory is safe, no correction required",

            "Increase Altitude":
                "Altitude adjustment provides safer separation from debris",

            "Decrease Altitude":
                "Lower orbit adjustment reduces collision probability",

            "Change Orbit":
                "Major trajectory correction required due to high collision risk"
        }

        return reasons[action]


def reinforcement_decision(risk_status, distance):

    agent = ReinforcementAgent()

    return agent.choose_action(
        risk_status,
        distance
    )