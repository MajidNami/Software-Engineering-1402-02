package com.softwareEngineering.chatServer;

import com.softwareEngineering.chatServer.config.GetStreamConfig;
import com.softwareEngineering.chatServer.service.GetStreamService;
import io.getstream.chat.java.exceptions.StreamException;
public class MainTest {

    public static void main(String[] args) throws StreamException {
        GetStreamConfig getStreamConfig = new GetStreamConfig("s6sm7pjf2j7c","qund8kraswa39wwhpgynzv6enufbwybqvr7arzt74amptmcbuy7eygk57bdzgfyj");
        GetStreamService getStreamService = new GetStreamService();
        getStreamService.createChannel("channel22");
        getStreamService.createUser("nini");
        getStreamService.addMember("nini", "channel22");
       String res = getStreamService.generateToken("nini");
        System.out.println(res);
    }

}
