let fromCity = document.getElementById("fromCity");
let toCity = document.getElementById("toCity");
let button = document.getElementById("findRoute");

button.addEventListener("click", async function() {

    let source = fromCity.value;
    let destination = toCity.value;

    let response = await fetch(
        `http://127.0.0.1:8000/shortest-route?source=${source}&destination=${destination}`
    );

    let data = await response.json();
     document.getElementById("routeResult").textContent =
    data.route.join(" → ");

    document.getElementById("distanceResult").textContent =
    data.distance + " km";
    let speed = 50;
    let time = data.distance / speed;
    let hours = Math.floor(time);

    let minutes = Math.round((time - hours) * 60);

    document.getElementById("timeResult").textContent =
    hours + " hr " + minutes + " min";
});