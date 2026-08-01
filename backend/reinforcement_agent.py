class ReinforcementAgent:

    def __init__(self):

        self.actions = [
            "No Maneuver",
            "Increase Altitude",
            "Decrease Altitude",
            "Change Orbit",
            "Emergency Collision Avoidance"
        ]

    def choose_action(self, risk_status, distance):

        if distance < 20:
            action = "Emergency Collision Avoidance"
            fuel = "Very High"
            priority = "Critical"

        elif distance < 50:
            action = "Change Orbit"
            fuel = "High"
            priority = "High"

        elif distance < 200:
            action = "Increase Altitude"
            fuel = "Medium"
            priority = "Medium"

        elif distance < 500:
            action = "Decrease Altitude"
            fuel = "Low"
            priority = "Low"

        else:
            action = "No Maneuver"
            fuel = "Zero"
            priority = "Normal"

        return {
            "recommended_action": action,
            "priority": priority,
            "fuel_consumption": fuel,
            "reason": self.get_reason(action)
        }

    def get_reason(self, action):

        reasons = {

            "No Maneuver":
                "Current orbital path is safe. Continue monitoring.",

            "Increase Altitude":
                "Increasing altitude provides greater separation from nearby objects.",

            "Decrease Altitude":
                "Lowering the orbit increases separation while conserving fuel.",

            "Change Orbit":
                "A significant orbital adjustment is recommended due to elevated collision risk.",

            "Emergency Collision Avoidance":
                "Immediate evasive maneuver required to prevent a possible collision."
        }

        return reasons[action]


def reinforcement_decision(risk_status, distance):

    agent = ReinforcementAgent()

    return agent.choose_action(risk_status, distance) 