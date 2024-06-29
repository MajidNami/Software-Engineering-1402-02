package com.softwareEngineering.chatServer.Exception;

public class PartnerNotFoundException extends RuntimeException {

    public PartnerNotFoundException(String message) {
        super(message);
    }
}
