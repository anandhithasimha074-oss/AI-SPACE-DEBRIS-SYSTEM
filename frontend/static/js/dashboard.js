document.addEventListener("DOMContentLoaded", function () {

    console.log("AI Space Debris Tracking System Running");


    // Debris Activity Graph

    const debrisChart = document.getElementById("debrisChart");

    if (debrisChart) {

        new Chart(debrisChart, {

            type: "line",

            data: {

                labels: [
                    "00:00",
                    "04:00",
                    "08:00",
                    "12:00",
                    "16:00",
                    "20:00"
                ],

                datasets: [
                    {
                        label: "Tracked Debris Objects",

                        data: [
                            820,
                            950,
                            1100,
                            1180,
                            1250,
                            1320
                        ]

                    }
                ]

            }

        });

    }





    // Collision Risk Graph


    const riskChart = document.getElementById("riskChart");


    if (riskChart) {


        new Chart(riskChart, {


            type:"line",


            data:{


                labels:[
                    "Day 1",
                    "Day 2",
                    "Day 3",
                    "Day 4",
                    "Day 5",
                    "Day 6"
                ],


                datasets:[

                    {

                    label:"Collision Risk %",

                    data:[
                        4,
                        6,
                        5,
                        8,
                        3,
                        2
                    ]

                    }

                ]


            }


        });


    }







    // Live AI Simulation


    function updateSystemData(){


        const riskValues = [
            "LOW",
            "MEDIUM",
            "HIGH"
        ];


        const risk =
        riskValues[Math.floor(Math.random()*3)];



        console.log(
            "AI Risk Level:",
            risk
        );



        console.log(

            "Tracked Objects:",
            Math.floor(
                Math.random()*5000 + 30000
            )

        );



        console.log(

            "Collision Probability:",
            Math.floor(
                Math.random()*10
            )
            +"%"

        );


    }



    setInterval(
        updateSystemData,
        5000
    );


});