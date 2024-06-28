package com.softwareEngineering.chatServer.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.Setter;


@Setter
@Getter
@Entity
public class GradeInfo {

    @Id
    private int id;

    private int userId;

    private String grade;
}
