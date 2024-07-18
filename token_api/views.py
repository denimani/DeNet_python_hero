import json
from django.http import JsonResponse
from web3 import Web3


def get_balance(request):
    if 'address' in request.GET:
        address = request.GET['address']
        token_address = '0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0'
        token_address = Web3.to_checksum_address(token_address)
        web3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))

        with open('./erc20_abi.json') as f:
            erc20_abi = json.load(f)

        contract = web3.eth.contract(address=token_address, abi=erc20_abi)

        balance = contract.functions.balanceOf(address).call()

        formatted_balance = balance / 10**18

        return JsonResponse({'balance': formatted_balance})

    else:
        return JsonResponse({'error': 'Missing address parameter'})
