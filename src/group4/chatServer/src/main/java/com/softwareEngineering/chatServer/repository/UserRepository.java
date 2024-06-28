package com.softwareEngineering.chatServer.repository;

import com.softwareEngineering.chatServer.entity.User;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends CrudRepository<User, Integer> {
    User findById(int id);

    User findByName(String name);

    User findByUsername(String username);

}
