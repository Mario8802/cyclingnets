document.addEventListener("DOMContentLoaded", function () {
    const backToTopButton = document.getElementById("back-to-top");

    window.addEventListener("scroll", () => {
        if (window.scrollY > 200) {
            backToTopButton.style.display = "block";
        } else {
            backToTopButton.style.display = "none";
        }
    });

    // Плавно скролиране до началото
    backToTopButton.addEventListener("click", (event) => {
        event.preventDefault(); // Спира анкора да промени URL
        window.scrollTo({
            top: 0,
            behavior: "smooth",
        });
    });
});
