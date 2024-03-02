Title: Contact Us
Status: Hidden
Menu: TopE

{!notice.md!}

## Mailing Address
West Lane Translator Incorporated  
P.O. Box 91  
Florence, Oregon 97439

## Email Us

Use this form to send us a message about reception problems,
becoming a member of WLT, tower space rental, or whatever else is on
your mind.

Someone from our organization will contact you in reply shortly.

<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/emailjs-com@2.3.2/dist/email.min.js"></script>
<script type="text/javascript">
    (function(){
        emailjs.init("user_qynd2RaOSxVwUeWdviCzy");
    })();
</script>

<script type="text/javascript">
    window.onload = function() {
	document.getElementById('contact-form').addEventListener('submit', function(event) {
	    event.preventDefault();
	    emailjs.sendForm('default_service', 'contact_form', this)
	    .then(function(response) {
		alert('Your e-mail has been sent.');
		window.location.reload(false);
	    }, function(error) {
		alert('Your e-mail could not be sent: ' + error);
	    });
	});
    }
</script>

<form id="contact-form">
  <p><label><b>Your name:</b><br>
      <input type="text" name="user_name"
             placeholder="John Doe" size="50" required>
  </label></p>
  <p><label><b>Your e-mail address:</b><br>
      <input type="email" name="user_email"
             placeholder="john.doe@big_company.com" size="50" required>
  </label></p>
  <p><label><b>Subject:</b><br>
      <input type="text" name="subject" size="50" required>
  </label></p>
  <p><label><b>Category:</b><br>
      <select name="category">
        <option value="WLT Administration">WLT Administration</option>
        <option value="Website Problems">Website Problems</option>
        <option value="Reception Issues - KEPB (OPB) channel 28">
          Reception Issues - KEPB (OPB) channel 28</option>
        <option value="Reception Issues - KEZI (ABC) channel 9">
          Reception Issues - KEZI (ABC) channel 9</option>
        <option value="Reception Issues - KLSR (FOX) channel 34">
          Reception Issues - KLSR (FOX) channel 34</option>
        <option value="Reception Issues - KMTR (NBC) channel 16">
          Reception Issues - KMTR (NBC) channel 16</option>
        <option value="Reception Issues - KVAL (CBS) channel 13">
          Reception Issues - KVAL (CBS) channel 13</option>
        <option value="Support WLT - Membership">
          Support WLT - Membership</option>
        <option value="Problems with the Library's Signal Meter">
          Problems with the Library's Signal Meter</option>
        <option value="Tower Leasing">Tower Leasing</option>
      </select>
  </label></p>
  <p><label><b>Message:</b><br>
      <textarea name="message" cols="80" rows="6" required></textarea>
  </label></p>

  <p><label>
      <!-- Client-side validation is a bit silly, but it's something. -->
      The following question is for testing whether you are a human
      visitor and to prevent automated spam submissions.<br>
      <b>What river runs through Florence, Oregon?:</b><br>
      <input type="text" name="river" size="10" required
             pattern="[Ss][Ii][Uu][Ss][Ll][Aa][Ww]"><br>
      <i>Hint: One word only, seven letters total.</i>
  </label></p>

  <input type="submit" value="Send e-mail">
</form>
