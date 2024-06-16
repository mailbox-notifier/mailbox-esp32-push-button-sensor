# mailbox-esp32-push-button-sensor
use micropython on an esp32 to sense (snail) mailbox door status 

# Mailbox Monitoring System Documentation

## 1. Introduction

- **Project Overview**
- **Objectives**

## 2. Hardware Components

- **ESP32 Microcontroller**
    - Specifications
    - Features
- **Button Sensor**
    - Specifications
    - Features
- **LED Indicator**
    - Specifications
    - Features
- **Power Supply**
    - Specifications
    - Features

## 3. Hardware Parts List

- **ESP32 Development Board**
- **Button Sensor (e.g., tactile button)**
- **LED (any color)**
- **Resistors (for LED, e.g., 220 ohms)**
- **Breadboard and Jumper Wires**
- **Power Supply (e.g., USB power adapter)**
- **Enclosure for ESP32 (optional, for protection)**
- **Mounting Tape or Screws (for securing components in the mailbox)**

## 4. Hardware Assembly

- **Wiring Diagram**
- **Assembly Instructions**
- **Installation in Mailbox**
    - Placement of ESP32
    - Placement of Button Sensor
    - Placement of LED Indicator

## 5. ESP32 Firmware

- **Overview**
    - Purpose
    - Features
- **Code Structure**
    - Main Functions
    - Libraries Used
- **Wi-Fi Connectivity**
    - Configuration Instructions
    - Troubleshooting
- **State Detection Logic**
    - Button Press Detection
    - State Transitions
- **HTTP POST Requests**
    - Endpoint Configuration
    - Payload Structure
- **LED Indicator Logic**
    - State Indications

## 6. AWS Lambda Functions

- **Overview**
    - Purpose
    - Features
- **State Management Lambda**
    - Function Logic
    - Event Handling
    - DynamoDB Integration
    - SNS Notifications
- **Health Check Lambda**
    - Function Logic
    - Timestamp Verification
    - Alerting Mechanism

## 7. Mailbox State Machine

- **State Diagram**
- **State Definitions**
    - OPEN
    - CLOSED
    - AJAR
- **State Transitions**
    - Transition Conditions
- **DynamoDB Schema**
    - Table Structure
    - Attributes

## 8. AWS Services Integration

- **DynamoDB**
    - Table Configuration
    - Data Storage Logic
- **SNS (Simple Notification Service)**
    - Notification Configuration
    - Alerting Logic

## 9. System Deployment

- **ESP32 Firmware Upload**
    - Tools Required
    - Step-by-Step Instructions
- **AWS Lambda Deployment**
    - Function Configuration
    - Deployment Steps
- **DynamoDB Setup**
    - Table Creation
    - Configuration Steps
- **SNS Setup**
    - Topic Creation
    - Subscription Configuration

## 10. Testing and Validation

- **ESP32 Testing**
    - Connectivity Test
    - State Detection Test
- **Lambda Functions Testing**
    - State Management Test
    - Health Check Test
- **End-to-End System Test**
    - Test Scenarios
    - Expected Outcomes

## 11. Troubleshooting

- **Common Issues**
- **Diagnostic Steps**
- **Solutions**

## 12. Maintenance

- **Regular Checks**
- **Firmware Updates**
- **AWS Services Monitoring**

## 13. Appendices

- **Code Listings**
- **Circuit Diagrams**
- **Configuration Files**
- **References**

![](.README_images/12-volt-power-supply.png)

![](.README_images/mailbox-underside-before-circuit-board-attached.png)

![](.README_images/circuit-board-side-view.png)

![](.README_images/garage-floor-power-cable-to-outside.png)

![](.README_images/mailbox-pole-with-cable-attached.png)

![](.README_images/circuit-board-top-view.png)

![](.README_images/mailbox-underside-with-fitted-circuit-board.png)

![](.README_images/mailbox-push-button-front-view.png)

![](.README_images/mailbox-inside-back-view.png)

![](.README_images/mailbox-push-button-side-view.png)