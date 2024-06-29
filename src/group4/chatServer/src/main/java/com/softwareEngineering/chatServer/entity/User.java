package com.softwareEngineering.chatServer.entity;


import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
@Entity
@Table(name = "USERS")
public class User {

    @Id
    private int id;
    private String name;
    private String username;

}
