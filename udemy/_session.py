#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH 
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''

from ._compat import (
                sys,
                time,
                requests,
                HEADERS,
                LOGOUT_URL,
            )
from ._colorized import *


class Session(object):

    def __init__(self):
        self._headers = HEADERS
        self._session = requests.sessions.Session()

    def _set_auth_headers(self, access_token='', client_id=''):
        self._headers['Authorization'] = "Bearer {}".format(access_token)
        self._headers['X-Udemy-Authorization'] = "Bearer {}".format(access_token)

    def _get(self, url):
        session = self._session.get(url, headers=self._headers)
        if session.ok:
            return session
        if not session.ok:
            msg = session.json()
            sys.stdout.write(fc + sd + "[" + fr + sb + "-" + fc + sd + "] : " + fr + sb + "Udemy Says : %s %s %s ...\n" % (session.status_code, session.reason, msg.get('detail', '')))
            time.sleep(0.8)
            sys.exit(0)

    def _post(self, url, data):
        session = self._session.post(url, data, headers=self._headers)
        if session.ok:
            return session
        if not session.ok:
            msg = session.json()
            sys.stdout.write(fc + sd + "[" + fr + sb + "-" + fc + sd + "] : " + fr + sb + "Udemy Says : %s %s %s ...\n" % (session.status_code, session.reason, msg.get('detail', '')))
            time.sleep(0.8)
            sys.exit(0)

    def terminate(self):
        self._set_auth_headers()
        return
