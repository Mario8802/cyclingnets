document.addEventListener("DOMContentLoaded", function () {
    // Attach event listeners to all buttons with the class "join-leave-btn"
    document.querySelectorAll(".join-leave-btn").forEach(function (button) {
        button.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent the default form submission behavior

            const form = this.closest("form"); // Find the closest form element to the button
            const formData = new FormData(form); // Create a FormData object from the form
            const csrfToken = form.querySelector('input[name="csrfmiddlewaretoken"]').value; // Get the CSRF token from the form

            // Send an AJAX POST request to the form's action URL
            fetch(form.action, {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": csrfToken, // Include the CSRF token in the headers
                    "X-Requested-With": "XMLHttpRequest", // Indicate that this is an AJAX request
                },
            })
                .then((response) => response.json()) // Parse the response as JSON
                .then((data) => {
                    // Handle the response based on the status
                    if (data.status === "joined") {
                        this.textContent = "Leave"; // Update the button text
                        this.classList.remove("btn-primary"); // Remove the primary button style
                        this.classList.add("btn-secondary"); // Add the secondary button style
                    } else if (data.status === "left") {
                        this.textContent = "Join"; // Update the button text
                        this.classList.remove("btn-secondary"); // Remove the secondary button style
                        this.classList.add("btn-primary"); // Add the primary button style
                    } else if (data.error) {
                        alert(data.error); // Show an error message to the user
                    }
                })
                .catch((error) => {
                    console.error("Error:", error); // Log any errors to the console
                    alert("Something went wrong. Please try again."); // Show a generic error message to the user
                });
        });
    });
});
