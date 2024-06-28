package com.softwareEngineering.chatServer;

import com.softwareEngineering.chatServer.service.GetStreamService;
import io.getstream.chat.java.exceptions.StreamException;

public class MainTest {


    public static void main(String[] args) throws StreamException {
        GetStreamService getStreamService = new GetStreamService();
//        getStreamService.createChannel("channel1");
        getStreamService.createUser("almas");
//        getStreamService.addMember("almas", "channel1");
//       String res = getStreamService.generateToken("almas");
//        System.out.println(res);
    }

}
