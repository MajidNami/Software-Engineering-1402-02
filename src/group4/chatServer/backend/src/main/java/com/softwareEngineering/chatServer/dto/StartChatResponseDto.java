package com.softwareEngineering.chatServer.dto;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class StartChatResponseDto {
    private String channelId;
    private String token;
}
