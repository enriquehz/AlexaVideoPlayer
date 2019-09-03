#!/usr/bin/env python3
 
import paho.mqtt.client as mqtt
import subprocess
 
def hdmi_on():
    CONTROL = "vcgencmd"
    CONTROL_BLANK = [CONTROL, "display_power", "1"]
    subprocess.call(CONTROL_BLANK)
 
def hdmi_off():
    CONTROL = "vcgencmd"
    CONTROL_BLANK = [CONTROL, "display_power", "0"]
    subprocess.call(CONTROL_BLANK)
 
def on_connect(client, userdata, flags, rc):
  print("Connected to MQTT broker")
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    if msg.payload.decode() == "on":
        hdmi_on()
    elif msg.payload.decode() == "off":
        hdmi_off()
    else:
        pass
 
client = mqtt.Client()
client.username_pw_set( "User" , "Password" )
client.connect( "m23.cloudmqtt.com", 17905, 60)
client.subscribe( "frame/red/display" , qos=0)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
