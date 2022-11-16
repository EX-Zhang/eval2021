
import blockcypher

def create_Address(api_key):

    return blockcypher.generate_new_address(api_key=api_key)

def create_Wallet(wallet_name, address, api_key):

    return blockcypher.create_wallet_from_address(wallet_name, address, api_key)

def delete_Wallet(wallet_name, api_key):

    return blockcypher.delete_wallet(wallet_name,api_key)


def Wallet_Remove_Address(wallet_name, address, api_key):

    return blockcypher.remove_address_from_wallet(wallet_name, address, api_key)

def Wallet_Add_Address(wallet_name, address, api_key):

    return blockcypher.add_address_to_wallet(wallet_name, address, api_key)

def Wallet_Balance(wallet_name, api_key):

    return blockcypher.get_wallet_balance(wallet_name, api_key)

def start_Transaction(input_addrs, output_addr, value, api_key):

    inputs = []

    for input_addr in input_addrs:

        inputs.append({"address": input_addr})

    outputs = [{"address": output_addr, "value": value}]

    return blockcypher.create_unsigned_tx(inputs,outputs,api_key=api_key)
