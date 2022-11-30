// SPDX-License-Identifier: MIT
pragma solidity ^0.8.16;

contract CarGPS {

    using GPS for *;

    address endpoint;

    constructor() {
        endpoint = SIGNAL_TOWER_A;
    } 
}

import "./gps.sol";

