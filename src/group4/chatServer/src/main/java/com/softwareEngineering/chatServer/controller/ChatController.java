package com.softwareEngineering.chatServer.controller;

import com.softwareEngineering.chatServer.entity.ChatInfo;
import com.softwareEngineering.chatServer.entity.User;
import com.softwareEngineering.chatServer.facade.ChatFacade;
import com.softwareEngineering.chatServer.service.ChatService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
@AllArgsConstructor
public class ChatController implements ChatFacade {
    ChatService chatService;
    @Override
    public List<ChatInfo> getUserChatHistory(int userId) {
       // return chatService.getUserChatHistory(userId);

        List<ChatInfo> list = new ArrayList<>(); //for test
        ChatInfo chatInfo = new ChatInfo();
        chatInfo.setFirstUserId(22);
        chatInfo.setId(33);
        chatInfo.setSecondUserId(44);
        list.add(chatInfo);
        return list;
    }

    @Override
    public void startChat(User user) {
        chatService.startChat(user);
    }
}
