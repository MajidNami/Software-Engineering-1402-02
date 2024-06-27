package com.softwareEngineering.chatServer.entity;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.Entity;
import javax.persistence.Id;
import java.util.Date;
import java.util.List;

@Entity
@Setter
@Getter
public class ChatRequestInfo {

    @Id
    private int id;
    private String channelId;
    private int userId;
    private boolean responded;
    private Date creationDate;
}
