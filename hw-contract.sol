pragma solidity ^0.7.3;

contract Token {

  address public owner;
  string public name;

  constructor() {
    owner = msg.sender;
    name = "JamaicaCoin";
  }


  mapping(address => uint) public balance;
  
  
  function produce(uint amount) public {
    require (msg.sender == owner);
    balance[owner] += amount;
  }

  function transfer(uint amount, address to) public {
    require (balance[msg.sender] >= amount);
    balance[msg.sender] -= amount;
    balance[to] += amount;
  }

}