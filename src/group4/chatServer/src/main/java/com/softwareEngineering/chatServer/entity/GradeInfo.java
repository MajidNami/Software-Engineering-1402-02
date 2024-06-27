package com.softwareEngineering.chatServer.entity;

import com.softwareEngineering.chatServer.enumeration.UserGrade;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;

@Entity
@Setter
@Getter
public class GradeInfo {

    @Id
    private int id;

    private int userId;

    private UserGrade grade;
}
