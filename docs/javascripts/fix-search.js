// Fix: prevent search overlay from opening on page refresh (CMD+R).
// Browsers may restore the search toggle checkbox state after refresh.
document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.querySelector("[data-md-toggle=search]");
  if (toggle) toggle.checked = false;
});
