import logging,os.path
from functools import singledispatchmethod
from typing import Any
from localstack import config
from localstack.services.stores import AccountRegionBundle
from localstack.state import AssetDirectory,Encoder,StateVisitor,pickle
from moto.core import BackendDict
LOG=logging.getLogger(__name__)
class SaveSnapshotVisitor(StateVisitor):
	service:0;data_dir:0;encoder:0
	def __init__(A,service,data_dir=None,encoder=None):A.service=service;A.data_dir=data_dir or os.path.join(config.dirs.data,'api_states');A.encoder=encoder or pickle.PickleEncoder()
	@singledispatchmethod
	def visit(self,state_container):LOG.warning('cannot save state container of type %s',type(state_container))
	@visit.register(AccountRegionBundle)
	def _(self,state_container):A=state_container;B=os.path.join(self.data_dir,A.service_name,'store.state');self._encode(A,B)
	@visit.register(BackendDict)
	def _(self,state_container):A=state_container;B=os.path.join(self.data_dir,A.service_name,'backend.state');self._encode(A,B)
	@visit.register(AssetDirectory)
	def _(self,state_container):0
	def _encode(B,state_container,file):
		A=os.path.dirname(file)
		if not os.path.exists(A):os.mkdir(A)
		with open(file,'wb')as C:B.encoder.encode(state_container,C)