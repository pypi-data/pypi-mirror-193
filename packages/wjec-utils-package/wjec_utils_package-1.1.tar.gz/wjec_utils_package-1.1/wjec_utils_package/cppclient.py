"""
Module:   cppclient.py
Package:  varius/utils
Date:     Mar 2020
Owner:    WJE

Description:  A module to create, manage and communicate over a client socket with the C++
              side software of the OmniMonitor. This module uses communication via JSON strings
              which are specifically formatted as agreed upon by WJE staff working on software
              development.
"""

import json
from socket import socket, AF_INET, SOCK_DGRAM, timeout

MAX_UDP_PACKET_SIZE = 2048


class WJESocketException(Exception):
    def __init__(self, message):
        self.msg = message

    def __str__(self):
        return repr(self.msg)


def dict_to_jsonbytes(d):
    """
    convert a python dictionary into JSON string and then encode into bytes
    for transfer over a UDP socket
    :param d:
    :return:
    """
    return json.dumps(d).encode("ascii")


def jsonbytes_to_dict(b):
    """
    convert JSON/ bytes into a Python dictionary
    :param b:
    :return:
    """
    return json.loads(b.decode("ascii"))


def clean_socket(sock,
                 max_packet_length=MAX_UDP_PACKET_SIZE):
    """
    Function used to clean out the receive side of the socket before sending.
    Timeout is set to zero, so that if the socket is empty, there is no wait.
    The cpp_socket.recv will raise an excep if empty, so do nothing in that case.
    :return:
    """
    timeout_orig = sock.gettimeout()
    sock.settimeout(0.0)  # Set immediate timeout
    try:
        while sock.recv(max_packet_length):
            pass
    except Exception:
        pass
    sock.settimeout(timeout_orig)  # Reset socket timeout time


class SocketListener:
    """
    TODO: in progress
    Should be called something like:
    self.socket = SocketListener(...)
    msg = self.socket.receive_msg()
    -->parse messasge
    self.socket.ack <-- if needed
    """

    def __init__(self,
                 host,
                 port,
                 header_key,
                 payload_keys,
                 ack_msg,
                 timeout=0.05,
                 socket_family=AF_INET,
                 socket_type=SOCK_DGRAM,
                 max_receive_length=MAX_UDP_PACKET_SIZE):
        """

        Message protocol:
        {
        <header_key>:
            {
                <payload_keys[0]>: <data0>,
                <payload_keys[1]>: <data1>,
                ...
            }
        }
        :param host:
        :param port:
        :param header_key:  str - the header key in the received JSON dictionary
        :param payload_keys: array (str) - the keys for each message data
        :param ack_msg:
        :param timeout:
        :param socket_family:
        :param socket_type:
        :param max_receive_length:
        """
        self.sock = socket(socket_family, socket_type)
        self.sock.bind((host, port))
        self.last_msg = dict()
        self.ack_msg = ack_msg
        self.set_timeout(timeout)
        self.buffer_size = max_receive_length
        self.header_key = header_key
        for key in payload_keys:
            self.last_msg[key] = None

    def set_timeout(self,
                    timeout):
        """
        Wrapper for socket's 'settimeout' function.
        If None, socket will block.
        If set to 0, socket will not-block.
        Other non-negative float values set timeout.
        :param timeout: float, None - the timout to set
        """
        try:
            self.sock.settimeout(timeout)
        except ValueError as err:
            raise ValueError(err)

    def receive_msg(self):
        """
        Caution, if socket is set to blocking mode, the object will hang on this function.
        TODO: Enable blocking/non-blocking setting
        :return:
        """
        try:
            msg, addr = self.sock.recvfrom(self.buffer_size)
            return msg, addr
        except BlockingIOError as err:
            return None, None  # TODO, error when non-blocking socket has nothing
        except timeout:
            return None, None  # TODO, error when socket timesout
        except ValueError as err:
            return None, None   # TODO, when too many values to unpack

    def ack(self,
            address):
        """
        Send the ack message after a message is successfully parsed.
        :param address:
        :return:
        """
        self.sock.sendto(dict_to_jsonbytes(self.ack_msg),
                         address)

    def parse_msg(self,
                  msg,
                  ack_addr):
        """
        TODO: Should ack only if parsed message requires
        :param msg:
        :param ack_addr:
        :return:
        """
        try:
            msg_dict = jsonbytes_to_dict(msg)
            msg_payload = msg_dict[self.header_key]
            for key in msg_payload:
                self.last_msg[key] = msg_payload[key]
        except KeyError as err:
            pass  # TODO: error if message didn't have 'key'
        except TypeError as err:
            pass  # TODO: error if json couldn't parse message
        else:
            self.ack(ack_addr)
        return self.last_msg


class SocketSender:
    """

    """

    def __init__(self,
                 host,
                 port,
                 ack_msg,
                 timeout=0.05,
                 socket_family=AF_INET,
                 socket_type=SOCK_DGRAM,
                 max_receive_length=MAX_UDP_PACKET_SIZE,
                 send_attempts=10):
        """

        :param host:
        :param port:
        :param ack_msg:
        :param timeout:
        :param socket_family:
        :param socket_type:
        :param max_receive_length:
        :param send_attempts:
        """
        self.sock = socket(socket_family, socket_type)
        self.address = (host, port)
        self.sock.connect(self.address)
        self.ack_msg = ack_msg
        self.sock.settimeout(timeout)
        self.buffer_size = max_receive_length
        self.send_attempts = send_attempts
        self.send_queue_full = False

    def set_timeout(self,
                    timeout):
        """

        :param timeout:
        :return:
        """
        try:
            self.sock.settimeout(timeout)
        except ValueError as err:
            raise ValueError(err)

    def send_msg(self,
                 message,
                 expect_ack=True):
        """
        Converts message to json string then sends over the socket.
        :return:
        """
        try:
            json_message = dict_to_jsonbytes(message)
            for attempts in range(self.send_attempts):
                bytes_sent = self.sock.sendto(json_message,
                                              self.address)
                self.send_queue_full = False
                if bytes_sent == len(json_message):
                    if expect_ack:
                        if self.receive_ack():
                            return True
                        else:
                            clean_socket(self.sock)
                    else:
                        return True
            return False    # Send/receive attempts not successful
        except TypeError as err:
            raise WJESocketException("TypeError raised")
        except ConnectionRefusedError as err:
            if not self.send_queue_full:
                self.send_queue_full = True
                raise WJESocketException("Connection refused on port " + str(self.address[1]))

    def receive_ack(self):
        """
        Note, if socket is non-blocking, the immediate return may miss the ack message
        :return:
        """
        try:
            recv_msg_bytes, _ = self.sock.recvfrom(self.buffer_size)
        except BlockingIOError as err:
            return False    # TODO, anything else if returned immediately with nothing?
        except timeout:
            return False    # TODO, anything else to do if timed out?
        else:
            recv_msg = jsonbytes_to_dict(recv_msg_bytes)
            if recv_msg is self.ack_msg:        # TODO, may need better implementation
                return True


class CPPClient(object):
    def __init__(self,
                 host=None,
                 port=None,
                 timeout=0.1,
                 socket_family=AF_INET,
                 socket_type=SOCK_DGRAM,
                 max_receive_length=MAX_UDP_PACKET_SIZE,
                 is_server=False):
        """Class initializer
        :param
        """
        self.host = host
        self.port = port
        self.max_length = max_receive_length
        self.cpp_socket = socket(socket_family,
                                 socket_type)
        self.timeout = timeout
        self.socket_settimeout(self.timeout)
        self.is_server = is_server
        self.sender_host = None
        self.sender_port = None

    def socket_bind(self):
        """
        Bind to the socket. This is not needed if the socket will be bound by another
        :return:
        """
        address = (self.host, self.port)
        try:
            self.cpp_socket.bind(address)
            self.is_server = True
        except Exception as e:
            pass

    def socket_send(self, msg_bytes):
        """
        :param msg_bytes: byte-like - the message to be sent
        """
        try:
            # json_dump = json.dumps(message)
            self.cpp_socket.sendto(msg_bytes, (self.host, self.port))
        except Exception as err:
            pass

    def socket_receive(self):
        """
        :return message: The message received over the socket
        """
        try:
            msg, (remote_host, remote_port) = self.cpp_socket.recvfrom(self.max_length)  # TODO, get own socket address

        except Exception as err:
            # self.debug_log.error("Error of type: " + str(err) + " in socket_receive. Server may be absent.")
            return []

    def socket_settimeout(self, timeout):
        """
        Set the socket to the specified timeout.
        Has the dual purpose of removing from blocking more.
        :return:
        """
        try:
            self.cpp_socket.settimeout(timeout)
        except Exception:
            pass

    def socket_clean(self):
        """
        Function used to clean out the receive side of the socket before sending.
        Timeout is set to zero, so that if the socket is empty, there is no wait.
        The cpp_socket.recv will raise an excep if empty, so do nothing in that case.
        :return:
        """
        self.socket_settimeout(0.0)  # Set immediate timeout
        try:
            while self.cpp_socket.recv(self.max_length):
                pass
        except Exception:
            pass
        self.socket_settimeout(self.timeout)  # Reset socket timeout time


class JsonUsgsClient(CPPClient):
    def __init__(self,
                 heartbeat_message,
                 ack_message,
                 host=None,
                 port=None,
                 timeout=0.050,
                 ack_attempts=10):
        self.heartbeat_message = heartbeat_message
        self.ack_message = ack_message
        self.ack_attempts = ack_attempts
        CPPClient.__init__(self,
                           host=host,
                           port=port,
                           timeout=timeout)

    def send_msg_noack(self,
                       message_dict):
        """
        Send a message a expect nothing in return
        :param message_dict:
        :param heartbeat_message: string
        """
        self.socket_clean()
        self.socket_send(dict_to_jsonbytes(message_dict))

    def send_ack_msg(self, message_dict, ack_dict):
        """
        Send a message and expect an ack(nowledgement)
        :param ack_message: string
        :param message: string
        """
        ack_received = False
        attempt_counter = 1
        msg_bytes = dict_to_jsonbytes(message_dict)
        while not ack_received and attempt_counter <= self.ack_attempts:
            self.socket_clean()
            self.socket_send(msg_bytes)
            attempt_counter += 1
            if self.receive_ack(ack_dict):
                ack_received = True
        if not ack_received:
            pass

    def receive_ack(self, ack_dict):
        """
        Receive an acknowledgement on a message
        :param ack_string: str - the expected acknowledgement message
        :return: bool - if/not ack was received
        """
        try:
            received_message = self.socket_receive()
            # self.debug_log.debug("Socket message received: {}".format(received_message))
            # uncomment this line if detailed analysis of received_message is needed
            # j_dict = json.loads(received_message.decode("ascii"))
            if received_message == dict_to_jsonbytes(ack_dict):
                return True
            else:
                return False
        except Exception as err:
            return False

