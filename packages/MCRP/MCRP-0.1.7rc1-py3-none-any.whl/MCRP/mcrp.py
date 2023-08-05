"""
    MineCraft Rewrite Proxy
    =======================
"""

import traceback
import logging
from importlib import import_module
from unittest.mock import MagicMock
from time import sleep
from Crypto.Cipher import AES
import datetime

import cubelib
import MCRP

from .tcproxy import tcproxy

from typing import Optional, List, Callable, Tuple
from types import ModuleType

Relative = MagicMock()

class ProtocolDecryptor:
    """
        Protocol Decryptor Prototype
    """

    name: str
    version: str

    def __init__(self, logger):
        pass

    def EncryptionRequest(self, server_id: str, public_key: bytes, verify_token: str) -> Tuple[bytes, str, str]:
        """
        External Encryption Request handler for decryption setup purposes

        Args:
            server_id (str): EncryptionRequest.ServerID
            public_key (bytes): EncryptionRequest.PublicKey
            verify_token (bytes): EncryptionRequest.VerifyToken
        
        Returns:
            server_id (str): New server id
            public_key (bytes): New public key
            verify_token (bytes): New verify token
        """        
        pass
    
    def EncryptionResponse(self, shared_secret: bytes, verify_token: bytes) -> Tuple[bytes, bytes, bytes]:
        """
        External Encryption Response handler for decryption setup purposes

        Args:
            shared_secret (bytes): EncryptionResponse.SharedSecret
            verify_token (bytes): EncryptionResponse.VerifyToken
        
        Returns:
            shared_secret (bytes): Plain shared secret
            shared_secret (bytes): Encrypted shared secret
            verify_token (bytes): Encrypted verify token
        """          
        pass

class AESCipher:
    
    Encryptor: AES
    Decryptor: AES

    def __init__(self, secret: bytes):
        self.Encryptor = AES.new(secret, AES.MODE_CFB, iv=secret)
        self.Decryptor = AES.new(secret, AES.MODE_CFB, iv=secret)

class AESComplex:

    ClientCipher: AESCipher
    ServerCipher: AESCipher

    def __init__(self, secret):
        self.ClientCipher = AESCipher(secret)
        self.ServerCipher = AESCipher(secret)

class MCRewriteProxy(tcproxy):    

    ServerBoundBuff: List[bytes]
    ClientBoundBuff: List[bytes]

    PROTOCOL: ModuleType = cubelib.proto
    STATE: cubelib.state = cubelib.state.Handshaking
    COMPRESSION_THR: int = -1

    PASS_THROUGH: bool = False
    decryptor: Optional[ProtocolDecryptor] = None
    cipher: AESComplex

    HANDLERS: dict # {cubelib.proto.v47.ServerBound.ChatMessage: [False, <function handler at 0x00000...>]}
    REL_HANDLERS: dict

    ServerBoundHandler: Optional[Callable] = None
    ClientBoundHandler: Optional[Callable] = None
    
    def __init__(self, listen_addr: tuple, upstream_addr: tuple,
        loglevel = logging.ERROR, decryptor: Optional[ProtocolDecryptor] = None,
            leave_debug_journals: bool = False):
        
        self.ServerBoundBuff = [b""] # it's a little trick to make immutable type (bytes)
        self.ClientBoundBuff = [b""] # mutable to pass reference to it
        self.HANDLERS = {}
        self.REL_HANDLERS = {}
        self.leave_debug_journals = leave_debug_journals

        self.logger = logging.getLogger("MCRP")
        self.logger.setLevel(loglevel)
        super().__init__(listen_addr, upstream_addr)
        self.logger.info(f"Running MCRP v{MCRP.version} (cubelib version {cubelib.version})")
        self.logger.info(f"Proxying config is: \u001b[97m{':'.join([str(a) for a in listen_addr])} \u001b[92m-> \u001b[97m{':'.join([str(a) for a in upstream_addr])}")
        self.logger.info(f"Using protocol decryptor: {decryptor.name}/{decryptor.version}") if decryptor else None
        self.logger.info(f"Debug journals enabled!") if leave_debug_journals else None
        if decryptor:
            crlogger = logging.getLogger("MCRP/CRYPTO")
            crlogger.setLevel(loglevel)
            self.decryptor = decryptor(crlogger)              
    
    def _waiting_for_client(self):
        
        print()
        self.logger.info(f"Waiting for client connection...")

    def _new_client(self):

        self.logger.info(f"New client, creating connection to the server")
            
    def _new_server(self):

        self.logger.info(f"Connected to the server")
        self.logger.info("Reseting state to Handshaking")
        self.STATE = cubelib.state.Handshaking
        self.PROTOCOL = cubelib.proto
        self.COMPRESSION_THR = -1
        self.ServerBoundBuff = [b""]
        self.ClientBoundBuff = [b""]
        self.PASS_THROUGH = False        
        self.cipher = None
        if self.leave_debug_journals:
            dt = datetime.datetime.now()
            m = dt.strftime("%B")[:3]
            ts = dt.strftime(f"%d {m} %Y %H-%M-%S")
            self.journal = open(f"{ts}.mcdj", "wb")

        # Remove relative handlers for old protocol
        for handler in dict(self.HANDLERS):
            if self.HANDLERS[handler][0] == True:
                del self.HANDLERS[handler]        
    
    def _client_lost(self):

        self.logger.info(f"Client disconnected")
    
    def _server_lost(self):

        if self.leave_debug_journals:
            self.journal.close()
        self.logger.info(f"Server disconnected")
    
    def _server_error(self, error):
        
        self.logger.error(f"Failed to connect to the server due to an error: {error}")
    
    def _from_client(self, data):

        return self._handle_bytes(data, self.ServerBoundBuff, cubelib.bound.Server)

    def _from_server(self, data):

        return self._handle_bytes(data, self.ClientBoundBuff, cubelib.bound.Client)

    def _client_error(self, error):
        
        self.logger.critical(f"Failed to bind socket to local addr due to an error: {error}")
        exit()

    def _handle_bytes(self, data, buff, bound):
        
        if self.leave_debug_journals:
            self.journal.write(b"\xff" if bound is cubelib.bound.Server else b"\xfe")
            self.journal.write(cubelib.types.VarInt.build(len(data)))
            self.journal.write(data)

        was_encrypted = False
        if self.cipher:
            if bound is cubelib.bound.Server:
                data = self.cipher.ServerCipher.Decryptor.decrypt(data)
            elif bound is cubelib.bound.Client:
                data = self.cipher.ClientCipher.Decryptor.decrypt(data)
            was_encrypted = True

        if data[:3] == b"\xFE\x01\xFA" and self.STATE == cubelib.state.Handshaking:
            self.logger.warn("Client sent legacy MC|PingHost! Unsupported! Enabling pass-trough!")
            self.PASS_THROUGH = True

        if self.PASS_THROUGH:
            r = b""
            if buff[0]:
                r += buff[0]
                buff[0] = b""
            r += data
            return r

        try:
            packs = []
            buff[0] += data
            buff[0] = cubelib.readPacketsStream(buff[0], self.COMPRESSION_THR, bound, packs)            

            ret = b""
            for p in packs:
                try:
                    hr = self._handle_packet(p)
                    if isinstance(hr, bytes):
                        ret += hr
                    elif isinstance(hr, cubelib.p.Night):
                        ret += hr.build(self.COMPRESSION_THR if p.compressed else -1)
                    elif hr is False:
                        ret += b""
                    else:
                        ret += p.build(self.COMPRESSION_THR if p.compressed else -1)
                        if hr is  not None:
                            self.logger.warn(f'обработчик сделал хуйню (вернул {hr})')                    

                except Exception as e:
                    self.logger.warn(f"Exception in {bound.name}Bound Handler: {e}")                    
                    self.logger.warn(traceback.format_exc())
                    ret += p.build(self.COMPRESSION_THR if p.compressed else -1)
            
            if self.cipher and was_encrypted:
                return self.cipher.ServerCipher.Encryptor.encrypt(ret) if bound is cubelib.bound.Server else self.cipher.ClientCipher.Encryptor.encrypt(data)            
            return ret

        except Exception as e:
            self.logger.error(f"Exception in {bound.name}Bound: {e}")
            self.logger.error(traceback.format_exc())            

    def _handle_packet(self, pack):
        
        p = pack.resolve(self.STATE, self.PROTOCOL)
        t = p.__class__

        # Global bound handlers
        if pack.bound == cubelib.bound.Client:
            self.ClientBoundHandler(p) if self.ClientBoundHandler else None
        else:
            self.ServerBoundHandler(p) if self.ServerBoundHandler else None                

        # Handle handshake
        if t is cubelib.proto.ServerBound.Handshaking.Handshake:
            self._handle_handshake(p)

        if self.STATE is cubelib.state.Login:
            
            # Handle SetCompression
            if t is self.PROTOCOL.ClientBound.Login.SetCompression:
                self.logger.info(f"Point of switching-on compression with threshold {p.Threshold}")
                self.COMPRESSION_THR = p.Threshold

            # Handle LoginSuccess
            if t is self.PROTOCOL.ClientBound.Login.LoginSuccess:
                self.STATE = cubelib.state.Play
                self.logger.info(f"State changed to {self.STATE}")
            
            # Handle EncryptionRequest
            if t is self.PROTOCOL.ClientBound.Login.EncryptionRequest:
                if self.decryptor:
                    hr = self.decryptor.EncryptionRequest(p.ServerID, p.PublicKey, p.VerifyToken)
                    return self.PROTOCOL.ClientBound.Login.EncryptionRequest(*hr)
                return

            # Handle EncryptionResponse
            if t is self.PROTOCOL.ServerBound.Login.EncryptionResponse:
                if self.decryptor:
                    hr = self.decryptor.EncryptionResponse(p.SharedSecret, p.VerifyToken)
                    self.cipher = AESComplex(hr[0])
                    self.logger.info(f"Protocol encryption is set, but you provided a shared secret")
                    self.logger.info(f"Shared secret: {hr[0].hex()}")
                    return self.PROTOCOL.ServerBound.Login.EncryptionResponse(*hr[1:])
                self.logger.warn(f"Minecraft client sent EncryptionResponse! That mean full symmetric encryption enabling, so we can't proceed with protocol analyzing. Just proxying!")
                self.PASS_THROUGH = True
                return

        # Call a handler if exists        
        return self.HANDLERS[t][1](p) if t in self.HANDLERS else None
        
    def _handle_handshake(self, p):

        if p.NextState == cubelib.NextState.Status:
            self.STATE = cubelib.state.Status
            return
        
        self.STATE = cubelib.state.Login
        self.logger.info(f"State changed to {self.STATE}, trying to load protocol v{p.ProtoVer}")
        if p.ProtoVer in cubelib.supported_versions:        
            self.PROTOCOL = import_module(f"cubelib.proto.v{p.ProtoVer}")
        else:
            self.logger.warn(f"Failed to load protocol v{p.ProtoVer}, looks like its unsupported! Enabling enabling pass-through")
            self.PASS_THROUGH = True

        self.logger.info(f"Successfuly loaded protovol v{p.ProtoVer}" + (f", compiling {len(self.REL_HANDLERS)} handlers..." if self.REL_HANDLERS else ""))

        for handler in self.REL_HANDLERS:            
            attrs = handler._extract_mock_name().split('.')[1:]
            obj = self.PROTOCOL
            for attr in attrs:
                obj = getattr(obj, attr, None)
                if not obj:
                    self.logger.warn(f'Failed to resolve handler {self.PROTOCOL.__name__}.{".".join(attrs)}')
                    break
            if obj:
                self.logger.debug(f"Successfully resolved {handler} into {obj}")
                self.HANDLERS[obj] = [True, self.REL_HANDLERS[handler]]

    def on(self, type_):
        def no(fun):
            if isinstance(type_, MagicMock):
                self.REL_HANDLERS[type_] = fun
            else:
                self.HANDLERS[type_] = [False, fun]
        return no
    
    def ClientBound(self, handler):
        self.ClientBoundHandler = handler
    
    def ServerBound(self, handler):
        self.ServerBoundHandler = handler

    def join(self):
        
        self.logger.info(f'Registred direct handlers list[{len(self.HANDLERS)}]:')
        for handler in self.HANDLERS:
            self.logger.info(f"    {handler}")

        self.logger.info(f'Registred relative handlers list[{len(self.REL_HANDLERS)}]:')
        for handler in self.REL_HANDLERS:            
            self.logger.info(f"    {'.'.join(handler._extract_mock_name().split('.')[1:])}")

        self.logger.debug('Entering mainloop')
        super().join()    
        #p = self.PROTOCOL.ClientBound.Play.Disconnect('proxy_closed').build(self.COMPRESSION_THR)
        #self.Client.send(p)
        self.logger.debug('Exiting')
