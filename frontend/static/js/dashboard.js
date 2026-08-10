
document.addEventListener("DOMContentLoaded", function () {

    console.log("AI Space Debris Tracking System Running");
    

    // -----------------------------
    // Debris Activity Chart
    // -----------------------------

    const debrisChartCanvas = document.getElementById("debrisChart");
    let debrisChart;
    alert(typeof Chart);

    if (debrisChartCanvas) {

        debrisChart = new Chart(debrisChartCanvas, {
    type: "line",
    data: {
        labels: ["00:00","04:00","08:00","12:00","16:00","20:00"],
        datasets: [{
            label: "Tracked Debris Objects",
            data: [820,950,1100,1180,1250,1320],
            borderColor: "#38bdf8",
            backgroundColor: "rgba(56,189,248,0.1)",
            borderWidth: 3,
            fill: true,
            tension: 0.4
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

    }

    // -----------------------------
    // Collision Risk Chart
    // -----------------------------

    const riskChartCanvas = document.getElementById("riskChart");
    let riskChart;

    if (riskChartCanvas) {

        riskChart = new Chart(riskChartCanvas, {
    type: "line",
    data: {
        labels: ["Day 1","Day 2","Day 3","Day 4","Day 5","Day 6"],
        datasets: [{
            label: "Collision Risk %",
            data: [4,6,5,8,3,2],
            borderColor: "#38bdf8",
            backgroundColor: "rgba(248, 56, 56, 0.24)",
            borderWidth: 3,
            fill: true,
            tension: 0.4
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

    }

    // -----------------------------
    // Live Dashboard Simulation
    // -----------------------------

    function random(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    function updateDashboard() {

        const detected = random(1200, 1400);
        const tracked = random(34000, 36000);
        const probability = random(1, 10);
        const confidence = random(90, 99);
        // Satellite Health Simulation

const battery = random(80, 100);
const fuel = random(60, 95);
const signal = random(85, 100);

        const nearestObject = "DEB-" + random(1000, 9999);

        let risk = "LOW";

        if (probability >= 7) {
            risk = "HIGH";
        } else if (probability >= 4) {
            risk = "MEDIUM";
        }
        // -----------------------------
// Mission Alert Banner
// -----------------------------

const alertBanner = document.getElementById("alert-banner");

if (alertBanner) {

    if (risk === "LOW") {

        alertBanner.className = "alert-normal";

        alertBanner.innerHTML =
        "🟢 NORMAL OPERATION • All satellites are operating normally.";

    }

    else if (risk === "MEDIUM") {

        alertBanner.className = "alert-medium";

        alertBanner.innerHTML =
        "🟡 MEDIUM COLLISION RISK DETECTED • Continue monitoring.";

    }

    else {

        alertBanner.className = "alert-high";

        alertBanner.innerHTML =
        "🔴 HIGH COLLISION RISK • Avoidance maneuver recommended.";

    }

}

        // Update text values

        if (document.getElementById("objects-detected"))
            document.getElementById("objects-detected").textContent = detected;

        if (document.getElementById("objects-tracked"))
            document.getElementById("objects-tracked").textContent = tracked;

        if (document.getElementById("tracking-count"))
            document.getElementById("tracking-count").textContent = tracked;

        if (document.getElementById("collision-probability"))
            document.getElementById("collision-probability").textContent = probability + "%";

        if (document.getElementById("mission-probability"))
            document.getElementById("mission-probability").textContent = probability + "%";

        if (document.getElementById("ai-confidence"))
            document.getElementById("ai-confidence").textContent = confidence + "%";

        if (document.getElementById("nearest-object"))
            document.getElementById("nearest-object").textContent = nearestObject;

        if (document.getElementById("risk-level")) {

            const riskElement = document.getElementById("risk-level");

            riskElement.textContent = risk;

            if (risk === "LOW") {

                riskElement.style.color = "#22c55e";

            } else if (risk === "MEDIUM") {

                riskElement.style.color = "#facc15";

            } else {

                riskElement.style.color = "#ef4444";

            }

        }

        if (document.getElementById("mission-risk")) {

            const missionRisk = document.getElementById("mission-risk");

            missionRisk.textContent = risk;

            if (risk === "LOW") {

                missionRisk.style.color = "#22c55e";

            } else if (risk === "MEDIUM") {

                missionRisk.style.color = "#facc15";

            } else {

                missionRisk.style.color = "#ef4444";

            }

        }

        // Update charts

        if (debrisChart) {

            debrisChart.data.datasets[0].data.shift();
            debrisChart.data.datasets[0].data.push(detected);
            debrisChart.update();

        }

        if (riskChart) {

            riskChart.data.datasets[0].data.shift();
            riskChart.data.datasets[0].data.push(probability);
            riskChart.update();

        }
        // -----------------------------
// Satellite Health Bars
// -----------------------------

const batteryBar = document.getElementById("battery-bar");

if (batteryBar) {

    batteryBar.style.width = battery + "%";
    batteryBar.innerHTML = battery + "%";

}

const fuelBar = document.getElementById("fuel-bar");

if (fuelBar) {

    fuelBar.style.width = fuel + "%";
    fuelBar.innerHTML = fuel + "%";

}

const signalBar = document.getElementById("signal-bar");

if (signalBar) {

    signalBar.style.width = signal + "%";
    signalBar.innerHTML = signal + "%";

}

    }

 // Run dashboard once
updateDashboard();

// Mission timer starts
const missionStart = new Date();

function updateClock() {

    const now = new Date();

    // UTC Time
    const utc = now.toUTCString().split(" ")[4] + " UTC";

    const utcElement = document.getElementById("utc-time");

    if (utcElement) {

        utcElement.textContent = utc;

    }

    // Last Update
    const updateElement = document.getElementById("last-update");

    if (updateElement) {

        updateElement.textContent = "Last Update: " + now.toLocaleTimeString();

    }

    // Mission Timer
    const diff = Math.floor((now - missionStart) / 1000);

    const hrs = String(Math.floor(diff / 3600)).padStart(2, "0");
    const mins = String(Math.floor((diff % 3600) / 60)).padStart(2, "0");
    const secs = String(diff % 60).padStart(2, "0");

    const missionElement = document.getElementById("mission-time");

    if (missionElement) {

        missionElement.textContent =
            "Mission Time: T+" + hrs + ":" + mins + ":" + secs;

    }

}

// Update clock every second
setInterval(updateClock, 1000);

// Update dashboard every 5 seconds
setInterval(updateDashboard, 5000);

// Run clock immediately
updateClock();   
});
// =============================
// Search Function
// =============================

const searchInput = document.querySelector(".search-box input");
const searchButton = document.querySelector(".search-box button");

if (searchButton) {

    searchButton.addEventListener("click", function () {

        const value = searchInput.value.trim().toUpperCase();

        if (value === "") {

            alert("Please enter a Satellite ID or Debris ID.");

        } else {

            alert("Searching for: " + value);

        }

    });

}
// =============================
// Simulation Controls
// =============================

let simulationRunning = false;
let simulationInterval;

const startBtn = document.querySelector(".start-btn");
const pauseBtn = document.querySelector(".pause-btn");
const resetBtn = document.querySelector(".reset-btn");
console.log("Start Button:", startBtn);
console.log("Pause Button:", pauseBtn);
console.log("Reset Button:", resetBtn);

if (startBtn) {

    startBtn.addEventListener("click", () => {
        console.log("start button clicked");

        if (simulationRunning) return;

        simulationRunning = true;
        document.getElementById("simulation-status").innerText = "RUNNING";

       simulationInterval = setInterval(() => {

    let debrisValue = Math.floor(35000 + Math.random() * 500);

    let riskValue = (Math.random() * 10).toFixed(2);


    if(document.getElementById("debris-count"))
        document.getElementById("debris-count").innerText = debrisValue;


    if(document.getElementById("collision-risk"))
        document.getElementById("collision-risk").innerText = riskValue + "%";


    if(document.getElementById("objects-detected"))
        document.getElementById("objects-detected").innerText =
        Math.floor(Math.random() * 300 + 1200);


    if(document.getElementById("collision-probability"))
        document.getElementById("collision-probability").innerText =
        riskValue + "%";


}, 2000);

    });

}

if (pauseBtn) {

    pauseBtn.addEventListener("click", () => {

        clearInterval(simulationInterval);
        simulationRunning = false;
        document.getElementById("simulation-status").innerText = "PAUSED";

    });

}

if (resetBtn) {

    resetBtn.addEventListener("click", () => {

        clearInterval(simulationInterval);
        simulationRunning = false;
        document.getElementById("simulation-status").innerText = "READY";

        document.getElementById("objects-detected").innerText = "1250";
        document.getElementById("collision-probability").innerText = "2%";

    });

}

// =============================
// Number Counting Animation
// =============================

function animateNumbers() {

    const numbers = document.querySelectorAll(".stat-number");

    numbers.forEach(number => {

        const value = number.innerText.replace(/,/g, "").replace("+","").replace("%","");
const target = Number(value);

        let count = 0;

        const speed = target / 80;

        function update(){

            count += speed;

            if(count < target){

                number.innerText = Math.floor(count).toLocaleString();

                requestAnimationFrame(update);

            }
            else{

                number.innerText = target.toLocaleString();

            }

        }

        update();

    });

}


window.addEventListener("load", animateNumbers);
// =============================
// Backend API Integration
// =============================

// =============================
// Backend API Integration
// =============================

async function loadSystemStatus() {

    try {

        const response = await fetch("http://127.0.0.1:8000/status");

        if (!response.ok) {
            throw new Error("Failed to fetch system status");
        }

        const data = await response.json();

        const systemStatus = document.getElementById("system-status");
        if (systemStatus) systemStatus.textContent = data.system;

        const aiModel = document.getElementById("ai-model-status");
        if (aiModel) aiModel.textContent = data.collision_detection;

        const monitor = document.getElementById("monitor-status");
        if (monitor) monitor.textContent = data.digital_twin;

        const connection = document.getElementById("connection-status");
        if (connection) connection.textContent = data.reinforcement_learning;

        console.log("Backend Connected:", data);

    } catch (error) {

        console.error("Status API Error:", error);

    }

}

loadSystemStatus();
setInterval(loadSystemStatus, 5000);
// =============================
// Collision Prediction API
// =============================

async function loadPrediction() {

    try {

        const response = await fetch("http://127.0.0.1:8000/predict");

        if (!response.ok) {
            throw new Error("Prediction API failed");
        }

        const data = await response.json();

        if (data.length > 0) {

            const prediction = data[0].predictions[0];
            
            // =============================
// Reinforcement Learning Data
// =============================

            const action = document.getElementById("monitoring-status");
            const priority = document.getElementById("threat-level");
            const fuel = document.getElementById("fuel-consumption");
            const reason = document.getElementById("maneuver-reason");

            if (action)
                action.textContent = prediction.recommended_action;

            if (priority)
                priority.textContent = prediction.priority;

            if (fuel)
                fuel.textContent = prediction.fuel_consumption;

            if (reason)
                reason.textContent = prediction.reason;
            // Satellite Protection
            const satelliteStatus = document.getElementById("satellite-status");
            const threatLevel = document.getElementById("threat-level");
            const monitoringStatus = document.getElementById("monitoring-status");

            if (satelliteStatus) {
                satelliteStatus.textContent =
                   prediction.recommended_action === "No Maneuver"
            ? "Protected"
            : "Action Required";
            }

            if (threatLevel) {
                threatLevel.textContent = prediction.priority;
            }

            if (monitoringStatus) {
                monitoringStatus.textContent = prediction.recommended_action;
            }

            // Existing Dashboard Updates
            const nearestObject = document.getElementById("nearest-object");
            if (nearestObject)
                nearestObject.textContent = data[0].satellite_2;

            const probability = document.getElementById("mission-probability");
            if (probability)
                probability.textContent = prediction.confidence + "%";

            const risk = document.getElementById("mission-risk");
            if (risk)
                risk.textContent = prediction.status;

            const approach = document.getElementById("closest-approach");
            if (approach)
                approach.textContent = prediction.distance_km + " km";
            // AI Maneuver Recommendation Card

const recommendedManeuver =
    document.getElementById("recommended-maneuver");

const maneuverFuel =
    document.getElementById("maneuver-fuel");

const maneuverConfidence =
    document.getElementById("maneuver-confidence");

const maneuverExplanation =
    document.getElementById("maneuver-explanation");

if (recommendedManeuver) {

    const action =
        prediction.recommended_action || "No maneuver required";

    recommendedManeuver.textContent = action;

    if (action === "No Maneuver") {

        recommendedManeuver.style.color = "#22c55e";

    } else if (
        action.toLowerCase().includes("monitor")
    ) {

        recommendedManeuver.style.color = "#facc15";

    } else {

        recommendedManeuver.style.color = "#ef4444";

    }
}
if (maneuverFuel)
    maneuverFuel.textContent =
        (prediction.fuel_consumption || "0") + "%";

if (maneuverConfidence)
    maneuverConfidence.textContent =
        (prediction.confidence || "0") + "%";

if (maneuverExplanation)
    maneuverExplanation.textContent =
        prediction.reason || "Waiting for collision analysis...";

            // New Collision Prediction Card Updates
            const predictionStatus = document.getElementById("prediction-status");
            if (predictionStatus)
                predictionStatus.textContent = prediction.status;

            const predictionDistance = document.getElementById("prediction-distance");
            if (predictionDistance)
                predictionDistance.textContent = prediction.distance_km + " km";

            const predictionVelocity = document.getElementById("prediction-velocity");
            if (predictionVelocity)
                predictionVelocity.textContent = prediction.relative_velocity_kms + " km/s";

            const predictionConfidence = document.getElementById("prediction-confidence");
            if (predictionConfidence)
                predictionConfidence.textContent = prediction.confidence + "%";

            console.log("Prediction Loaded:", prediction);
            console.log("🤖 AI MANEUVER DATA:", {
    action: prediction.recommended_action,
    fuel: prediction.fuel_consumption,
    confidence: prediction.confidence,
    reason: prediction.reason
});

        }

    } catch (error) {

        console.error("Prediction API Error:", error);

    }

}

loadPrediction();
setInterval(loadPrediction, 5000);

// =============================
// Digital Twin API Integration
// =============================

async function loadDigitalTwin() {

    try {

        const response = await fetch("http://127.0.0.1:8000/digital-twin");

        if (!response.ok) {
            throw new Error("Digital Twin API failed");
        }

        const data = await response.json();

        console.log("Digital Twin Data:", data);

        // Latitude
        const latitude = document.getElementById("digital-twin-latitude");

        if (latitude && data.latitude !== undefined) {
            latitude.textContent = data.latitude.toFixed(4) + "°";
        }

        // Longitude
        const longitude = document.getElementById("digital-twin-longitude");

        if (longitude && data.longitude !== undefined) {
            longitude.textContent = data.longitude.toFixed(4) + "°";
        }

        // Altitude
        const altitude = document.getElementById("digital-twin-altitude");

        if (altitude && data.altitude_km !== undefined) {
            altitude.textContent = data.altitude_km.toFixed(2) + " km";
        }

        // Fuel
        const fuel = document.getElementById("digital-twin-fuel");

        if (fuel && data.fuel_percentage !== undefined) {
            fuel.textContent = data.fuel_percentage + "%";
        }
        // Status
        const status = document.getElementById("digital-twin-status");

        if (status && data.risk_status !== undefined) {
            status.textContent = data.risk_status;
        }
        
 

    } catch (error) {

        console.error("Digital Twin API Error:", error);

    }

}

loadDigitalTwin();
setInterval(loadDigitalTwin, 5000);

// =============================
// Real-Time Satellite Fleet Data
// =============================

async function loadSatelliteFleet() {

    try {

        const response = await fetch("http://127.0.0.1:8000/satellites");

        if (!response.ok) {
            throw new Error("Satellite API failed");
        }

        const satellites = await response.json();

        const tableBody =
            document.getElementById("satellite-table-body");

        if (!tableBody) {
            console.error("Satellite table body not found");
            return;
        }

        tableBody.innerHTML = "";
        const updatedTime = new Date().toLocaleTimeString();

        satellites.forEach((satellite, index) => {

            let orbit = "LEO";

            if (
                satellite.altitude_km >= 2000 &&
                satellite.altitude_km < 35786
            ) {
                orbit = "MEO";

            } else if (satellite.altitude_km >= 35786) {
                orbit = "GEO";
            }

            const fuelLevels = [100, 90, 80, 70, 60];

            const fuel =
                fuelLevels[index] !== undefined
                    ? fuelLevels[index]
                    : 50;

            const row = document.createElement("tr");
            row.innerHTML = `
            <td>${satellite.id}</td>
            <td>${orbit}</td>
            <td>${satellite.altitude_km} km</td>
            <td>${satellite.velocity_kms} km/s</td>
            <td>
    <div style="display:flex; align-items:center; gap:8px;">
        <div class="fuel-cell">
            <div class="fuel-bar-table" style="width:${fuel}%"></div>
        </div>
        <strong style="color:white !important;">${fuel}%</strong>
    </div>
</td>
            <td>${satellite.threat_level || "SAFE"}</td>
            <td>
                <span style=" color: #22c55e; font-weight: bold;">
                    SAFE
                </span>
            </td>
`;

tableBody.appendChild(row);

        });

        console.log(
            "🛰 Real Satellite Fleet Loaded:",
            satellites
        );
        const lastUpdated = document.getElementById("satellite-last-updated");

if (lastUpdated) {
    lastUpdated.textContent = "Last Updated: " + updatedTime;
}

    } catch (error) {

        console.error(
            "Satellite Fleet API Error:",
            error
        );

    }

}

loadSatelliteFleet();
setInterval(loadSatelliteFleet, 10000);