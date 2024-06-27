package com.softwareEngineering.chatServer.service;

import com.softwareEngineering.chatServer.entity.ChatInfo;
import com.softwareEngineering.chatServer.entity.ChatRequestInfo;
import com.softwareEngineering.chatServer.entity.GradeInfo;
import com.softwareEngineering.chatServer.entity.User;
import com.softwareEngineering.chatServer.enumeration.UserGrade;
import com.softwareEngineering.chatServer.repository.ChatInfoRepository;
import com.softwareEngineering.chatServer.repository.GradeInfoRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.List;

@Service
@AllArgsConstructor
public class ChatService {

    ChatInfoRepository chatInfoRepository;
    ChatRequestService chatRequestService;
    GradeInfoRepository gradeInfoRepository;

    public List<ChatInfo> getUserChatHistory(User user) {
        int userId = user.getId();
        return chatInfoRepository.findByFirstUserIdOrSecondUserId(userId, userId);
    }

    public List<ChatInfo> getUserChatHistory(int userId) {
        return chatInfoRepository.findByFirstUserIdOrSecondUserId(userId, userId);
    }

    public void startChat(User user) {
        GradeInfo gradeInfo = gradeInfoRepository.findByUserId(user.getId());
        UserGrade grade = UserGrade.A;
        if (gradeInfo != null) {
            grade = gradeInfo.getGrade();
        }
        ChatRequestInfo requestInfo = chatRequestService.findTopRequestWithSpecificGrade(grade, user.getId());
        int partnerId;
        if (requestInfo == null) {
            // we could not find a partner please wait
            ChatRequestInfo newRequest = new ChatRequestInfo();
            newRequest.setResponded(false);
            newRequest.setUserId(user.getId());
            newRequest.setCreationDate(new Date());
            chatRequestService.addChatRequest(newRequest);
        } else {
            //todo
        }

    }
}
