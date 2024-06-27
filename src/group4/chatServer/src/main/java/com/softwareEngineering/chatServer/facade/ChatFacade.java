package com.softwareEngineering.chatServer.facade;

import com.softwareEngineering.chatServer.entity.ChatInfo;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

public interface ChatFacade {
    String baseUrl = "/chat";

    @GetMapping(value = baseUrl, produces = MediaType.APPLICATION_JSON_VALUE)
    List<ChatInfo> getUserChatHistory(int userId);

}
