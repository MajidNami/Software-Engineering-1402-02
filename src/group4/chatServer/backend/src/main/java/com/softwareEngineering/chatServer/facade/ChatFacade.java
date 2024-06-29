package com.softwareEngineering.chatServer.facade;

import com.softwareEngineering.chatServer.dto.ChatHistoryResponseDto;
import com.softwareEngineering.chatServer.dto.RequestDto;
import com.softwareEngineering.chatServer.dto.StartChatResponseDto;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

public interface ChatFacade {
    String baseUrl = "/chat";

    @PostMapping(value = baseUrl + "/chatHistory", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
    ChatHistoryResponseDto getUserChatHistory(@RequestBody RequestDto requestDto);

    @PostMapping(value = baseUrl + "/startChat", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
    StartChatResponseDto startChat(@RequestBody RequestDto requestDto);


}
