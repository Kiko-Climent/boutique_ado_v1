from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intend_succeeded(self, event):
        """
        Handle the payment_intend.succeeded from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intend_payment_failed(self, event):
        """
        Handle the payment_intend.payment_failed from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)