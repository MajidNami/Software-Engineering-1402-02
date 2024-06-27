package com.softwareEngineering.chatServer.repository;

import com.softwareEngineering.chatServer.entity.ChatInfo;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface ChatInfoRepository extends CrudRepository<ChatInfo, Integer> {

    List<ChatInfo> findByFirstUserIdOrSecondUserId(int firstUserId, int secondUserId);

}
