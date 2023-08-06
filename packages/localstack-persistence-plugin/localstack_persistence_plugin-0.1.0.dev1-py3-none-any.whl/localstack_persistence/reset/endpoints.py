from localstack.http import Request,route
from localstack.services.plugins import ServiceManager
from .reset import reset_all,reset_state
class StateResetResource:
	'\n    Internal endpoints to trigger state reset.\n    ';service_manager:0
	def __init__(A,service_manager):A.service_manager=service_manager
	@route('/_localstack/state/<service>/reset',methods=['POST'])
	def reset_service_state(self,request,service):
		if(A:=self.service_manager.get_service(service)):reset_state(A)
	@route('/_localstack/state/reset',methods=['POST'])
	def reset_all_service_states(self,request):reset_all(self.service_manager)