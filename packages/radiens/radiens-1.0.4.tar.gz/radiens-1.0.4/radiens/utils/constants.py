from pathlib import Path
from radiens.grpc import (allegoserver_pb2, allegoserver_pb2_grpc,
                          common_pb2, spikesorter_pb2)

DEFAULT_IP = 'localhost'
DEFAULT_HUB = 'default'


# ports
ALLEGO_CORE_PORT = 50051
PCACHE_PORT = 50052
KPI_PORT = 50053
NEURONS1_PORT = 50054

# default server addresses
CORE_ADDR = '{}:{}'.format(DEFAULT_IP, ALLEGO_CORE_PORT)
PCACHE_ADDR = '{}:{}'.format(DEFAULT_IP, PCACHE_PORT)
KPI_ADDR = '{}:{}'.format(DEFAULT_IP, KPI_PORT)
NEURONS1_ADDR = '{}:{}'.format(DEFAULT_IP, NEURONS1_PORT)


# services
CORE_SERVICE = 'core'
PCACHE_SERVICE = 'pcache'

# only allego stream group
PRIMARY_CACHE_STREAM_GROUP_ID = 'Live Signals'

# default datasource paths
DATASOURCE_PATHS = {
    'dsrc_path': Path(Path.home(), 'radix', 'data'),
    'dsrc_type': 'xdat',
    'dsrc_name': 'sbpro'
}

# ports/signals
PORT_ENUM = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
PORT_ = {'A': common_pb2.A,  'B': common_pb2.B, 'C': common_pb2.C,  'D': common_pb2.D,
         'E': common_pb2.E,  'F': common_pb2.F, 'G': common_pb2.G,  'H': common_pb2.H}
SIGNAL_TYPE_ENUM = {0: 'amp', 1: 'adc', 2: 'din', 3: 'dout'}
SIGNAL_TYPES = ['amp', 'adc', 'din', 'dout']

# system
SYSTEM_MODE = {
    'sbpro': allegoserver_pb2.SMARTBOX_PRO,
    'sbpro-sinaps-256': allegoserver_pb2.SMARTBOX_PRO_SINAPS_256,
    'sbpro-sinaps-1024': allegoserver_pb2.SMARTBOX_PRO_SINAPS_1024,
    'sb-classic': allegoserver_pb2.SMARTBOX_CLASSIC,
    'sim-sine': allegoserver_pb2.SMARTBOX_SIM_GEN_SINE,
    'sim-sine-mapped': allegoserver_pb2.SMARTBOX_SIM_GEN_SINE_MAPPED,
    'sim-sine-high-freq': allegoserver_pb2.SMARTBOX_SIM_GEN_SINE_HIGH_FREQ,
    'sim-sine-multi-band': allegoserver_pb2.SMARTBOX_SIM_GEN_SINE_MULTI_BAND,
    'sim-spikes': allegoserver_pb2.SMARTBOX_SIM_GEN_SPIKES,
    'open-ephys_usb2': allegoserver_pb2.OPEN_EPHYS_USB2,
    'open-ephys_usb3': allegoserver_pb2.OPEN_EPHYS_USB3,
    'intan-usb2': allegoserver_pb2.INTAN_USB2,
    'intan-1024': allegoserver_pb2.INTAN_RECORDING_CONTROLLER_1024,
    'intan-512': allegoserver_pb2.INTAN_RECORDING_CONTROLLER_512,
    'xdaq-one-rec': allegoserver_pb2.XDAQ_ONE_REC,
    'xdaq-one-stim': allegoserver_pb2.XDAQ_ONE_STIM,
    'xdaq-core-rec': allegoserver_pb2.XDAQ_CORE_REC,
    'xdaq-core-stim': allegoserver_pb2.XDAQ_CORE_STIM,
}

SYSTEM_MODE_DECODE = {
    0: 'sbox-pro',
    1: 'sim-sine',
    2: 'sim-spikes',
    4: 'open-ephys-usb3',
    5: 'intan-1024',
    6: 'sb-classic',
    7: 'intan-512',
    8: 'open-ephys-usb2',
    9: 'intan-usb2',
    10: 'sim-sine-mapped',
    11: 'sim-sine-high-freq',
    12: 'sim-sine-multi-band',
    13: 'sbpro-sinaps-256',
    14: 'sbpro-sinaps-1024',
    15: 'xdaq-one-rec',
    16: 'xdaq-one-stim',
    17: 'xdaq-core-rec',
    18: 'xdaq-core-stim',
}

DOUT_MODE_OUT = {
    0: 'manual',
    1: 'events',
    2: 'gated'
}

APPS_ = {0: 'allego', 1: 'curate', 2: 'videre'}

# stream/record
STREAM_MODE = {'S_OFF': 0, 'S_ON': 1}
RECORD_MODE = {'R_OFF': 0, 'R_ON': 1}
STREAM_MODE_OUT = {0: 'S_OFF', 1: 'S_ON'}
RECORD_MODE_OUT = {0: 'R_OFF', 1: 'R_ON'}

# sensors
HEADSTAGE_ALIAS = {'smart-16': 'acute_smartlink_A16', 'smart-32': 'chronic_smartlink_CM32',
                   'pass-32': 'passthrough_32',  'pass-64': 'passthrough_64', 'chronic-64': 'chronic_smartlink_H64'}

PROBE_ALIAS = {'v1x16-16': 'v1x16_edge_10mm200_177', '4x8-32': 'a4x8_5mm100_200_177',
               '8x1tet-32': 'a8x1_tet_7mm_200_121',  'buz-32': 'buz32', 'poly3-32': 'a1x32_poly3_8mm50s_177',
               ' poly5-32': 'a1x32_poly5_6mm35s_100',  '8x8-64': 'a8x8_5mm200_200_413', 'poly3-64': 'v1x64_poly3_10mm25s_177',
               'buz-64': 'buz64'}

# spike sorter
SPK_SORTER_ = {'on': spikesorter_pb2.SORTER_CMD_ON, 'off': spikesorter_pb2.SORTER_CMD_OFF,
               'clear': spikesorter_pb2.SORTER_CMD_CLEAR_SORT, 'rebase': spikesorter_pb2.SORTER_CMD_REBASE,
               'init': spikesorter_pb2.SORTER_CMD_INIT, 'localize': spikesorter_pb2.SORTER_CMD_LOCALIZE,
               'sort': spikesorter_pb2.SORTER_CMD_SORT}

SPK_SORTER_STATE_DECODE = {0: 'on', 1: 'off', 2: 'not_configured'}
