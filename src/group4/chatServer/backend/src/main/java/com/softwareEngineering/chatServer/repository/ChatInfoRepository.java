package com.softwareEngineering.chatServer.repository;

import com.softwareEngineering.chatServer.entity.ChatInfo;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ChatInfoRepository extends CrudRepository<ChatInfo, Integer> {

    List<ChatInfo> findByFirstUserIdOrSecondUserId(int firstUserId, int secondUserId);

}
