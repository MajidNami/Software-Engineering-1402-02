package com.softwareEngineering.chatServer.dto;

import com.softwareEngineering.chatServer.entity.ChatInfo;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Setter
@Getter
public class ChatHistoryResponseDto {
    private List<ChatInfo> chatInfoList;
}
