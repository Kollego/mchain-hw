## Домашняя работа Masterchain
### Выполнил: Колесников Егор БПИ171
### Описание
В данной работе представлен смарт-контракт `hw-contract.sol` Цифровой валюты центрального банка Ямайки (*YamaicaCoin*).
Смарт-контракт [размещен в тестнете goerli](https://goerli.etherscan.io/address/0x07b9722b82c54784366e9F785FF99baBEeE2Aeb3).

### Функции смарт-контракта
#### produce
Создает на главном кошельке новые токены.
``` js
function produce(uint amount) public
```
#### transfer
Пересылает токены с текущего адреса на другой.
``` js
function transfer(uint amount, address to) public
```

### Код взаимодействия
Код взаимодействия со смарт-контраком находится в `python/my-web3.py`. В нём представлен пример создания новых токенов через Web3 на Python.
