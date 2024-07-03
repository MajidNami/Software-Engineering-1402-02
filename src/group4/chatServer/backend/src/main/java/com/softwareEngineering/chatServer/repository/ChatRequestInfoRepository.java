package com.softwareEngineering.chatServer.repository;

import com.softwareEngineering.chatServer.entity.ChatRequestInfo;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ChatRequestInfoRepository extends CrudRepository<ChatRequestInfo, Integer> {

    public List<ChatRequestInfo> findByUserId(int userId);

    public List<ChatRequestInfo> findByRespondedFalse();

    public List<ChatRequestInfo> findByRespondedFalseOrderByCreationDateAsc();

    public List<ChatRequestInfo> deleteByUserId(int UserId);


}
