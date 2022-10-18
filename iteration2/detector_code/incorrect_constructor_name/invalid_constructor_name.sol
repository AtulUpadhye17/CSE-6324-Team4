// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Missing{
    address private owner;

    modifier onlyowner {
        require(msg.sender==owner);
        _;
    }
    
    function missing() public{
        owner = msg.sender;
    }
}