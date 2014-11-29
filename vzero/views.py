"""
" views.py
" --------
"
" Methods defined for creating the views of the demo
"""

"""
" To use Braintree it is mandatory to configure the API credentials, that could
" be gotten from Braintree account. In this example, we'll use Sandbox API
" credentials from the Commerce Factory Braintree account. More information at:
"    * github.com/commercefactory
"    * commercefactory.org
"""
import braintree

braintree.Configuration.configure(
                braintree.Environment.Sandbox,
                merchant_id="ffdqc9fyffn7yn2j",
                public_key="qj65nndbnn6qyjkp",
                private_key="a3de3bb7dddf68ed3c33f4eb6d9579ca"
                )

"""
" Using django shorcuts for render the html templates
"""

from django.shortcuts import render_to_response

"""
" Method called in the root of website. Getting the client_token, which contains
" all authorization and configuration information your client needs to
" initialize a Braintree Client SDK to communicate with Braintree.
"""

def index(request):
    client_token=braintree.ClientToken.generate({})

    return render_to_response("index.html",locals())

"""
" Responsible for receiving the payment method nonce and using it appropriately.
" In this case, finish the transaction
"""

def checkout(request):
    nonce=request.POST.get("payment_method_nonce")

    result=braintree.Transaction.sale({
        "amount":"10.00",
        "payment_method_nonce":nonce
    })

    transaction_id=result.transaction.id

    return render_to_response("checkout.html",locals())
