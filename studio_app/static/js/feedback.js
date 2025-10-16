document.addEventListener("DOMContentLoaded", function() {
    const stars = document.querySelectorAll(".star-rating .star");
    const ratingInput = document.getElementById("id_rating");

    stars.forEach((star, idx) => {
        star.addEventListener("click", function() {
            ratingInput.value = idx + 1;

            stars.forEach((s, i) => {
                if (i <= idx) {
                    s.classList.add("selected");
                } else {
                    s.classList.remove("selected");
                }
            });
        });

        star.addEventListener("mouseover", function() {
            stars.forEach((s, i) => {
                s.style.color = i <= idx ? "#ff4081" : "#ccc";
            });
        });

        star.addEventListener("mouseout", function() {
            stars.forEach((s, i) => {
                s.style.color = s.classList.contains("selected") ? "#ff4081" : "#ccc";
            });
        });
    });
});
