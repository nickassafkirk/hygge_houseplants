/* 
Core logic/payment flow comes from this article:
https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements
css from:
https://stripe.com/docs/js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1); /* Get the public key from the template using .text method*/
var clientSecret = $('#id_client_secret').text().slice(1, -1); /* The slice method removes the first and last apostrophe chars */
var stripe = Stripe(stripePublicKey); /* Set up stripe using our public key, Stripe function comes from the stripe.js script in our base template */
var elements = stripe.elements(); /* create an instance of stripe.elements so we can make a card details form */

var style = {
      base: {
        color: '#000',
        fontFamily: 'Source Sans Pro, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        '::placeholder': {
          color: '#898e94'
        }
      },
      invalid: {
        iconColor: '#dc3545',
        color: '#dc3545',
      }
};

var card = elements.create('card', {style: style}); 
card.mount('#card-element'); /* mount the new card element to the appropriate part of our template */

// Handle realtime validation errors on the card element
card.addEventListener('change', function(event){
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
    var html = `
    <span class="icon" role="alert">
        <i class="fas fa-times"></i>
    </span>
    <span>${event.error.message}</span>
    `
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent='';
  }
}); 

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({ 'disabled': true});
  $('#submit-button').attr('disabled', true);
  $('#payment-form').fadeToggle(100);
  $('#loading-overlay').fadeToggle(100);


  var saveInfo = Boolean($('#id-save-info').attr('checked'));
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var postData = {
    'csrfmiddlewaretoken': csrfToken,
    'client_secret': clientSecret,
    'save_info': saveInfo,
  };
  var url = '/checkout/cache_checkout_data/';
  
  // posts to the postData object above to the cahe_checkout_data view
  // using .done, we execute the callback when we've received 200 response from view
  $.post(url, postData).done(function(){
    stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: $.trim(form.full_name.value),
          phone: $.trim(form.phone_number.value),
          email: $.trim(form.email.value),
          address:{
            line1: $.trim(form.street_address1.value),
            line2: $.trim(form.street_address2.value),
            city: $.trim(form.town_or_city.value),
            country: $.trim(form.country.value),
            state: $.trim(form.county.value),
          }
        }
      },
      shipping: {
        name: $.trim(form.full_name.value),
        phone: $.trim(form.phone_number.value),
        address:{
          line1: $.trim(form.street_address1.value),
          line2: $.trim(form.street_address2.value),
          city: $.trim(form.town_or_city.value),
          country: $.trim(form.country.value),
          postal_code: $.trim(form.postcode.value),
          state: $.trim(form.county.value),
        }
      }
    }).then(function(result) {
      if (result.error) {
        var errorDiv = document.getElementById('card-errors');
        var html = `
                    <span class="icon" role="alert">
                      <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
        $(errorDiv).html(html);
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);
        card.update({ 'disabled': false});
        $('#submit-button').attr('disabled', false);
      } else {
        // The payment has been processed
        if (result.paymentIntent.status === 'succeeded') {
          form.submit();
        }
      }
    }) 
  }).fail(function(){
    // if post fails, reload the page so django error message is displayed.
    location.reload();
  })
});