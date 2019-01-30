#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH 
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''

from pprint import pprint
from ._session import Session
from ._compat import (
        sys,
        time,
        conn_error,
        LOGIN_URL,
        )
from ._utils import (
        parse_json,
        js_to_json,
        search_regex,
        hidden_inputs,
        unescapeHTML,
        )
from ._colorized import *

class UdemyAuth(object):

    def __init__(self, username='', password=''):
        self.username = username
        self.password = password
        self._session = Session()

    def _form_hidden_input(self, form_id):
        try:
            webpage = self._session._get(LOGIN_POPUP).text
        except conn_error as e:
            sys.stdout.write(fc + sd + "[" + fr + sb + "-" + fc + sd + "] : " + fr + sb + "Connection error : make sure your internet connection is working.\n")
            time.sleep(0.8)
            sys.exit(0)
        else:
            login_form = hidden_inputs(
                            search_regex(
                                r'(?is)<form[^>]+?id=(["\'])%s\1[^>]*>(?P<form>.+?)</form>' % form_id,
                                webpage,
                                '%s form' % form_id,
                                group='form'
                                )
                            )
            login_form.update({
                'email'     : self.username,
                'password'  : self.password,
                })
            return login_form

    def authenticate(self, access_token='', client_id=''):
        if not access_token and not client_id:
            data = {'email' : self.username, 'password' : self.password}
            auth_response = self._session._post(LOGIN_URL, data=data)
            auth_cookies, auth_response = auth_response.cookies, auth_response.json()
            
            access_token = auth_response.get('access_token', '')
            client_id = auth_cookies.get('client_id', '')
        
        if access_token:
            self._session._set_auth_headers(access_token=access_token, client_id=client_id)
            return self._session
        else:
            self._session._set_auth_headers()
            return None
