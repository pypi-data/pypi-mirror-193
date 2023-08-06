# -*- coding: utf-8 -*-
# ==============================================================================
# MIT License
#
# Copyright (c) 2019 Albert Moky
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================

"""
    Messenger for client
    ~~~~~~~~~~~~~~~~~~~~

    Transform and send message
"""

from typing import Optional

from dimples import EntityType, ID, EVERYONE
from dimples import Station
from dimples import Envelope, InstantMessage
from dimples import MetaCommand, DocumentCommand

from ..utils import QueryFrequencyChecker
from ..common import HandshakeCommand, ReportCommand, LoginCommand
from ..common import CommonMessenger

from .network import ClientSession


class ClientMessenger(CommonMessenger):

    @property
    def session(self) -> ClientSession:
        sess = super().session
        assert isinstance(sess, ClientSession), 'session error: %s' % sess
        return sess

    def handshake(self, session_key: Optional[str]):
        """ send handshake command to current station """
        session = self.session
        station = session.station
        srv_id = station.identifier
        if session_key is None:
            # first handshake
            facebook = self.facebook
            user = facebook.current_user
            assert user is not None, 'current user not found'
            env = Envelope.create(sender=user.identifier, receiver=srv_id)
            cmd = HandshakeCommand.start()
            # send first handshake command as broadcast message
            cmd.group = Station.EVERY
            # create instant message with meta & visa
            i_msg = InstantMessage.create(head=env, body=cmd)
            i_msg['meta'] = user.meta.dictionary
            i_msg['visa'] = user.visa.dictionary
            self.send_instant_message(msg=i_msg, priority=-1)
        else:
            # handshake again
            cmd = HandshakeCommand.restart(session=session_key)
            self.send_content(sender=None, receiver=srv_id, content=cmd, priority=-1)

    def handshake_success(self):
        """ callback for handshake success """
        # broadcast current documents after handshake success
        self.broadcast_document()

    def broadcast_document(self):
        """ broadcast meta & visa document to all stations """
        facebook = self.facebook
        current = facebook.current_user
        identifier = current.identifier
        meta = current.meta
        visa = current.visa
        cmd = DocumentCommand.response(identifier=identifier, meta=meta, document=visa)
        # broadcast to everyone@everywhere
        self.send_content(sender=identifier, receiver=EVERYONE, content=cmd, priority=1)

    def broadcast_login(self, sender: ID, user_agent: str):
        """ send login command to keep roaming """
        # get current station
        session = self.session
        station = session.station
        assert sender.type != EntityType.STATION, \
            'station (%s) would not login to another station: %s' % (sender, station)
        # create login command
        cmd = LoginCommand(identifier=sender)
        cmd.agent = user_agent
        cmd.station = station
        # broadcast to everyone@everywhere
        self.send_content(sender=sender, receiver=EVERYONE, content=cmd, priority=1)

    def report_online(self, sender: ID = None):
        """ send report command to keep user online """
        cmd = ReportCommand(title=ReportCommand.ONLINE)
        self.send_content(sender=sender, receiver=Station.ANY, content=cmd, priority=1)

    def report_offline(self, sender: ID = None):
        """ Send report command to let user offline """
        cmd = ReportCommand(title=ReportCommand.OFFLINE)
        self.send_content(sender=sender, receiver=Station.ANY, content=cmd, priority=1)

    # Override
    def _query_meta(self, identifier: ID) -> bool:
        checker = QueryFrequencyChecker()
        if not checker.meta_query_expired(identifier=identifier):
            # query not expired yet
            self.debug(msg='meta query not expired yet: %s' % identifier)
            return False
        self.info(msg='querying meta: %s from any station' % identifier)
        cmd = MetaCommand.query(identifier=identifier)
        self.send_content(sender=None, receiver=Station.ANY, content=cmd)
        return True

    # Override
    def _query_document(self, identifier: ID) -> bool:
        checker = QueryFrequencyChecker()
        if not checker.document_query_expired(identifier=identifier):
            # query not expired yet
            self.debug(msg='document query not expired yet: %s' % identifier)
            return False
        self.info(msg='querying document: %s from any station' % identifier)
        cmd = DocumentCommand.query(identifier=identifier)
        self.send_content(sender=None, receiver=Station.ANY, content=cmd)
        return True
