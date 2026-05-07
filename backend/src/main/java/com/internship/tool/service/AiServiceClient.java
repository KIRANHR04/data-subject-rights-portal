package com.internship.tool.service;

import org.springframework.http.*;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

public class AiServiceClient {

    private final RestTemplate restTemplate = new RestTemplate();

    private final String AI_URL = "http://127.0.0.1:5000/generate";

    public String generateResponse(String prompt) {

        try {

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            Map<String, String> body = new HashMap<>();
            body.put("prompt", prompt);

            HttpEntity<Map<String, String>> request =
                    new HttpEntity<>(body, headers);

            ResponseEntity<String> response = restTemplate.exchange(
                    AI_URL,
                    HttpMethod.POST,
                    request,
                    String.class
            );

            return response.getBody();

        } catch (Exception e) {

            return null;
        }
    }
}