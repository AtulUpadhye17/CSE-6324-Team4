// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;
contract HelloBlockchain
{
    enum StateType { Request, Respond}
    StateType public  State;
    address public  Requestor;
    address public  Responder;
    string public RequestMessage;
    string public ResponseMessage;
    function SendRequest(string memory requestMessage) public
    {
        if (Requestor != msg.sender)
        {
            revert();
        }
        RequestMessage = requestMessage;
        State = StateType.Request;
    }
    function SendResponse(string memory responseMessage) public
    {
        Responder = msg.sender;
        ResponseMessage = responseMessage;
        State = StateType.Respond;
    }
    constructor(string memory message) public
    {
        Requestor = msg.sender;
        RequestMessage = message;
        State = StateType.Request;
    }
}