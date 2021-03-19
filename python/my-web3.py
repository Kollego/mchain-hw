from web3 import Web3
from eth_account import Account
import json
from web3.middleware import geth_poa_middleware

# Запускать через командную строку!

# Подключаемся к сети
w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/2766c630280c4028a8f90a253d71098f'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Проверка подключения
if w3.isConnected():
    print('Successful connection.')
else:
    print('Connection failed')
    exit(0)

# Подключаение к смарт-контракту
contract_address = '0x07b9722b82c54784366e9F785FF99baBEeE2Aeb3'
with open('abi.json', 'r') as f:
    ABI = json.loads(f.read())
my_contract = w3.eth.contract(contract_address, abi=ABI)

# Получение аккаунта (private key хранится локально)
with open('pk.txt', 'r') as f:
    private_key = f.read()
acct = Account.privateKeyToAccount(private_key)
# public key 0x29Fa39bCC564541D2116871dc140a8FEBd3678DF

print('NAME OF TOKEN: ', my_contract.functions.name().call())

# Изначальный баланс
print('INITIAL BALANCE: ', my_contract.functions.balance(acct.address).call())

# Выпускаем деньги
nonce = w3.eth.getTransactionCount(acct.address)
txn = my_contract.functions.produce(100).buildTransaction({
    'chainId': 5,
    'gas': 70000,
    'nonce': nonce
})
signed_txn = w3.eth.account.sign_transaction(txn, private_key)
# hash можно проверить на https://goerli.etherscan.io/
hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Конечный баланс должен быть на 100 больше
print('RESULT BALANCE: ', my_contract.functions.balance(acct.address).call())

