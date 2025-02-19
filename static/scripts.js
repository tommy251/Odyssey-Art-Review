// Function to handle menu button clicks
function handleMenuClick(event) {
    event.preventDefault(); // Prevent default behavior (e.g., page reload)
    alert("Menu button clicked!");
    // Add logic to show/hide menu options
}

// Function to handle Imagery Art button clicks
function handleImageryArtClick(event) {
    event.preventDefault(); // Prevent default behavior
    alert("Imagery Art button clicked!");
    // Add logic to filter or display imagery art
}

// Function to handle Visual Art button clicks
function handleVisualArtClick(event) {
    event.preventDefault(); // Prevent default behavior
    alert("Visual Art button clicked!");
    // Add logic to filter or display visual art
}

// Function to handle Admire button clicks
function handleAdmireClick(artworkName) {
    fetch('/admire', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ artwork_name: artworkName }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred. Please try again.");
    });
}

// Function to handle Dislike button clicks
function handleDislikeClick(artworkName) {
    fetch('/dislike', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ artwork_name: artworkName }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred. Please try again.");
    });
}

// Attach event listeners to buttons
document.addEventListener("DOMContentLoaded", function () {
    // Menu button
    const menuButton = document.querySelector("nav ul li a[href='#']");
    if (menuButton) {
        menuButton.addEventListener("click", handleMenuClick);
    }

    // Imagery Art button
    const imageryArtButton = document.querySelector("nav ul li a[href='#imagery']");
    if (imageryArtButton) {
        imageryArtButton.addEventListener("click", handleImageryArtClick);
    }

    // Visual Art button
    const visualArtButton = document.querySelector("nav ul li a[href='#visual']");
    if (visualArtButton) {
        visualArtButton.addEventListener("click", handleVisualArtClick);
    }

    // Admire and Dislike buttons
    document.querySelectorAll(".admire-btn").forEach(button => {
        button.addEventListener("click", (event) => {
            event.preventDefault(); // Prevent default behavior
            const artworkName = button.closest(".art-item").querySelector("h3").innerText;
            handleAdmireClick(artworkName);
        });
    });

    document.querySelectorAll(".dislike-btn").forEach(button => {
        button.addEventListener("click", (event) => {
            event.preventDefault(); // Prevent default behavior
            const artworkName = button.closest(".art-item").querySelector("h3").innerText;
            handleDislikeClick(artworkName);
        });
    });
});