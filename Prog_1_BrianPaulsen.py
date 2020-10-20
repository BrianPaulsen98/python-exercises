#!/usr/bin/env python3

from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

api_key = ''

zillow_data = ZillowWrapper(api_key)

address = '3749 McCracken Lane, Arden Hills, MN'
zip_code = '55112'

deep_search_response = zillow_data.get_deep_search_results(address, zip_code)
result = GetDeepSearchResults(deep_search_response)
