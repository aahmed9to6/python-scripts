#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH 
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''

from ._internal import InternUdemyCourse as Udemy


def course(url, username='', password='', cookies='', basic=True, callback=None):
    """Returns udemy course instance.

    @params:
        url      : Udemy course url required : type (string).
        username : Udemy email account required : type (string).
        password : Udemy account password required : type (string)
        cookies  : Udemy account logged in browser cookies optional : type (string)
    """
    return Udemy(url, username, password, cookies, basic, callback)