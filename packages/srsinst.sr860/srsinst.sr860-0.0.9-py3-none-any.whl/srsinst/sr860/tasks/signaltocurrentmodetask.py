import time
import logging

from srsgui import Task
from srsgui import BoolInput, IntegerListInput, FloatListInput, InstrumentInput, CommandInput
from srsinst.sr860 import SR860, get_sr860

from srsinst.sr860.instruments.components import Signal
from srsinst.sr860.instruments.keys import Keys


class SignalToCurrentModeTask(Task):
    """
When the task is selected, the relevant parameters are read from the unit, \
and updates the input panel display. The values in the unit will change, when the \
Apply button is pressed.

When this task runs, it sets the input mode to the current inout mode.
    """
    InstName = 'inst to change'
    InputGain = 'input gain (Ohm)'
    Sensitivity = 'sensitivity (A)'
    TimeConstant = 'time constant (s)'
    FilterSlope = 'filter slope (dB/oct)'
    SyncFilter = 'synchronous filter'
    AdvancedFilter = 'advanced filter'

    input_parameters = {
        InstName:       InstrumentInput(),
        InputGain:      CommandInput('signal.current_input_gain', Signal.current_input_gain),
        Sensitivity:    CommandInput('signal.current_sensitivity', Signal.current_sensitivity),
        TimeConstant:   CommandInput('signal.time_constant', Signal.time_constant),
        FilterSlope:    CommandInput('signal.filter_slope', Signal.filter_slope),
        SyncFilter:     CommandInput('signal.sync_filter', Signal.sync_filter),
        AdvancedFilter: CommandInput('signal.advanced_filter', Signal.advanced_filter)
    }

    def setup(self):
        self.logger = logging.getLogger(__file__)
        self.lockin = get_sr860(self, self.get_input_parameter(self.InstName))

    def test(self):
        self.lockin.signal.input_mode = Keys.Current
        self.params = self.get_all_input_parameters()
        self.logger.info(self.params)
        self.logger.info('Input mode change to the current mode')

    def cleanup(self):
        pass
