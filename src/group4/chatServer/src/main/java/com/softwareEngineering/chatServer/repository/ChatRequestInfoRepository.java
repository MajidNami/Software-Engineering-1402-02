package com.softwareEngineering.chatServer.repository;

import com.softwareEngineering.chatServer.entity.ChatRequestInfo;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.Repository;

import java.util.List;

public interface ChatRequestInfoRepository extends CrudRepository<ChatRequestInfo, Integer> {

    List<ChatRequestInfo> findByUserId(int userId);

    List<ChatRequestInfo> findByRespondedFalse();
    List<ChatRequestInfo> findByRespondedFalseOrderByCreationDateAsc();

    List<ChatRequestInfo> deleteByUserId(int UserId);
}
