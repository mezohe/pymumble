# -*- coding: utf-8 -*-

import platform
import sys

PYMUMBLE_VERSION = "0.2.0"

#============================================================================
# Tunable parameters
#============================================================================
PYMUMBLE_CONNECTION_RETRY_INTERVAL = 10 # in sec
PYMUMBLE_AUDIO_PER_PACKET = float(20)/1000 # size of one audio packet in sec
PYMUMBLE_BANDWIDTH = 50 * 1000 # total outgoing bitrate in bit/seconds
PYMUMBLE_LOOP_RATE = 0.01 # pause done between two iteration of the main loop of the mumble thread, in sec
                          # should be small enough to manage the audio output, so smaller than PYMUMBLE_AUDIO_PER_PACKET

#============================================================================
# Constants
#============================================================================
PYMUMBLE_PROTOCOL_VERSION = (1, 2, 4)
PYMUMBLE_VERSION_STRING = "PyMumble %s" % (PYMUMBLE_VERSION)
PYMUMBLE_OS_STRING = "PyMumble %s" % (PYMUMBLE_VERSION)
PYMUMBLE_OS_VERSION_STRING = "Python %s - %s %s" % (sys.version, platform.system(), platform.release())

PYMUMBLE_PING_DELAY = 10 # interval betwen 2 pings in sec

PYMUMBLE_SAMPLERATE = 48000 # in hz

PYMUMBLE_SEQUENCE_DURATION = float(10)/1000 #in sec
PYMUMBLE_SEQUENCE_RESET_INTERVAL = 5 #in sec
PYMUMBLE_READ_BUFFER_SIZE = 4096 # how much bytes to read at a time from the control socket, in bytes

# client connection state
PYMUMBLE_CONN_STATE_NOT_CONNECTED = 0
PYMUMBLE_CONN_STATE_AUTHENTICATING = 1
PYMUMBLE_CONN_STATE_CONNECTED = 2
        
# Mumble control messages types
PYMUMBLE_MSG_TYPES_VERSION = 0
PYMUMBLE_MSG_TYPES_UDPTUNNEL = 1
PYMUMBLE_MSG_TYPES_AUTHENTICATE = 2
PYMUMBLE_MSG_TYPES_PING = 3
PYMUMBLE_MSG_TYPES_REJECT = 4
PYMUMBLE_MSG_TYPES_SERVERSYNC = 5
PYMUMBLE_MSG_TYPES_CHANNELREMOVE = 6
PYMUMBLE_MSG_TYPES_CHANNELSTATE = 7
PYMUMBLE_MSG_TYPES_USERREMOVE = 8
PYMUMBLE_MSG_TYPES_USERSTATE = 9
PYMUMBLE_MSG_TYPES_BANLIST = 10
PYMUMBLE_MSG_TYPES_TEXTMESSAGE = 11
PYMUMBLE_MSG_TYPES_PERMISSIONDENIED = 12
PYMUMBLE_MSG_TYPES_ACL = 13
PYMUMBLE_MSG_TYPES_QUERYUSERS = 14
PYMUMBLE_MSG_TYPES_CRYPTSETUP = 15
PYMUMBLE_MSG_TYPES_CONTEXTACTIONADD = 16
PYMUMBLE_MSG_TYPES_CONTEXTACTION = 17
PYMUMBLE_MSG_TYPES_USERLIST = 18
PYMUMBLE_MSG_TYPES_VOICETARGET = 19
PYMUMBLE_MSG_TYPES_PERMISSIONQUERY = 20
PYMUMBLE_MSG_TYPES_CODECVERSION = 21
PYMUMBLE_MSG_TYPES_USERSTATS = 22
PYMUMBLE_MSG_TYPES_REQUESTBLOB = 23
PYMUMBLE_MSG_TYPES_SERVERCONFIG = 24

# callbacks names
PYMUMBLE_CLBK_CONNECTED = "connected"
PYMUMBLE_CLBK_CHANNELCREATED = "channel_created" 
PYMUMBLE_CLBK_CHANNELUPDATED = "channel_updated"
PYMUMBLE_CLBK_CHANNELREMOVED = "channel_remove"
PYMUMBLE_CLBK_USERCREATED = "user_created"
PYMUMBLE_CLBK_USERUPDATED = "user_updated"
PYMUMBLE_CLBK_USERREMOVED = "user_remove"
PYMUMBLE_CLBK_SOUNDRECEIVED = "sound_received"
PYMUMBLE_CLBK_TEXTMESSAGERECEIVED = "text_received"
PYMUMBLE_CLBK_TEXTMESSAGERECEIVEDFULL = "text_received_full"

# audio types
PYMUMBLE_AUDIO_TYPE_CELT_ALPHA = 0
PYMUMBLE_AUDIO_TYPE_PING = 1
PYMUMBLE_AUDIO_TYPE_SPEEX = 2
PYMUMBLE_AUDIO_TYPE_CELT_BETA = 3
PYMUMBLE_AUDIO_TYPE_OPUS = 4

# command names
PYMUMBLE_CMD_MOVE = "move"
PYMUMBLE_CMD_MODUSERSTATE = "update_user"
