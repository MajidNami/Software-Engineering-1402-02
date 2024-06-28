package com.softwareEngineering.chatServer.facade;

import com.softwareEngineering.chatServer.entity.ChatInfo;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.List;

public interface ChatFacade {
    String baseUrl = "/chat";

@PostMapping(value = baseUrl, consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
    List<ChatInfo> getUserChatHistory(@RequestBody int userId);

}
