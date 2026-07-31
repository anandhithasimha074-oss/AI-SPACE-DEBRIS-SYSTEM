import requests
import time


API_URL = "http://127.0.0.1:8000/predict"


class RaspberryController:

    def __init__(self):

        self.status = "Idle"


    def get_ai_decision(self):

        try:

            response = requests.get(API_URL)

            data = response.json()

            return data


        except Exception as e:

            print("API Connection Error:", e)

            return None



    def execute_maneuver(self, decision):

        if decision is None:
            print("No decision received")
            return


        prediction = decision["predictions"][0]

        maneuver = prediction["recommended_maneuver"]


        print("=" * 50)
        print("Raspberry Pi Satellite Controller")
        print("=" * 50)


        print("Satellite:",
              decision["satellite_1"])

        print("Risk:",
              prediction["status"])


        print("Action:",
              maneuver["recommended_action"])


        print("Fuel Usage:",
              maneuver["fuel_consumption"])


        print("Reason:",
              maneuver["reason"])


        print("=" * 50)



    def run(self):

        while True:

            decision = self.get_ai_decision()

            self.execute_maneuver(decision)

            time.sleep(60)



if __name__ == "__main__":

    controller = RaspberryController()

    controller.run()