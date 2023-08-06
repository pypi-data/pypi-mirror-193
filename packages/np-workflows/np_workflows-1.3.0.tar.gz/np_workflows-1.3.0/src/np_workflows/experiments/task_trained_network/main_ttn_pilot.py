import configparser
import copy
import dataclasses
import datetime
import enum
import functools
import pathlib
import threading
import time
from typing import ClassVar, Literal, NamedTuple, NoReturn, Optional, TypedDict

import IPython
import IPython.display
import ipywidgets as ipw
import np_config
import np_logging
import np_services
import np_session
import np_workflows
import PIL.Image
import pydantic
from pyparsing import Any
from np_services import (
    Service, Finalizable,
    ScriptCamstim, OpenEphys, Sync, VideoMVR, NewScaleCoordinateRecorder, MouseDirector,
)

from .ttn_stim_config import (
    TTNSession,
    session_main_stim_params, 
    session_mapping_params,
    session_opto_params,
    default_ttn_params as DEFAULT_STIM_PARAMS,
)

logger = np_logging.getLogger(__name__)


class TTNMixin:
    
    ttn_session: TTNSession
        
    opto_script: ClassVar[str] = 'C:/ProgramData/StimulusFiles/dev/opto_tagging_v2.py'
    "Used with `opto_params`"
    
    @property
    def recorders(self) -> tuple[Service, ...]:
        match self.ttn_session:
            case TTNSession.PRETEST | TTNSession.ECEPHYS:
                return (Sync, VideoMVR, OpenEphys)
            case TTNSession.HAB_60 | TTNSession.HAB_90 | TTNSession.HAB_120:
                return (Sync, VideoMVR)
    @property
    def stims(self) -> tuple[Service, ...]:
        return (ScriptCamstim, )   
    
    def initialize_and_test_services(self) -> None:
        """Initialize and test services."""
        
        self.configure_services()

        MouseDirector.user = self.user.id
        MouseDirector.mouse = self.mouse.id

        OpenEphys.folder = self.session.folder

        NewScaleCoordinateRecorder.log_root = self.session.npexp_path   
        
        super().initialize_and_test_services()
            
    def start_stim(self) -> None:

        # mapping and main -------------------------------------------------------------------- #
        ScriptCamstim.script = self.mapping_and_main_script
        ScriptCamstim.params = self.all_params

        logger.info('Starting mapping and main script')

        ScriptCamstim.start()

        while not ScriptCamstim.is_ready_to_start():
            time.sleep(10)

        if isinstance(ScriptCamstim, Finalizable):
            ScriptCamstim.finalize()

        logger.info('Mapping and main script complete')

        # opto --------------------------------------------------------------------------------- #
        if self.opto_params:
            ScriptCamstim.script = self.opto_script
            ScriptCamstim.params = self.opto_params
            
            logger.info('Starting opto-tagging script')
            ScriptCamstim.start()

            while not ScriptCamstim.is_ready_to_start():
                time.sleep(10)

            if isinstance(ScriptCamstim, Finalizable):
                ScriptCamstim.finalize()

            logger.info('Opto-tagging script complete')
        else:
            logger.info('Opto-tagging skipped')

    @property
    def mapping_and_main_script(self) -> str:
        "Used together with `all_params` to run mapping and main stim script."
        logger.warning(f'Using hard-coded script in notebooks directory for testing')
        # will eventually point to 'C:/ProgramData/StimulusFiles/dev/oct22_tt_stim_script.py'
        return np_config.local_to_unc(np_config.Rig().sync, pathlib.Path('oct22_tt_stim_script.py').resolve()).as_posix()
    
    @property
    def all_params(self) -> dict[Literal['main', 'mapping', 'opto'], dict[str, Any]]:
        params = copy.deepcopy(DEFAULT_STIM_PARAMS)
        params['main'] = self.main_params
        params['mapping'] = self.mapping_params
        params['opto'] = self.opto_params
        return params
    
    @property
    def main_params(self) -> dict[str, Any]:
        return session_main_stim_params(self.ttn_session)
    
    @property
    def mapping_params(self) -> dict[str, Any]:
        return session_mapping_params(self.ttn_session)
    
    @property
    def opto_params(self) -> dict[str, Any]:
        return session_opto_params(self.ttn_session, self.mouse)
             
class Hab(np_workflows.Hab, TTNMixin):
        
    def __init__(self, *args, **kwargs):
        self.services = (
            MouseDirector,
            Sync,
            VideoMVR,
            self.imager,
            ScriptCamstim,
            )
        super().__init__(*args, **kwargs)
        
class Ecephys(np_workflows.Ecephys, TTNMixin):
    
    def __init__(self, *args, **kwargs):
        self.services = (
            MouseDirector,
            Sync,
            VideoMVR,
            self.imager,
            ScriptCamstim,
            OpenEphys,
            NewScaleCoordinateRecorder,
            )
        super().__init__(*args, **kwargs)


# --------------------------------------------------------------------------------------
        
def new_experiment(
    mouse: int | str | np_session.Mouse, 
    user: str | np_session.User, 
    session: TTNSession,
    ) -> Ecephys | Hab:
    """Create a new experiment for the given mouse and user."""
    match session:
        case TTNSession.PRETEST | TTNSession.ECEPHYS:
            experiment = Ecephys(mouse, user)
        case TTNSession.HAB_60 | TTNSession.HAB_90 | TTNSession.HAB_120:
            experiment = Hab(mouse, user)
        case _: raise ValueError(f'Invalid session type: {session}')
    experiment.ttn_session = session
    logger.info('Created new experiment session: %s', experiment)
    return experiment

# --------------------------------------------------------------------------------------