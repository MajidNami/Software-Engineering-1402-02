package com.softwareEngineering.chatServer.service;

import com.softwareEngineering.chatServer.dto.ChatHistoryResponseDto;
import com.softwareEngineering.chatServer.dto.RequestDto;
import com.softwareEngineering.chatServer.dto.StartChatResponseDto;
import com.softwareEngineering.chatServer.entity.ChatInfo;
import com.softwareEngineering.chatServer.entity.ChatRequestInfo;
import com.softwareEngineering.chatServer.entity.GradeInfo;
import com.softwareEngineering.chatServer.entity.User;
import com.softwareEngineering.chatServer.repository.ChatInfoRepository;
import com.softwareEngineering.chatServer.repository.ChatRequestInfoRepository;
import com.softwareEngineering.chatServer.repository.GradeInfoRepository;
import com.softwareEngineering.chatServer.repository.UserRepository;
import io.getstream.chat.java.exceptions.StreamException;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.List;
import java.util.UUID;

@Service
@AllArgsConstructor
public class ChatService {

    ChatInfoRepository chatInfoRepository;
    ChatRequestService chatRequestService;
    GradeInfoRepository gradeInfoRepository;
    GetStreamService getStreamService;
    ChatRequestInfoRepository chatRequestInfoRepository;
    UserRepository userRepository;

    public List<ChatInfo> getUserChatHistory(User user) {
        int userId = user.getId();
        return chatInfoRepository.findByFirstUserIdOrSecondUserId(userId, userId);
    }

    public ChatHistoryResponseDto getUserChatHistory(RequestDto dto) {
        User user = userRepository.findByUsername(dto.getUsername());
        List<ChatInfo> chatRequestInfoList = chatInfoRepository.findByFirstUserIdOrSecondUserId(user.getId(), user.getId());
        ChatHistoryResponseDto responseDto = new ChatHistoryResponseDto();
        responseDto.setChatInfoList(chatRequestInfoList);
        return responseDto;
    }

    public StartChatResponseDto startChat(RequestDto dto) {
        User user = userRepository.findByUsername(dto.getUsername());
        GradeInfo gradeInfo = gradeInfoRepository.findByUserId(user.getId());
        String grade = "A";
        if (gradeInfo != null) {
            grade = gradeInfo.getGrade();
        }
        ChatRequestInfo requestInfo = chatRequestService.findTopRequestWithSpecificGrade(grade, user.getId());
        if (requestInfo == null) {
            // we could not find a partner please wait
            String channelId = UUID.randomUUID().toString();
            try {
                getStreamService.createChannel(channelId);
                getStreamService.createUser(user.getUsername());
                getStreamService.addMember(user.getUsername(), channelId);
                String token = getStreamService.generateToken(user.getUsername());
                ChatRequestInfo newRequest = new ChatRequestInfo();
                newRequest.setResponded(false);
                newRequest.setUserId(user.getId());
                newRequest.setCreationDate(new Date());
                newRequest.setChannelId(channelId);
                chatRequestService.addChatRequest(newRequest);
                StartChatResponseDto responseDto = new StartChatResponseDto();
                responseDto.setChannelId(channelId);
                responseDto.setToken(token);
                return responseDto;
            } catch (StreamException e) {
                throw new RuntimeException(e);
            }
        }
        try {
            String channelId = requestInfo.getChannelId();
            getStreamService.createUser(user.getUsername());
            getStreamService.addMember(user.getUsername(), channelId);
            String token = getStreamService.generateToken(user.getUsername());
            requestInfo.setResponded(true);
            chatRequestInfoRepository.save(requestInfo);
            StartChatResponseDto responseDto = new StartChatResponseDto();
            responseDto.setChannelId(channelId);
            responseDto.setToken(token);
            return responseDto;
        } catch (StreamException e) {
            throw new RuntimeException(e);
        }
    }
}
