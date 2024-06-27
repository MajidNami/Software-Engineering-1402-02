package com.softwareEngineering.chatServer.entity;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;
import java.util.Date;
import java.util.List;

@Entity
@Setter
@Getter
public class ChatInfo {

    @Id
    private int id;

    private int firstUserId;

    private int secondUserId;
}
