package com.softwareEngineering.chatServer.repository;

import com.softwareEngineering.chatServer.entity.GradeInfo;
import org.springframework.data.repository.CrudRepository;
public interface GradeInfoRepository extends CrudRepository<GradeInfo, Integer> {

    GradeInfo findByUserId(int userId);
}
