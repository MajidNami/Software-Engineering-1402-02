package com.softwareEngineering.chatServer.config;

import io.getstream.chat.java.exceptions.StreamException;
import lombok.Getter;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
@Getter
public class GetStreamConfig {
    private String STREAM_KEY;
    private String STREAM_SECRET;

    public GetStreamConfig(@Value("${STREAM_KEY}") String key, @Value("${STREAM_SECRET}") String secret) throws StreamException {
        STREAM_KEY = key;
        STREAM_SECRET = secret;
        System.setProperty("STREAM_KEY", STREAM_KEY);
        System.setProperty("STREAM_SECRET", STREAM_SECRET);
    }


}
