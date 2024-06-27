package com.softwareEngineering.chatServer.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.Setter;
import org.springframework.stereotype.Component;


@Setter
@Getter
@Component
@Entity
public class ChatInfo {

    @Id
    private int id;

    private int firstUserId;

    private int secondUserId;
}
