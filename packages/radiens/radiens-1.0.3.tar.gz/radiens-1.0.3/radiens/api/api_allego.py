import grpc
import numpy as np
import pandas as pd
import warnings
from radiens.exceptions.grpc_error import handle_grpc_error
from radiens.grpc import (allegoserver_pb2, allegoserver_pb2_grpc,
                          common_pb2, spikesorter_pb2)
from radiens.signal_group.SignalGroup import SignalGroup
from radiens.utils.config import new_server_channel
from radiens.utils.constants import (DOUT_MODE_OUT, PORT_, PRIMARY_CACHE_STREAM_GROUP_ID, PORT_ENUM,
                                     HEADSTAGE_ALIAS, PROBE_ALIAS, SYSTEM_MODE, SYSTEM_MODE_DECODE,
                                     APPS_, SPK_SORTER_, SPK_SORTER_STATE_DECODE)

CLIENT_NAME = 'Allego'

# ====== life cycle ======


def restart(addr, mode: str):
    if mode not in SYSTEM_MODE.keys():
        raise ValueError('invalid system type {}'.format(mode))

    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            stub.Restart(allegoserver_pb2.RestartRequest(mode=SYSTEM_MODE[mode]))
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)

# ====== workspace ======


def workspace_save(addr, is_force_overwrite=True, tags='', notes=''):
    annotate = common_pb2.AnnotateBundle(tags=tags, notes=notes)
    req = common_pb2.WorkspaceControlRequest(cmd=common_pb2.WSPACE_Save,
                                             annotation=annotate, isForceOverwrite=is_force_overwrite)
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            stub.WorkspaceControl(req)
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)


def workspace_save_as(addr, wspace_id: str, is_force_overwrite=True, tags='', notes=''):
    annotate = common_pb2.AnnotateBundle(tags=tags, notes=notes)
    req = common_pb2.WorkspaceControlRequest(cmd=common_pb2.WSPACE_Save,
                                             workspaceID=wspace_id,
                                             annotation=annotate, isForceOverwrite=is_force_overwrite)
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            stub.WorkspaceControl(req)
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)


def workspace_switch(addr, wspace_id: str):
    req = common_pb2.WorkspaceControlRequest(cmd=common_pb2.WSPACE_Switch,
                                             workspaceID=wspace_id)
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            stub.WorkspaceControl(req)
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)


def workspace_delete(addr, wspace_id: str):
    req = common_pb2.WorkspaceControlRequest(cmd=common_pb2.WSPACE_Delete,
                                             workspaceID=wspace_id)
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            stub.WorkspaceControl(req)
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)


def workspace_current(addr):
    req = common_pb2.GetWorkspaceRequest(cmd=common_pb2.GET_WSPACE_Current, appMask=common_pb2.Allego)
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            resp = stub.GetWorkspace(req)
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)
        d = {'ID': [], 'app': [], 'last_used': [], 'last_modified': [], 'is_modified': [], 'notes': [], 'tags': []}
        for _, v in resp.workspaceDesc.items():
            d['ID'].append(v.iD)
            d['app'].append(APPS_[v.app])
            d['last_used'].append(v.timestampLastUsed)
            d['last_modified'].append(v.timestampModified)
            d['is_modified'].append(v.isModified)
            d['tags'].append(v.annotation.tags)
            d['notes'].append(v.annotation.notes)
        return pd.DataFrame(d)


def workspace_list(addr):
    req = common_pb2.GetWorkspaceRequest(cmd=common_pb2.GET_WSPACE_List, appMask=common_pb2.Allego)
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            resp = stub.GetWorkspace(req)
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)
        d = {'ID': [], 'app': [], 'last_used': [], 'last_modified': [], 'is_modified': [], 'notes': [], 'tags': []}
        for _, v in resp.workspaceDesc.items():
            d['ID'].append(v.iD)
            d['app'].append(APPS_[v.app])
            d['last_used'].append(v.timestampLastUsed)
            d['last_modified'].append(v.timestampModified)
            d['is_modified'].append(v.isModified)
            d['tags'].append(v.annotation.tags)
            d['notes'].append(v.annotation.notes)
        return pd.DataFrame(d)

# ====== getters ======


def get_config(addr):
    cfg = {}
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            res = stub.GetConfig(common_pb2.StandardRequest())
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)
        else:
            cable_dict = {}
            for p in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
                try:
                    cable_dict[p] = eval('res.cableLengths.{}'.format(p))
                except AttributeError:
                    pass
            cfg = {'system_server_port': res.allegoCoreServerPort,
                   'base_samp_freq': res.baseSampFreq,
                   'stream_loop_dur_ms': res.streamLoopDurMs,
                   'headstage_cable_lens': cable_dict,
                   'backbone_mode': SYSTEM_MODE_DECODE[res.backboneMode]}

        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            res = stub.GetConfigRecording(common_pb2.StandardRequest())
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)
        else:
            cfg['base_filename'] = res.baseFileName
            cfg['filepath'] = res.baseFilePath

        return cfg


def get_ports(addr):
    req = common_pb2.SignalGroupIDRequest()
    req.streamGroupId = PRIMARY_CACHE_STREAM_GROUP_ID
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            res = stub.ListSensorSpecs(req)
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)
        ports = {}
        for _, v in enumerate(res.ports):
            ports[PORT_ENUM[v.port]] = v.channelCount
        return ports


def get_sensors(addr):
    req = common_pb2.SignalGroupIDRequest()
    req.streamGroupId = PRIMARY_CACHE_STREAM_GROUP_ID
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            res = stub.ListSensorSpecs(req)
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)
        hstages = {}
        for _, v in enumerate(res.headstages):
            hstages[v.name.strip('hstg__')] = v.channelCount
        probes = {}
        for _, v in enumerate(res.probes):
            probes[v.name.strip('probe__')] = v.channelCount
        return {'headstages': hstages, 'probes': probes}


def get_status(addr):
    with new_server_channel(addr) as chan:
        AllegoCoreStub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            res = AllegoCoreStub.GetStatus(common_pb2.StandardRequest())
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)
        else:
            return {'streaming': {'mode': 'on' if res.streaming.streamMode == 1 else 'off',
                                  'time_range': [res.streaming.primaryCacheTRange[0], res.streaming.primaryCacheTRange[1]],
                                  'hardware_memory': res.streaming.hardwareMemoryLevel},
                    'recording': {'mode': 'on' if res.recording.recordMode == 1 else 'off',
                                  'active_filename': res.recording.activeFileName,
                                  'duration': res.recording.duration,
                                  'error': res.recording.error}}


def get_signal_group(addr, stream_group_id=None):
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            req = common_pb2.SignalGroupIDRequest()
            req.streamGroupId = stream_group_id

            raw = stub.GetSignalGroup(req)
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)
        else:
            return SignalGroup(raw)


def get_signals(addr, stream_group_id: str, samp_freq: float):
    sigarray = []
    time_range = []
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.Pcache1Stub(chan)
        req = common_pb2.GetSignalsRequest(streamGroupId=stream_group_id)
        req.params.timeWindow = 1
        req.params.spacing = 0
        req.params.magnitude = -1
        req.params.plotWidthPoints = samp_freq
        req.params.gpioOnTop = False
        req.params.auxMagnitude = -1
        req.params.componentID = 'allego_python_client'

        try:
            raw = stub.GetSignals(req)
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)
        else:
            sigarray = np.frombuffer(raw.data, dtype=np.float32)
            sigarray = np.reshape(sigarray, (raw.shape[0], raw.shape[1]))
            time_range = [raw.timeRange[0], raw.timeRange[1]]

            return sigarray, time_range


def get_digital_out_states(addr):
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            res = stub.GetDIOReg(common_pb2.StandardRequest())
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)
        else:
            return {
                'digital_outs_mode': DOUT_MODE_OUT[res.mode],
                'states': [{'chan_idx': i.ntvChanIdx, 'state': i.manualState} for i in res.doutChanRegisters]
            }


# ======= setters ========

def set_digital_out_manual(addr, dout1_state: bool, dout2_state: bool):
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)

        req1 = allegoserver_pb2.DIOModeManualRequest()
        req1.chanIdx = 0
        req1.state = dout1_state

        req2 = allegoserver_pb2.DIOModeManualRequest()
        req2.chanIdx = 1
        req2.state = dout2_state

        try:
            stub.SetDIOManual(req1)
            stub.SetDIOManual(req2)
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)


def set_fs(addr, fs: int):
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            stub.SetConfigCore(allegoserver_pb2.SetConfigCoreRequest(sampFreq=float(fs)))
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)


def set_sensor(addr, port: str, hstage: str, probe: str):
    connected_ports = get_ports(addr)
    if port not in connected_ports.keys():
        raise ValueError('port {} is not valid or is connected'.format(port))
    pb_port = PORT_[port]

    sensors = get_sensors(addr)
    if hstage in HEADSTAGE_ALIAS.keys():
        pb_hstage = 'hstg__{}'.format(HEADSTAGE_ALIAS[hstage])
    elif hstage in sensors['headstages'].keys():
        pb_hstage = 'hstg__{}'.format(hstage)
    else:
        raise ValueError('headstage {} is not an alias nor an available headstage ID'.format(hstage))

    if probe in PROBE_ALIAS.keys():
        pb_probe = 'probe__{}'.format(PROBE_ALIAS[probe])
    elif probe in sensors['probes'].keys():
        pb_probe = 'probe__{}'.format(probe)
    else:
        raise ValueError('probe {} is not an alias nor an available probe ID'.format(hstage))

    port_num_chan = connected_ports[port]
    hstg_num_chan = sensors['headstages'][pb_hstage.strip('hstg__')]
    probe_num_chan = sensors['probes'][pb_probe.strip('probe__')]
    if port_num_chan != hstg_num_chan:
        warnings.warn('port {} number of channels={} does not match headstage number of channels={}'.format(
                      connected_ports[port], port_num_chan, hstg_num_chan))
    if hstg_num_chan != probe_num_chan:
        warnings.warn('headstage {} number of channels={} does not match probe number of channels={}'.format(
                      sensors['headstages'][pb_hstage.strip('hstg__')], hstg_num_chan, probe_num_chan))

    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            stub.SetSensor(common_pb2.SetSensorRequest(streamGroupId=PRIMARY_CACHE_STREAM_GROUP_ID,
                                                       port=pb_port, headstageId=pb_hstage, probeId=pb_probe))
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)


def set_stream_state(addr, state: int):
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            stub.SetStreamState(allegoserver_pb2.SetStreamRequest(mode=state))
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)


def set_record_state(addr, state: int):
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            stub.SetRecordState(allegoserver_pb2.SetRecordRequest(mode=state))
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)


def set_recording_config(addr, filename: str, filepath: str, index: int, time_stamp: str):
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.AllegoCoreStub(chan)
        try:
            stub.SetConfigRecording(allegoserver_pb2.ConfigRecording(baseFileName=filename,
                                                                     baseFilePath=filepath,
                                                                     datasource_idx=index,
                                                                     timeStamp=time_stamp))
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)


def set_time_to_cache_head(addr, stream_group_id=None):
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.Pcache1Stub(chan)
        req = common_pb2.SignalGroupIDRequest()
        req.streamGroupId = stream_group_id
        try:
            stub.SetTimeRangeToHead(req)
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)

# ====== spike sorter ======


def sorter_cmd(addr, cmd: str):
    if cmd not in SPK_SORTER_.keys():
        raise ValueError('invalid spike sorter command={}, valid commands are {}'.format(cmd, list(SPK_SORTER_.keys())))

    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.Neurons1Stub(chan)
        try:
            stub.SpikeSorterCommand(spikesorter_pb2.SpikeSorterCommandRequest(
                cmd=SPK_SORTER_[cmd], subCmd=spikesorter_pb2.SORTER_SUBCMD_NULL, spikeSorterID=''))
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)


def sorter_get_params(addr):
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.Neurons1Stub(chan)
        try:
            resp = stub.SpikeSorterGetParam(spikesorter_pb2.SpikeSorterStandardRequest(spikeSorterID=''))
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)
        p = {'ntv_chan_idx': [], 'chan_enabled?': [], 'thr_set?': [], 'use_sd?': [], 'thr': [], 'thr_sd': [], 'thr_wdw': [], 'peak_wdw': [],
             'shadow': [], 'weak_thr': [], 'thr_wdw_pts': [], 'peak_wdw_pts': [], 'shadow_pts': []}
        for v in resp.rec:
            p['ntv_chan_idx'].append(v.ntvChanIdx)
            p['chan_enabled?'].append(v.isEnabled)
            p['thr_set?'].append(v.isSetThr)
            p['use_sd?'].append(v.isSD)
            p['thr'].append(np.array(v.thr))
            p['thr_sd'].append(np.array(v.thrSd))
            p['thr_wdw'].append(np.around(np.array(v.thrWdw) * 1000.0, 5))
            p['peak_wdw'].append(np.around(np.array(v.peakWdw) * 1000.0, 5))
            p['shadow'].append(np.around(np.array(v.shadow) * 1000.0, 5))
            p['weak_thr'].append(np.array(v.weakThr))
            p['thr_wdw_pts'].append(v.thrWdwPts)
            p['peak_wdw_pts'].append(v.peakWdwPts)
            p['shadow_pts'].append(v.shadowPts)
        return pd.DataFrame(p)


def sorter_get_state(addr):
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.Neurons1Stub(chan)
        try:
            resp = stub.SpikeSorterGetState(spikesorter_pb2.SpikeSorterStandardRequest(spikeSorterID=''))
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)
        return {'sorter': SPK_SORTER_STATE_DECODE[resp.sys], 'msg': resp.msg,
                'time_initialize': resp.initializeTime, 'time_start': resp.sessionStartTime, 'time_stop': resp.sessionStopTime}


def sorter_get_dashboard(addr):
    with new_server_channel(addr) as chan:
        stub = allegoserver_pb2_grpc.Neurons1Stub(chan)
        try:
            resp = stub.SpikeSorterGetDashboard(spikesorter_pb2.SpikeSorterStandardRequest(spikeSorterID=''))
        except grpc.RpcError as ex:
            handle_grpc_error(ex, CLIENT_NAME)
    sum_stats = []
    sum_stats.append(pd.DataFrame({'stat': ['probe-snr', 'probe-noise', 'probe-units'],
                                   'port': ['all', 'all', 'all'],
                                   'N': [resp.siteStats.snr[11], resp.siteStats.noise[11], resp.siteStats.neuronYield[11]],
                                   'mean': [resp.siteStats.snr[0], resp.siteStats.noise[0], resp.siteStats.neuronYield[0]],
                                   'sd': [resp.siteStats.snr[1], resp.siteStats.noise[1], resp.siteStats.neuronYield[1]],
                                   'min': [resp.siteStats.snr[3], resp.siteStats.noise[3], resp.siteStats.neuronYield[3]],
                                   'max': [resp.siteStats.snr[4], resp.siteStats.noise[4], resp.siteStats.neuronYield[4]],
                                   'median': [resp.siteStats.snr[6], resp.siteStats.noise[6], resp.siteStats.neuronYield[6]],
                                   'mode': [np.NaN, np.NaN, resp.siteStats.neuronYield[2]],
                                   'mode_cnt': [np.NaN, np.NaN, resp.siteStats.neuronYield[5]],
                                   'q25': [resp.siteStats.snr[7], resp.siteStats.noise[7], resp.siteStats.neuronYield[7]],
                                   'q75': [resp.siteStats.snr[8], resp.siteStats.noise[8], resp.siteStats.neuronYield[8]],
                                   'skew': [resp.siteStats.snr[9], resp.siteStats.noise[9], resp.siteStats.neuronYield[9]],
                                   'kurtosis': [resp.siteStats.snr[10], resp.siteStats.noise[10], resp.siteStats.neuronYield[10]],
                                   }))
    for k in resp.portStats:
        v = resp.portStats[k]
        sum_stats.append(pd.DataFrame({'stat': ['port-snr', 'port-noise', 'port-units'],
                                       'port': [PORT_ENUM[k], PORT_ENUM[k], PORT_ENUM[k]],
                                       'N': [v.snr[11], v.noise[11], v.neuronYield[11]],
                                       'mean': [v.snr[0], v.noise[0], v.neuronYield[0]],
                                       'sd': [v.snr[1], v.noise[1], v.neuronYield[1]],
                                       'min': [v.snr[3], v.noise[3], v.neuronYield[3]],
                                       'max': [v.snr[4], v.noise[4], v.neuronYield[4]],
                                       'median': [v.snr[6], v.noise[6], v.neuronYield[6]],
                                       'mode': [np.NaN, np.NaN, v.neuronYield[2]],
                                       'mode_cnt': [np.NaN, np.NaN, v.neuronYield[5]],
                                       'q25': [v.snr[7], v.noise[7], v.neuronYield[7]],
                                       'q75': [v.snr[8], v.noise[8], v.neuronYield[8]],
                                       'skew': [v.snr[9], v.noise[9], v.neuronYield[9]],
                                       'kurtosis': [v.snr[10], v.noise[10], v.neuronYield[10]],
                                       }))
    df_sum_stats = pd.concat(sum_stats, axis=0)
    return {'enabled_ports': resp.enabledPorts, 'general': {'sorter': SPK_SORTER_STATE_DECODE[resp.general.state.sys],
                                                            'msg': resp.general.state.msg,
                                                            'time_range': np.array(resp.general.timeRange),
                                                            'num_sites_total': resp.general.numTotalSites,
                                                            'num_sites_enabled': resp.general.numEnabledSites,
                                                            'num_sites_active': resp.general.numActiveSites,
                                                            'num_units': resp.general.numNeurons,
                                                            'probe_yield_mean': resp.general.probeYield,
                                                            'site_yield_mean': resp.general.siteYield,
                                                            'num_spikes_processed': resp.general.numSpikesProcessed,
                                                            'num_spikes_labeled': resp.general.numSpikesLabeled,
                                                            'sort_efficiency': resp.general.sortEfficiency,
                                                            'spikes_file_path': resp.general.sinkDesc.path,
                                                            'spikes_file_base_name': resp.general.sinkDesc.baseName,
                                                            },
            'summary_stats': df_sum_stats}
