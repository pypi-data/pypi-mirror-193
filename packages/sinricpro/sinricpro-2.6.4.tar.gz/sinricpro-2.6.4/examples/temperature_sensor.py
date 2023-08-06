from sinric import SinricPro
import asyncio
from asyncio import sleep

APP_KEY = '24fc8298-3078-45f0-8197-8e9b0ef0aafc'
APP_SECRET = 'aef2c17c-2c02-4966-979c-eabf2ecfe7dd-eab83dc6-7ac3-4815-b6eb-823a58d2235c'
TEMPERATURE_SENSOR_ID = '63f5e7a65ec7d92a47127d5a'

def power_state(did, state):
    print(did, state)
    return True, state
 
async def events():
    while True:
        print("Send temperatureHumidityEvent!")
        client.event_handler.raiseEvent(TEMPERATURE_SENSOR_ID, 'temperatureHumidityEvent', data={'humidity': 75.3, 'temperature': 24})
        await sleep(60) # Server will trottle / block IPs sending events too often.

callbacks = {
    'powerState': power_state
}

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    client = SinricPro(APP_KEY, [TEMPERATURE_SENSOR_ID], callbacks, event_callbacks=events, enable_log=True, restore_states=False, secretKey=APP_SECRET)
    loop.run_until_complete(client.connect())

# To update the temperature on server. 
#client.event_handler.raiseEvent(temperatureSensorDeviceId, 'temperatureHumidityEvent', data={'humidity': 75.3, 'temperature': 24})