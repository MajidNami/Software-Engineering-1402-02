package com.softwareEngineering.chatServer.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.Setter;


@Setter
@Getter
@Entity
public class ChatInfo {

    @Id
    private int id;

    private int firstUserId;

    private String firstUserName;

    private int secondUserId;

    private String secondUserName;


}
