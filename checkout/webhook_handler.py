from django.http import HttpResponse
from .models import Order


class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Generic webhook handler
        """
        return HttpResponse(
            content=f'Unhandled Webhook received {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handles payment_intent.succeeded webhook from stripe
        """

        # Extracts data from payment intent to be stored in DB
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_details = intent.metadata.save_details
        accept_marketing = intent.metadata.accept_marketing

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        order_total = round(intent.data.charges[0].amount / 100, 2)

        # Store none for blank address field not empty string
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        try:
            order = Order.objects.get(
                full_name__iexact=shipping_details.name,
                email__iexact=shipping_details.email,
                phone_number__iexact=shipping_details.phone,
                country__iexact=shipping_details.country,
                postcode__iexact=shipping_details.postal_code,
                city_or_town__iexact=shipping_details.city,
                street_address1__iexact=shipping_details.line1,
                street_address2__iexact=shipping_details.line2,
                county_or_state__iexact=shipping_details.state,
                order_total__iexact=order_total,
            )
            order_exists = True
            return HttpResponse(
                content=f'Webhook received {event["type"]} | SUCCESS: Order already in Database',
                status=200)
        except Order.DoesNotExist:
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=shipping_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.country,
                    postcode=shipping_details.postal_code,
                    city_or_town=shipping_details.city,
                    street_address1=shipping_details.line1,
                    street_address2=shipping_details.line2,
                    county_or_state=shipping_details.state,
                    order_total=order_total,
                )

                for product_id, product_data in json.loads(cart).items():   
                    product = get_object_or_404(Product, pk=product_id)

                    # handle lineitem without variants
                    if isinstance(product_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            quantity=product_data,
                            product=product
                        )
                        order_line_item.save()

                # handle lineitem with variant
                else:
                    # iterate through product_data to extract variant_id & Qty
                    for variant_id, quantity in product_data["product_variants"].items():
                        variant = get_object_or_404(Variant, pk=variant_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            variant=variant,
                            quantity=quantity,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handles payment_intent.failed webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook received {event["type"]}',
            status=200)
