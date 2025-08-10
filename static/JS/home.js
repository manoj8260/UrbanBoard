document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.getElementById("theme-checkbox");
    themeToggle.addEventListener("change", () => {
        document.body.classList.toggle("dark", themeToggle.checked);
    });

    const priceSlider = document.getElementById("filterPrice");
    const priceValue = document.getElementById("priceValue");
    priceSlider.addEventListener("input", () => {
        priceValue.textContent = `₹${parseInt(priceSlider.value).toLocaleString()}`;
    });
});
