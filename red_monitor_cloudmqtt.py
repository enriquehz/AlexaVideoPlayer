#!/usr/bin/env python3
 
import paho.mqtt.client as mqtt
import subprocess

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep 

VIDEO_PATH = Path("home/pi/Desktop/Videos/vistasur.mkv")
 
def hdmi_on():
    CONTROL = "vcgencmd"
    CONTROL_BLANK = [CONTROL, "display_power", "1"]
    subprocess.call(CONTROL_BLANK)
 
def hdmi_off():
    CONTROL = "vcgencmd"
    CONTROL_BLANK = [CONTROL, "display_power", "0"]
    subprocess.call(CONTROL_BLANK)
    
def play_video(video):
    subprocess.call("omxplayer" video)
 
def on_connect(client, userdata, flags, rc):
  print("Connected to MQTT broker")
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    if msg.payload.decode() == "on":
        hdmi_on()
        player = OMXPlayer(VIDEO_PATH)
        sleep(5)
    elif msg.payload.decode() == "off":
        hdmi_off()
    else:
        pass
 
client = mqtt.Client() #Service from CloudMQTT
client.username_pw_set( "User" , "Password" ) # Change "User" and "Password" 
client.connect( "soldier.cloudmqtt.com"", 15440, 60) 
client.subscribe( "alexa/prueba" , qos=0)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
