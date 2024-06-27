package com.softwareEngineering.chatServer.controller;

import com.softwareEngineering.chatServer.entity.ChatInfo;
import com.softwareEngineering.chatServer.facade.ChatFacade;
import com.softwareEngineering.chatServer.service.ChatService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@AllArgsConstructor
public class ChatController implements ChatFacade {
    ChatService chatService;
    @Override
    public List<ChatInfo> getUserChatHistory(int userId) {
        return chatService.getUserChatHistory(userId);
    }
}
