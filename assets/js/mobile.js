
var $menuButton = $("#menu-button-mobile");
var $nav = $("#top-nav");

$(document).ready(function() {
  $menuButton.on("click", function(event) {
    event.preventDefault();
    $nav.slideToggle(500);
  });
});