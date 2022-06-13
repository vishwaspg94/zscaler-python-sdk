
import logging
from .Defaults import *


class Datacenters(object):

    
	def get_all_vips(self):

		uri = self.api_url + 'api/v1/vips?pageSize=1000&include=all'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res
        
        
	def get_all_public_vips(self):

		uri = self.api_url + 'api/v1/vips?pageSize=1000&include=public'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res
        
        
	def get_all_private_vips(self):

		uri = self.api_url + 'api/v1/vips?pageSize=1000&include=private'

		res = self._perform_get_request(
			uri,
			self._set_header(self.jsessionid)
		)
		return res  
