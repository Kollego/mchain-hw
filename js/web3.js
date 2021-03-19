const Web3 = require('web3')
var web3 = new Web3(new Web3.providers.HttpProvider("https://goerli.infura.io/v3/2766c630280c4028a8f90a253d71098f"));
const address = "0x0e1FBb8916D67002336F8B28E357f954Ce2C31cc";
const my_addr = '0x29Fa39bCC564541D2116871dc140a8FEBd3678DF';
const contractJson = fs.readFileSync('abi.json');
const ABI = JSON.parse(contractJson);
web3.eth.getBalance // проверяем
const myContract = new web3.eth.Contract(ABI, address);
myContract.methods.balance(my_addr).call().then(console.log);
myContract.methods.owner().call().then(console.log);

/*
let transaction = myContract.methods.produce(100);

let options = {
    to  : transaction._parent._address,
    data: transaction.encodeABI(),
    gas : transaction.estimateGas({from: my_addr}),
};
let pk = '';
let signedTransaction = web3.eth.accounts.signTransaction(options, pk);
let transactionReceipt = web3.eth.sendSignedTransaction(signedTransaction.rawTransaction);


transaction.estimateGas({from: my_addr}).then(function(gasAmount){console.log(gasAmount)});
*/