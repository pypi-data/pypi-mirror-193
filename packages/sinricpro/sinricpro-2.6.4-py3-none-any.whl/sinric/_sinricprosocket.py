"""
 *  Copyright (c) 2019 Sinric. All rights reserved.
 *  Licensed under Creative Commons Attribution-Share Alike (CC BY-SA)
 *
 *  This file is part of the Sinric Pro (https://github.com/sinricpro/)
"""

from websockets import client
from websockets.exceptions import ConnectionClosed
import json
from ._mainqueue import queue
from ._cbhandler import CallBackHandler
from ._signature import Signature
from time import time
import asyncio
import pkg_resources
class SinricProSocket(Signature):

    def __init__(self, appKey, deviceId, callbacks, enable_trace=False, logger=None, restore_states=False,
                 secretKey="", loopDelay=0.5):
        self.appKey = appKey
        self.secretKey = secretKey
        self.restore_states = restore_states
        self.logger = logger
        self.deviceIds = deviceId
        self.connection = None
        self.callbacks = callbacks
        self.loopDelay = loopDelay

        self.callbackHandler = CallBackHandler(self.callbacks, enable_trace, self.logger, self.restore_states,
                                               secretKey=self.secretKey)
        self.enableTrace = enable_trace
        Signature.__init__(self, self.secretKey)

    async def connect(self):  # Producer
        sdk_version = pkg_resources.require("sinricpro")[0].version
        self.connection = await client.connect('ws://ws.sinric.pro',
                                                          extra_headers={'appkey': self.appKey,
                                                                         'deviceids': ';'.join(self.deviceIds),
                                                                         'platform': 'python',
                                                                         'sdkversion' : sdk_version,
                                                                         'restoredevicestates': (
                                                                             'true' if self.restore_states else 'false')},
                                                          ping_interval=30000, ping_timeout=10000)
        if self.connection.open:
            self.logger.success(f"{'Connected :)'}")
            timestamp  = await self.connection.recv()
            if(int(time()) - json.loads(timestamp).get('timestamp') > 60000):
                self.logger.warning(f'Timestamp is not in sync check your system time. 🙄🙄🙄🙄🙄:(')
            return self.connection

    async def receiveMessage(self, connection):
        while True:
            try:
                message = await connection.recv()
                if self.enableTrace:
                    self.logger.info(f"Request : {message}")
                requestJson = json.loads(message)
                queue.put([requestJson, 'socket_response'])
                await asyncio.sleep(self.loopDelay)
            except ConnectionClosed as e:
                self.logger.info('Connection with server closed')
                raise e

    async def handleQueue(self):
        while True:
            await asyncio.sleep(self.loopDelay)
            
            while queue.qsize() > 0:
                await self.callbackHandler.handleCallBacks(queue.get(), self.connection, None)
