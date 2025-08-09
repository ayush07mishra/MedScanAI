let map;
let markers = [];

function initMap() {
    map = L.map('map').setView([26.473846856636705, 80.30517856698373], 12);  // Default location (New York)

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
}

function getNearbyPlaces() {
    const lat = parseFloat(document.getElementById('lat').value);
    const lng = parseFloat(document.getElementById('lng').value);
    const placeType = document.getElementById('type').value;

    if (isNaN(lat) || isNaN(lng)) {
        alert("Please enter valid latitude and longitude.");
        return;
    }

    // Clear previous markers
    markers.forEach(marker => marker.remove());
    markers = [];

    // Make API call to Flask server to get nearby places
    fetch(`/nearby?lat=${lat}&lng=${lng}&type=${placeType}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                displayPlacesOnMap(data);
            }
        })
        .catch(error => console.error('Error:', error));
}

function displayPlacesOnMap(places) {
    places.forEach(place => {
        const marker = L.marker([place.latitude, place.longitude]).addTo(map);

        const popupContent = `
            <h3>${place.name}</h3>
            <p>Address: ${place.address}</p>
            <p>Distance: ${place.distance} km</p>
        `;
        marker.bindPopup(popupContent);

        markers.push(marker);
    });
}

window.onload = initMap;
