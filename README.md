# IoT Platform

A platform to visualize sensor data, receive alerts and perform actions using a raspberry PI.

Technologies:
- Python based scripts to read sensor data and publish using MQTT
- MQTT for data transfer between raspberry PI and the backend
- MongoDB for data storage
- NodeJS for the worker node, websocket server and the REST API
- Socket.IO for websockets
- React for the Web GUI
- Deployment using a GCP compute engine instance using docker and terraform.