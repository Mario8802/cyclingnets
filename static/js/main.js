// Wait for the DOM to be fully loaded before running the script
document.addEventListener("DOMContentLoaded", function () {
    // Get the "Back to Top" button element by its ID
    const backToTopButton = document.getElementById("back-to-top");

    /**
     * Show or hide the "Back to Top" button based on the scroll position.
     * - If the user scrolls down more than 200 pixels from the top, show the button.
     * - If the user scrolls back above 200 pixels, hide the button.
     */
    window.addEventListener("scroll", () => {
        if (window.scrollY > 200) {
            backToTopButton.style.display = "block"; // Show the button
        } else {
            backToTopButton.style.display = "none"; // Hide the button
        }
    });

    /**
     * Smoothly scroll to the top of the page when the "Back to Top" button is clicked.
     * - Prevent the default behavior of the button.
     * - Use the `window.scrollTo` method with smooth behavior for a better user experience.
     */
    backToTopButton.addEventListener("click", (event) => {
        event.preventDefault(); // Prevent the default link behavior (if any)
        window.scrollTo({
            top: 0, // Scroll to the very top of the page
            behavior: "smooth", // Enable smooth scrolling animation
        });
    });

    /**
     * Add smooth scrolling behavior to all internal anchor links on the page.
     * - Select all links that have an `href` starting with `#`.
     * - When clicked, prevent the default jump to the section and scroll smoothly instead.
     */
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener("click", (event) => {
            event.preventDefault(); // Prevent the default link jump behavior
            const targetId = anchor.getAttribute("href").slice(1); // Extract the ID from the href (e.g., "#section" -> "section")
            const targetElement = document.getElementById(targetId); // Find the target element by its ID

            // Scroll smoothly to the target element if it exists
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: "smooth", // Enable smooth scrolling animation
                });
            }
        });
    });
});
