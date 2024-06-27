package com.softwareEngineering.chatServer.service;

import com.softwareEngineering.chatServer.entity.ChatRequestInfo;
import com.softwareEngineering.chatServer.entity.GradeInfo;
import com.softwareEngineering.chatServer.entity.User;
import com.softwareEngineering.chatServer.enumeration.UserGrade;
import com.softwareEngineering.chatServer.repository.ChatRequestInfoRepository;
import com.softwareEngineering.chatServer.repository.GradeInfoRepository;
import com.softwareEngineering.chatServer.repository.UserRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@AllArgsConstructor
public class ChatRequestService {

    ChatRequestInfoRepository chatRequestInfoRepository;
    GradeInfoRepository gradeInfoRepository;
    UserRepository userRepository;

    public ChatRequestInfo findTopRequestWithSpecificGrade(UserGrade grade, int requestingUserId) {
        List<ChatRequestInfo> allChatRequestInfoList = chatRequestInfoRepository.findByRespondedFalseOrderByCreationDateAsc();
        for (ChatRequestInfo request : allChatRequestInfoList) {
            if (request.getUserId() != requestingUserId) {
                GradeInfo gradeInfo = gradeInfoRepository.findByUserId(request.getUserId());
                if (gradeInfo.getGrade().equals(grade)) {
                    return request;
                }
            }
        }
        return null;
    }

    public User findPartnerByGrade(UserGrade grade, int requestingUserId) {
        ChatRequestInfo request = findTopRequestWithSpecificGrade(grade, requestingUserId);
        if (request == null) {
            return null;
        }
        return userRepository.findById(request.getUserId());
    }

    public Integer findPartnerIdByGrade(UserGrade grade, int requestingUserId) {
        ChatRequestInfo request = findTopRequestWithSpecificGrade(grade, requestingUserId);
        if (request == null) {
            return null;
        }
        return request.getUserId();
    }

    public void addChatRequest(ChatRequestInfo requestInfo){
        chatRequestInfoRepository.save(requestInfo);
    }
}
