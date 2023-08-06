import logging,os,zipfile
from functools import singledispatchmethod
from typing import Any
from localstack import config
from localstack.services.stores import AccountRegionBundle
from localstack.state import AssetDirectory,Encoder,StateVisitor,pickle
from moto.core import BackendDict
LOG=logging.getLogger(__name__)
class CreatePodVisitor(StateVisitor):
	zip:0
	def __init__(A,zip_file,encoder=None):A.zip=zip_file;A.encoder=encoder or pickle.PickleEncoder()
	@singledispatchmethod
	def visit(self,state_container):LOG.warning('cannot save state container of type %s',type(state_container))
	@visit.register(AccountRegionBundle)
	def _(self,state_container):
		A=state_container;B=A.service_name
		for (C,D) in A.items():
			for (E,F) in D.items():
				G=f"api_states/{C}/{B}/{E}/store.state"
				with self.zip.open(G,'w')as H:self.encoder.encode(F,H)
	@visit.register(BackendDict)
	def _(self,state_container):
		A=state_container;B=A.service_name
		for (C,D) in A.items():
			for (E,F) in D.items():
				G=f"api_states/{C}/{B}/{E}/backend.state"
				with self.zip.open(G,'w')as H:self.encoder.encode(F,H)
	@visit.register(AssetDirectory)
	def _(self,state_container):
		A=config.dirs.data;A=A.rstrip('/')
		for (B,H,E) in os.walk(state_container.path):
			C=B.removeprefix(A).lstrip('/');self.zip.writestr(zipfile.ZipInfo.from_file(A,C),'')
			for D in E:F=os.path.join(B,D);G=os.path.join(C,D);self.zip.write(F,G)