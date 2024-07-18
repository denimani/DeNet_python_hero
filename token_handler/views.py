import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web3 import Web3

YOUR_TOKEN_ADDRESS = Web3.to_checksum_address('0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0')


def get_balance(request):
    if 'address' in request.GET:
        address = request.GET['address']

        web3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))
        with open('./erc20_abi.json') as f:
            erc20_abi = json.load(f)
        contract = web3.eth.contract(address=YOUR_TOKEN_ADDRESS, abi=erc20_abi)

        balance = contract.functions.balanceOf(address).call()

        formatted_balance = balance / 10 ** 18

        return JsonResponse({'balance': str(formatted_balance)})

    else:
        return JsonResponse({'error': 'Отсутствует параметр адреса'})


@csrf_exempt
def get_balance_batch(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        addresses = data.get('addresses', [])

        web3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))
        with open('./erc20_abi.json') as f:
            erc20_abi = json.load(f)
        contract = web3.eth.contract(address=YOUR_TOKEN_ADDRESS, abi=erc20_abi)

        balances = []
        for address in addresses:
            balance = contract.functions.balanceOf(address).call()
            formatted_balance = balance / 10 ** 18
            balances.append(formatted_balance)
        return JsonResponse({'balances': balances})
    else:
        return JsonResponse({'error': 'Требуется метод POST'})


def get_top_addresses(request, n):
    pass


def get_top_addresses_with_transactions(request, n):
    pass


def get_token_info(request, token_address):
    web3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))
    with open('../erc20_abi.json') as f:
        erc20_abi = json.load(f)
    contract = web3.eth.contract(address=token_address, abi=erc20_abi)

    symbol = contract.functions.symbol().call()
    name = contract.functions.name().call()
    total_supply = contract.functions.totalSupply().call()
    return JsonResponse({
        'symbol': symbol,
        'name': name,
        'total_supply': total_supply
    })
