
from .models import *

from .BlockCypher import *

def add_Address(username, address, wallet):

    addr = address['address']

    private = address['private']

    public = address['public']

    wif = address['wif']

    new_addr = Address(username=username, wallet=wallet, address=addr, private=private, public=public, wif=wif)

    new_addr.save()

def add_Wallet(username, wallet):

    if len(Wallet.objects.filter(username=username,wallet=wallet)) != 0:

        return {"error":"wallet exist"}

    new_wallet = Wallet(username=username,wallet=wallet)

    new_wallet.save()

def del_Wallet(username, wallet, api_key):

    delete_Wallet(wallet,api_key)

    Wallet.objects.get(username=username,wallet=wallet).delete()

    Address.objects.filter(username=username, wallet=wallet).delete()

def get_Addresses(username, wallet):

    results = []

    addresses = Address.objects.filter(username=username, wallet=wallet)

    for address in addresses:

        results.append(address.address)

    return results

def getWallets(username, api_key):

    results = []

    wallets = Wallet.objects.filter(username=username)

    for wallet in wallets:

        name = wallet.wallet

        balance = Wallet_Balance(name,api_key)

        result = {

            "Wallet" : name,

            "Addresses": get_Addresses(username, name),

            "Sent": balance["total_sent"],

            "Received": balance["total_received"],

            "Balance": balance["balance"],

        }

        results.append(result)

    return results

def getAddress(address):

    return Address.objects.get(address=address)
