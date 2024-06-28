package com.softwareEngineering.chatServer.service;

import io.getstream.chat.java.exceptions.StreamException;
import io.getstream.chat.java.models.Channel;
import io.getstream.chat.java.models.User;
import org.springframework.stereotype.Component;

@Component
public class GetStreamService {

    private String secretKey;

    public String generateToken(String userId) {
        return User.createToken(userId, null, null);
    }

    public void createChannel(String channelId) throws StreamException {

        var gandalf =
                User.UserRequestObject.builder()
                        .id("aut")
                        .build();
        Channel.getOrCreate("messaging", channelId)
                .data(Channel.ChannelRequestObject.builder().createdBy(gandalf).build())
                .request();
    }

    public void addMember(String userId, String channelId) throws StreamException {
        Channel.update("messaging", channelId).addMember(userId).request();
    }

    public void createUser(String userId) throws StreamException {
        var user = User.UserRequestObject.builder().id(userId).role("user").build();
        User.upsert().user(user).request();
    }

}
