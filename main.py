"""
ESP32 Mailbox Monitoring System

This script is designed to run on an ESP32 microcontroller to monitor the state of a physical mailbox using a button
sensor.
It leverages the Wi-Fi capability of the ESP32 to send HTTP POST requests to an AWS API endpoint, indicating the state
of the mailbox (open or closed). An LED is used to provide a visual indication of the mailbox state.

Components:
1. Button Sensor: Detects the state of the mailbox door (open or closed).
2. LED: Indicates the current state of the mailbox for local visualization.
3. Wi-Fi: Connects to a specified Wi-Fi network to enable HTTP communication.

Functionality:
1. State Detection:
   - The button sensor detects whether the mailbox door is open or closed.
   - The ESP32 monitors the state of the button sensor and detects changes in the mailbox state.

2. State Notification:
   - Upon detecting a change in the mailbox state, the ESP32 sends an HTTP POST request to the configured API endpoint.
   - The POST request includes information about the mailbox state (open or closed).

3. Wi-Fi Connectivity:
   - The ESP32 connects to a specified Wi-Fi network using provided SSID and password.
   - Handles reconnection logic in case the connection is lost.

4. LED Indication:
   - The LED is turned on when the mailbox is open and turned off when the mailbox is closed.

Configuration:
- Wi-Fi SSID and password need to be configured in the script for the ESP32 to connect to the internet.
- API endpoint URL for sending HTTP POST requests must be specified.

Dependencies:
- MicroPython: This script is intended to be run on MicroPython firmware on the ESP32.
- urequests: A MicroPython library for making HTTP requests.

Usage:
1. Flash MicroPython firmware on the ESP32.
2. Upload this script to the ESP32.
3. Configure the Wi-Fi credentials and API endpoint URL in the script.
4. Run the script to start monitoring the mailbox state.
"""
import time

import machine
import network
import urequests
from machine import Pin

import my_config

# Configuration
WIFI_SSID = my_config.wifi_ssid
WIFI_PASSWORD = my_config.wifi_password
WIFI_HOSTNAME = my_config.wifi_hostname

API_URL = my_config.status_notify_url

BUTTON_PIN = my_config.push_button_pin

DOOR_OPEN_RESEND_INTERVAL_SECONDS = my_config.door_open_resend_interval_seconds
KEEPALIVE_INTERVAL_SECONDS = my_config.keepalive_interval_seconds

RED_LED_PIN = my_config.red_led_pin
GREEN_LED_PIN = my_config.green_led_pin
BLUE_LED_PIN = my_config.blue_led_pin

red_led = Pin(RED_LED_PIN, Pin.OUT)
green_led = Pin(GREEN_LED_PIN, Pin.OUT)
blue_led = Pin(BLUE_LED_PIN, Pin.OUT)


def set_led_color(red, green, blue):
    # Setting pin value to 0 turns it on due to common cathode configuration
    red_led.value(red)
    green_led.value(green)
    blue_led.value(blue)


# Setup Wi-Fi connection
def connect_wifi(ssid, password, hostname):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(dhcp_hostname=hostname)  # Set the DHCP hostname before connecting

    attempt_count = 0

    print('Connecting to network:', ssid)

    while not wlan.isconnected() and attempt_count < 10:
        print('Attempting to connect to network, attempt', attempt_count + 1)
        wlan.connect(ssid, password)

        # Wait for 30 seconds for the connection to establish
        for _ in range(30):
            if wlan.isconnected():
                print('Connected to Wi-Fi')
                return
            time.sleep(7)

        attempt_count += 1
        print('Connection attempt failed, retrying...')

    if not wlan.isconnected():
        machine.reset()


# Function to send HTTP POST request
def send_post(message):
    """
    Sends a POST request to the configured API_URL with a suffix indicating the mailbox door state.

    The function constructs the URL based on the message parameter ('open' or 'closed') and sends a POST request to
    the server. It handles exceptions by printing error messages and triggering a system reset.

    Parameters:
    - message (str): The state of the mailbox door to notify about. Expected values are 'open' or 'closed'.

    Returns:
    None

    Raises:
    - Exception: If the POST request fails for any reason, it prints the error and calls reset_esp().
    """
    send_url = API_URL + '/closed'
    if message == 'open':
        print('Mailbox is open')
        send_url = API_URL + '/open'
    elif message == 'closed':
        print('Mailbox is closed')
    else:
        print('Invalid message:', message)
        return

    try:
        response = urequests.post(send_url, headers={'Content-Type': 'application/json'})
        print(response.text)
        response.close()
    except Exception as e:
        print('Failed to send POST request:', e)
        machine.reset()


def main():
    # Initialize GPIO for button
    button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

    # Main loop
    door_state = None  # None, 'open', 'closed'
    last_door_event_time = time.time()
    last_keepalive_time = time.time()

    connect_wifi(WIFI_SSID, WIFI_PASSWORD, WIFI_HOSTNAME)

    while True:
        # Read button state
        current_state = 'open' if button.value() == 1 else 'closed'
        if current_state == 'open':
            set_led_color(True, True, True)
        else:
            set_led_color(False, False, False)

        # Detect state change
        if current_state != door_state:
            door_state = current_state
            last_door_event_time = time.time()
            send_post(door_state)

        # Resend POST message based on door state
        if door_state == 'open' and time.time() - last_door_event_time >= DOOR_OPEN_RESEND_INTERVAL_SECONDS:
            send_post('open')
            last_door_event_time = time.time()
        elif door_state == 'closed' and time.time() - last_keepalive_time >= KEEPALIVE_INTERVAL_SECONDS:
            send_post('closed')
            last_keepalive_time = time.time()

        # Polling delay
        time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        machine.reset()
