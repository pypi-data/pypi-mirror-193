import radiens.api.api_allego as api
from radiens.utils.constants import (CORE_ADDR, PCACHE_ADDR, NEURONS1_ADDR,
                                     PRIMARY_CACHE_STREAM_GROUP_ID)


class AllegoClient:
    """
    A python API for allego

    Attributes:
        samp_freq (float): current sampling rate
    """

    def __init__(self):
        """
        """

        self.samp_freq = None

    def restart(self, mode: str):
        """
        Restarts Allego in the requested mode.  Valid modes: 'sbpro', '='sbpro-sinaps-256', 'sbpro-sinaps-1024'
        'sbclassic', 'sim-sine', 'sim-spikes', 'open-ephys_usb2','open-ephys_usb3', 'intan1024', 'intan512',
        'xdaq-one-rec', 'xdaq-one-stim', 'xdaq-core-rec', 'xdaq-core-stim'

        Returns:
            None

        Side Effect:
            Resets all settings to their initialization values in the requested mode.

        Example:
            >>> client.restart('sim-spikes')
            None
        """
        return api.restart(CORE_ADDR, mode)

    def workspace_save(self, workspace_id=None, tags='', notes=''):
        """
        Saves current workspace

        Parameters:
            workspace_id (str): optional workspace ID
            tags (str): optional tags
            notes (str): optional notes

        Returns:
            None

        Example:
            >>> client.workspace_save(workspace_id='my_wspace', tags='my_tags', notes='my_notes)
            None
        """
        if workspace_id is None:
            return api.workspace_save(CORE_ADDR, True, tags, notes)
        else:
            return api.workspace_save_as(CORE_ADDR, workspace_id, True, tags, notes)

    def workspace_switch(self, workspace_id: str):
        """
        Switches to requested workspace

        Parameters:
            workspace_id (str): workspace ID

        Returns:
            None

        Example:
            >>> client.workspace_switch('my_wspace')
            None
        """
        return api.workspace_switch(CORE_ADDR, workspace_id)

    def workspace_delete(self, workspace_id: str):
        """
        Deletes requested workspace 

        Parameters:
            workspace_id (str): workspace ID

        Returns:
            None

        Example:
            >>> client.workspace_delete('my_wspace')
            None
        """
        return api.workspace_delete(CORE_ADDR, workspace_id)

    def workspace_current(self):
        """
        Returns current workspace ID

        Returns:
            workspaces (pandas.DataFrame)

        Example:
            >>> client.workspace_current()
            df
        """
        return api.workspace_current(CORE_ADDR)

    def workspace_list(self):
        """
        Returns table of all available workspaces

        Returns:
            workspaces (pandas.DataFrame)

        Example:
            >>> client.workspace_list()
            df
        """
        return api.workspace_list(CORE_ADDR)

    # ======= getters =======

    def get_connected_ports(self):
        """
        Gets dictionary of connected ports.

        Returns:
            ports (dict): dictionary with key=port label, value=number of channels.

        Example: 
            >>> client.get_connected_ports()
            {'A': 32, 'B': 256}

        See also:
            client.get_signal_group()

        """
        return api.get_ports(CORE_ADDR)

    def get_available_sensors(self):
        """
        Gets dictionary of dictionaries of available Radiens headstage and probe models, with each model of form key=component ID, value=number of channels. 

        Returns:
            sensors (dict): has keys 'headstages' and 'probes' that map to dictionaries of the available headstage models and probe models, respectively.  

        Example: 
            >>> client.get_available_sensors()
            {'sensors': {'headstages': {'hstg__chronic_smartlink_HC16': 16, 'hstg__acute_smartlink_A64': 64, ...}, 
                        'probes': {'a2x16_10mm50_500_177': 32, 'a1x16_5mm150_177': 16, ...}}
        """
        return api.get_sensors(CORE_ADDR)

    def get_status(self):
        """
        Gets the status of Allego.

        Returns:
            status (dict): has keys 'streaming' and 'recording' that map to dictionaries describing their respective status

        Example: 
            >>> client.get_status()
            {'recording': {'active_filename': 'allego_0__uid1020-00-53-02',
                        'duration': 0.0,
                        'error': '',
                        'mode': 'off'},
            'streaming': {'hardware_memory': 0.0, 'mode': 'off', 'time_range': [0.0, 0.0]}}
        """
        return api.get_status(CORE_ADDR)

    def get_config(self):
        """
        Gets the configuration of Allego.

        Returns:
            config (dict): has various keys relating to the system configuration

        Side Effect:
            sets ``samp_freq`` attribute to the current system sampling rate.

        Example:
            >>> client.get_config()
            {'backbone_mode': 'SMARTBOX_SIM_GEN_SPIKES',
            'base_samp_freq': 20000.0,
            'headstage_cable_lens': {'A': 3.0,
                                    'B': 3.0,
                                    'C': 3.0,
                                    'D': 3.0,
                                    'E': 3.0,
                                    'F': 3.0,
                                    'G': 3.0,
                                    'H': 3.0},
            'stream_loop_dur_ms': 200,
            'system_server_port': ':50051', 
            'base_filename': 'my_filename',
            'filepath': 'my_filepath' }

        """
        config = api.get_config(CORE_ADDR)
        self.samp_freq = config['base_samp_freq']

        return config

    def get_signal_group(self):
        """
        Gets the signal group (channel metadata) for all connected ports.

        Returns:
            signal_group (SignalGroup): object containing metadata information for all channels. See :ref:`SignalGroup <signal group>`

        Notes:
            All ports are scanned to detect the connected ports. 

        """
        return api.get_signal_group(CORE_ADDR, PRIMARY_CACHE_STREAM_GROUP_ID)

    def get_signals(self):
        """
        Gets the the most recent signals since last call of itself or :py:meth:`set_time_to_cache_head`.

        Returns:
            sigarray (ndarray[numpy.float32]): raw signal data; the mapping contained in signal_group (see :py:meth:`get_signal_group`)
            time_range (list[float]): time range (in seconds) of sigarray
        """
        if self.samp_freq is None:
            self.samp_freq = api.get_config(CORE_ADDR)['base_samp_freq']

        return api.get_signals(PCACHE_ADDR, PRIMARY_CACHE_STREAM_GROUP_ID, self.samp_freq)

    def get_digital_out_states(self):
        """
        Gets digital out state.

        Returns:
            dout_state_dict (dict): has keys 'digital_outs_mode' and 'states'.

        Example:
            >>> client.get_digital_out_states()
            {'digital_outs_mode': 'manual',
            'states': [{'chan_idx': 0, 'state': True}, {'chan_idx': 1, 'state': False}]}
        """
        return api.get_digital_out_states(CORE_ADDR)

    # ======= setters =======

    def set_samp_freq(self, fs: int):
        """
        Sets sampling frequency.  Valid sampling frequencies: 625, 1000, 1250, 1500, 2000, 2500, 3000, 3333,
                4000, 5000, 6250, 8000, 10000, 12500, 15000, 20000, 25000, 30000

        Parameters: 
            fs (int): requested sampling frequency (samples/sec)

        Returns:
            None

        Example:
        >>> client.set_samp_freq(12500)
            None

        """
        return api.set_fs(CORE_ADDR, fs)

    def set_sensor(self, port: str, headstage_id: str, probe_id: str):
        """
        Sets a sensor (headstage paired with probe) to the requested port.

        Parameters: 
            port (str): requested port (must be a currently connected port)
            headstage_id (str): requested headstage alias or headstage ID
            probe_id (str): requested probe alias or probe ID

        Returns:
            None

        Example:
        >>> client.set_sensor('A', 'smart-32', '4x8-32')
            None

        Notes:
            use radiens.utils.HEADSTAGE_ALIAS and radiens.utils.PROBE_ALIAS to get headstage and probe aliases, respectively. 

        See also:
            client.get_available_sensors()
            client.get_connected_ports()

        """
        return api.set_sensor(CORE_ADDR, port, headstage_id, probe_id)

    def set_time_to_cache_head(self):
        """
        Sets current time to most recent time point in signal cache.

        This should be called before the first call of :py:meth:`get_signals`. The first call of :py:meth:`get_signals` 
        will return the new signals since the last call to :py:meth:`set_time_to_cache_head` 
        """
        return api.set_time_to_cache_head(PCACHE_ADDR, PRIMARY_CACHE_STREAM_GROUP_ID)

    def set_streaming(self, mode: str):
        """
        Sets signal streaming to 'on' or 'off' 

        Parameters: 
            mode (str): requested mode, ``on`` or ``off``

        Returns:
            None

        Example:
            >>> client.set_streaming('on')
            None

            >>> client.set_streaming('off')
            None

        """
        if mode in ['on']:
            api.set_stream_state(CORE_ADDR, 1)
        elif mode in ['off']:
            api.set_stream_state(CORE_ADDR, 0)
        else:
            raise ValueError("mode must be in ['on', 'off', 1, 0, True, False]")

    def set_recording(self, mode: str):
        """
        Sets signal recording to 'on' or 'off' 

        Parameters: 
            mode (str): requested mode, ``on`` or ``off``

        Returns:
            None

        Side Effect:
            sets streaming on if `mode=``on`` and streaming is off

        Example:
            >>> client.set_recording('on')
            None

            >>> client.set_recording('off')
            None

        """
        if mode in ['on']:
            api.set_record_state(CORE_ADDR, 1)
        elif mode in ['off']:
            api.set_record_state(CORE_ADDR, 0)
        else:
            raise ValueError("mode must be in ['on', 'off', 1, 0, True, False]")

    def set_recording_config(self, datasource_path, datasource_name, datasource_idx, is_time_stamp=True):
        """
        Sets recording configuration

        Parameters: 
            datasource_path (str): path to output XDAT file set
            datasource_name (str): base name of XDAT file set
            datasource_idx (int): index number of output XDAT file set
            is_time_stamp (bool): `True` if file name includes time stamp

        Returns:
            None

        Side Effect:
            sets streaming on if `mode=``on`` and streaming is off

        Example:
            >>> client.set_recording('on')
            None

            >>> client.set_recording('off')
            None
        """
        if is_time_stamp in [None, True]:
            is_time_stamp = True
        elif is_time_stamp in [False]:
            is_time_stamp = False
        api.set_recording_config(CORE_ADDR, datasource_name, datasource_path, datasource_idx, is_time_stamp)

    def set_digital_out_manual(self, dout1_state: bool, dout2_state: bool):
        """
        Sets digital out state.

        Parameters:
            dout1_state (bool): new dout 1 state
            dout2_state (bool): new dout 2 state

        Returns:
            None

        Example:
            >>> client.set_digital_out_manual(true, false)
            None

        """
        return api.set_digital_out_manual(CORE_ADDR, dout1_state, dout2_state)

# ======= spike sorter =======

    def sorter_cmd(self, cmd: str):
        """
        Sends the requested command to the spike sorter.

        Available spike sorter commands: 'on', 'off', 'clear', 'rebase', 'init', 'localize', 'sort'

        Parameters:
            cmd (str): spike sorter command

        Returns:
            None

        Example:
            >>> client.sorter_cmd('on')
            None

        """
        return api.sorter_cmd(NEURONS1_ADDR, cmd)

    def sorter_get_params(self):
        """
        Returns the spike sorter parameters

        Returns:
            pandas.DataFrame

        Example:
            >>> client.sorter_get_params()
            None

        """
        return api.sorter_get_params(NEURONS1_ADDR)

    def sorter_get_state(self):
        """
        Returns the spike sorter state

        Returns:
            pandas.DataFrame

        Example:
            >>> client.sorter_get_state()
            None

        """
        return api.sorter_get_state(NEURONS1_ADDR)

    def sorter_get_dashboard(self):
        """
        Returns the spike sorter dashboard

        Returns:
            pandas.DataFrame

        Example:
            >>> client.sorter_get_dashboard()
            None

        """
        return api.sorter_get_dashboard(NEURONS1_ADDR)
