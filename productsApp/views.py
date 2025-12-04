from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

# Create your views here.
def home(request):
    context ={}
    return render(request,'productsApp/home.html' , context)


def index(request):
    # cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    # phone_number = '0719873406'
    # amount = 1
    # account_reference = 'reference'
    # transaction_desc = 'Description'
    # callback_url = 'https://api.darajambili.com/express-payment'
    # response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def mpesaPayment(request):
    cl = MpesaClient()
    accountReference = 'SMS'
    transactionDesc = 'Purchase of camel milk.'
    callbackUrl = 'https://api.darajambili.com/express-payment'

    # get user phonenumber
    # get amount to pay
    if request.method == 'POST':
        phoneNumber = request.POST.get('phoneNumber')
        amount = int(float(request.POST.get('amount')))
        response = cl.stk_push(phoneNumber, amount, accountReference, transactionDesc, callbackUrl)
        context ={"response":response}
        return render(request, 'productsApp/mpesa_payments.html', context)
    else:
        return render(request, 'productsApp/mpesa_payments.html')
