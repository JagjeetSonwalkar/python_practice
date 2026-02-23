document.addEventListener("DOMContentLoaded", function () {

    console.log("JS Loaded ✅");

    let btn = document.getElementById("myBtn");
    let result = document.getElementById("result");

    if (btn) {
        btn.addEventListener("click", function () {
            result.innerText = "Button Clicked Successfully 🚀";
        });
    }

});
