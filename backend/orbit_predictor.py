from skyfield.api import load


def predict_satellite_positions():
    print("Loading satellite data...")

    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"
    satellites = load.tle_file(url)

    ts = load.timescale()
    t = ts.now()

    satellite_positions = []

    print(f"\nLoaded {len(satellites)} satellites.\n")

    for satellite in satellites[:10]:

        geocentric = satellite.at(t)
        subpoint = geocentric.subpoint()

        velocity = geocentric.velocity.km_per_s
        speed = (velocity[0]**2 + velocity[1]**2 + velocity[2]**2) ** 0.5

        satellite_info = {
            "name": satellite.name,
            "latitude": round(subpoint.latitude.degrees, 2),
            "longitude": round(subpoint.longitude.degrees, 2),
            "altitude": round(subpoint.elevation.km, 2),
            "velocity": round(speed, 2),
            "status": "SAFE"
        }

        satellite_positions.append(satellite_info)

    return satellite_positions


if __name__ == "__main__":

    satellites = predict_satellite_positions()

    print("Current Satellite Positions\n")

    for satellite in satellites:

        print(f"Satellite : {satellite['name']}")
        print(f"Latitude  : {satellite['latitude']}°")
        print(f"Longitude : {satellite['longitude']}°")
        print(f"Altitude  : {satellite['altitude']} km")
        print(f"Velocity  : {satellite['velocity']} km/s")
        print(f"Status    : {satellite['status']}")
        print("-" * 50)