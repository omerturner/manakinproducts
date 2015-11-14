

if (!(window.matchMedia('(max-width: 40em)').matches)) {
    $("#left-column").stick_in_parent();
    $("#right-column").stick_in_parent();
}


$('#mc-embedded-subscribe-form').submit(function(e) {
  console.debug('form submission')
  e.preventDefault();
  var $this = $(this);
  $.ajax({
      type: "GET", // GET & url for json slightly different
      url: "http://manakinproducts.us11.list-manage.com/subscribe/post-json?u=a1e0fa500772523128ea505f9&id=28d03a4f15&c=?",
      data: $this.serialize(),
      dataType    : 'json',
      contentType: "application/json; charset=utf-8",
      error       : function(err) { alert("Could not connect to the registration server."); },
      success     : function(data) {
          console.debug(data.msg)
          $('.submit-msg').remove()
          $signupDiv = $('#mc_embed_signup')
          if (data.result === "success") {
              msg =
              Ply.dialog("alert", { effect: ["fade", "scale"] } ,"Almost Finished..."
              + "To complete the subscription process, please click the link in the email we just sent you.");
          }
          else if (data.msg.indexOf("Please enter a value") > -1) {
              $signupDiv.append('<p class="submit-msg" style="font-size: 1.1em;color: red">Please Enter Your Email</p>');
          }
          else if (data.msg.indexOf("Too many subscribe") > -1) {
              Ply.dialog("alert", { effect: ["fade", "scale"] } ,"There are too many subscribe attempts from this email address,"
                                          + "Please try again in a few minutes");
          }
          else if (data.msg.indexOf("already subscribed") > -1) {
              Ply.dialog("alert", { effect: ["fade", "scale"] } ,"It Seems that your email is already in our mailing list");
          }
          else {
              Ply.dialog("alert", { effect: ["fade", "scale"] } ,"Oops, Something went wrong. Please Try again later");
          }
      }
  });
  return false;
});