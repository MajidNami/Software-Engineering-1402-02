package com.softwareEngineering.chatServer.entity;


import com.softwareEngineering.chatServer.enumeration.UserGrade;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
@Setter
@Getter
public class User {

    @Id
    private int id;
    private String name;
}
