package com.softwareEngineering.chatServer.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;


@Setter
@Getter
@Entity
@Table(name = "chatinfo")
public class ChatInfo {

    @Id
    private int id;

    private int firstUserId;

    private String firstUsername;

    private int secondUserId;

    private String secondUsername;


}
