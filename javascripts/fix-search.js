// Fix: prevent search overlay from opening on page refresh (CMD+R).
// Browsers may restore the search toggle checkbox state AFTER DOMContentLoaded,
// so we use pageshow + setTimeout to ensure we run after form restoration.
window.addEventListener("pageshow", function () {
  setTimeout(function () {
    var toggle = document.querySelector("[data-md-toggle=search]");
    if (toggle) toggle.checked = false;
  }, 0);
});
