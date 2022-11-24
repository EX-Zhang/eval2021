
from .models import *

import blockcypher

def create_Address(api_key):

    return blockcypher.generate_new_address(api_key=api_key,coin_symbol='btc-testnet')

def create_Wallet(wallet_name, address, api_key):

    return blockcypher.create_wallet_from_address(wallet_name, address, api_key,coin_symbol='btc-testnet')

def delete_Wallet(wallet_name, api_key):

    return blockcypher.delete_wallet(wallet_name,api_key,coin_symbol='btc-testnet')


def Wallet_Remove_Address(wallet_name, address, api_key):

    return blockcypher.remove_address_from_wallet(wallet_name, address, api_key,coin_symbol='btc-testnet')

def Wallet_Add_Address(wallet_name, address, api_key):

    return blockcypher.add_address_to_wallet(wallet_name, address, api_key,coin_symbol='btc-testnet')

def Wallet_Balance(wallet_name, api_key):

    return blockcypher.get_wallet_balance(wallet_name, api_key,coin_symbol='btc-testnet')

def start_Transaction(input_addrs, output_addr, value, api_key):

    inputs = []

    private_list = []

    public_list = []

    for input_addr in input_addrs:

        inputs.append({"address": input_addr})

        addr = Address.objects.get(address=input_addr)

        private_list.append(addr.private)

        public_list.append(addr.public)

    outputs = [{"address": output_addr, "value": int(value)}]

    unsigned_tx = blockcypher.create_unsigned_tx(inputs,outputs,api_key=api_key,include_tosigntx=True,coin_symbol='btc-testnet')

    signature = blockcypher.make_tx_signatures(unsigned_tx["tosign"],private_list,public_list)

    return blockcypher.broadcast_signed_transaction(unsigned_tx,signature,public_list,api_key=api_key,coin_symbol='btc-testnet')
