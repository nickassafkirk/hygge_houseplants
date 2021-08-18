from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """ Listen for webhooks from stripe """
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify it's signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except ValueError as e:
        # invalid Payload
        print('invalid payload')
        return HttpResponse(content=e, status=400)
    except stripe.error.SignatureVerificationError as e:
        # invalid signature
        print("invalid sig")
        return HttpResponse(content=e, status=400)
    except Exception as e:
        print("general")
        return HttpResponse(content=e, status=400)

    print('success')
    return HttpResponse(status=200)
