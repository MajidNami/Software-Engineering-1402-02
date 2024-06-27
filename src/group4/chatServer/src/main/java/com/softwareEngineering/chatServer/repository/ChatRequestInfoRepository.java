package com.softwareEngineering.chatServer.repository;

import com.softwareEngineering.chatServer.entity.ChatRequestInfo;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ChatRequestInfoRepository extends CrudRepository<ChatRequestInfo, Integer> {

    List<ChatRequestInfo> findByUserId(int userId);

    List<ChatRequestInfo> findByRespondedFalse();

    List<ChatRequestInfo> findByRespondedFalseOrderByCreationDateAsc();

    List<ChatRequestInfo> deleteByUserId(int UserId);
}
