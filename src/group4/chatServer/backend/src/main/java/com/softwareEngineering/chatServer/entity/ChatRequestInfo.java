package com.softwareEngineering.chatServer.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

import java.util.Date;

@Setter
@Getter
@Entity
@Table(name = "chatrequestinfo")
public class ChatRequestInfo {

    @Id
    private int id;
    private String channelId;
    private int userId;
    private boolean responded;
    private Date creationDate;
}
