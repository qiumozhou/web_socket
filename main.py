# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import eventlet
import socketio
from aiohttp import web



sio = socketio.AsyncServer(async_mode='aiohttp',cors_allowed_origins='*')
app = web.Application()
sio.attach(app)


@sio.event
async def connect(sid, environ):
    print("Client connect.", sid, environ)


# @sio.event
# async def change_room(sid, data):
#     print(data)
#     await sio.enter_room(sid, data)



@sio.event
async def disconnect(sid):
    print('disconnect ', sid)


@sio.event
async def hanxinStatusReply(sid,data):
    await sio.emit("hanxinStatusReply",data["data"],namespace=data["name"])



@sio.event
async def charging_server_status(sid,data):
    await sio.emit("chargingStatusReply",data["data"],namespace=data["name"])


@sio.event
async def agentMonitorAllReply(sid,data):
    await sio.emit("agentMonitorAllReply",data["data"],namespace=data["name"])


@sio.event
async def bwmsServerStatusReply(sid,data):
    await sio.emit("bwmsServerStatusReply",data["data"],namespace=data["name"])


@sio.event
async def rosNodeStatusReply(sid,data):
    await sio.emit("rosNodeStatusReply",data["data"],namespace=data["name"])


@sio.event
async def popAgentsDtcReply(sid,data):
    await sio.emit("popAgentsDtcReply",data["data"],namespace=data["name"])


@sio.event
async def elevatorStatusReply(sid,data):
    await sio.emit("elevatorStatusReply",data["data"],namespace=data["name"])


@sio.event
async def monitorReply(sid, data):
    await sio.send("monitorReply", data["data"], namespace=data["name"])


@sio.event
async def resumeReply(sid,data):
    await sio.emit("resumeReply",data["data"],namespace=data["name"])


if __name__ == '__main__':
    web.run_app(app, host="0.0.0.0", port=8000)

