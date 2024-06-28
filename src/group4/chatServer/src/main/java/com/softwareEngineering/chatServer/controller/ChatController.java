package com.softwareEngineering.chatServer.controller;

import com.softwareEngineering.chatServer.dto.ChatHistoryResponseDto;
import com.softwareEngineering.chatServer.dto.RequestDto;
import com.softwareEngineering.chatServer.dto.StartChatResponseDto;
import com.softwareEngineering.chatServer.facade.ChatFacade;
import com.softwareEngineering.chatServer.service.ChatService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.RestController;

@RestController
@AllArgsConstructor
public class ChatController implements ChatFacade {
    ChatService chatService;

    @Override
    public ChatHistoryResponseDto getUserChatHistory(RequestDto dto) {
        return chatService.getUserChatHistory(dto);
    }

    @Override
    public StartChatResponseDto startChat(RequestDto dto) {
        return chatService.startChat(dto);
    }
}
