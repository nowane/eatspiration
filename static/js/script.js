$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });

// Check if confirm password matches password and set valid/invalid

  $("#password-confirm").keyup(function() {
    if ($( this ).val() === $( "#password" ).val()) {
      $( this ).removeClass("invalid").addClass("valid");
      this.setCustomValidity("");
    } else {
      $( this ).removeClass("valid").addClass("invalid");
      this.setCustomValidity("No match");
    }
  });