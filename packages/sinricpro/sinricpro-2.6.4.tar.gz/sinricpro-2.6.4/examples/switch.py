from sinric import SinricPro 
import asyncio
 
APP_KEY = '24fc8298-3078-45f0-8197-8e9b0ef0aafc'
APP_SECRET = 'aef2c17c-2c02-4966-979c-eabf2ecfe7dd-eab83dc6-7ac3-4815-b6eb-823a58d2235c'
SWITCH_ID = '63dc87f607e1833ecb5383ad'

def power_state(device_id, state):
    print(device_id, state)
    return True, state
 
callbacks = {
    'powerState': power_state
}
 
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    client = SinricPro(APP_KEY, [SWITCH_ID], callbacks, enable_log=False, restore_states=False, secretKey=APP_SECRET)
    loop.run_until_complete(client.connect())

# To update the power state on server. 
# client.event_handler.raiseEvent(tvId, 'setPowerState',data={'state': 'On'})
