/* 
Core logic/payment flow comes from this article:
https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements
css from:
https://stripe.com/docs/js
*/

let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1); /* Get the public key from the template using .text method*/
let clientSecret = $('#id_client_secret').text().slice(1, -1); /* The slice method removes the first and last apostrophe chars */
let stripe = Stripe(stripePublicKey); /* Set up stripe using our public key, Stripe function comes from the stripe.js script in our base template */
let elements = stripe.elements(); /* create an instance of stripe.elements so we can make a card details form */

let style = {
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

let card = elements.create('card', {style: style}); 
card.mount('#card-element'); /* mount the new card element to the appropriate part of our template */

// Handle realtime validation errors on the card element
card.addEventListener('change', function(event){
  let errorDiv = document.getElementById('card-errors');
  if (event.error) {
    let html = `
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

// Target checkout form
let form = document.getElementById('checkout-form');

// Submit form by clicking hidden button in form.
$('#btn-checkout').click(function(){
   $('#hidden-submit').click();
})

// Handle form submit
form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({ 'disabled': true});
  $('#btn-checkout').attr('disabled', true);
  $('#checkout-form').fadeToggle(100);
  $('#loading-overlay').fadeToggle(100);
  
  // Send the form metadata to the view to be added to the payment intent
  let saveDetails = Boolean($('#save-details').attr('checked'));
  let acceptMarketing = Boolean($('#accept-marketing').attr('checked'));
  let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

  let postData = {
    'csrfmiddlewaretoken': csrfToken,
    'client_secret': clientSecret,
    'save_details': saveDetails,
    'accept_marketing': acceptMarketing,
  }

  let url = '/checkout/cache_checkout_data/';
  $.post(url, postData).done( function(){
    stripe.confirmCardPayment(clientSecret, {
      payment_method: {
          card: card,
          billing_details: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            email: $.trim(form.email.value),
            address: {
              line1: $.trim(form.street_address1.value),
              line2: $.trim(form.street_address2.value),
              city: $.trim(form.city_or_town.value),
              country: $.trim(form.country.value),
              state: $.trim(form.county_or_state.value),
            }
          }
      },
      shipping: {
        name: $.trim(form.full_name.value),
        phone: $.trim(form.phone_number.value),
        address: {
          line1: $.trim(form.street_address1.value),
          line2: $.trim(form.street_address2.value),
          city: $.trim(form.city_or_town.value),
          postal_code: $.trim(form.postcode.value),
          country: $.trim(form.country.value),
          state: $.trim(form.county_or_state.value),
        }
      }
    }).then(function(result) {
        if (result.error) {
            let errorDiv = document.getElementById('card-errors');
            let html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#checkout-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            card.update({ 'disabled': false});
            $('#btn-checkout').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
              form.submit();
            }
        }
    });
  }).fail(function(){
    location.reload();
  })
});