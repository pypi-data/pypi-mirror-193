# -*- coding: utf-8 -*-
# ==============================================================================
# MIT License
#
# Copyright (c) 2022 Albert Moky
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

from typing import Optional, List

from dimsdk import PrivateKey, DecryptKey, SignKey
from dimsdk import ID, Meta, Document

from ..common import AccountDBI

from .t_private import PrivateKeyTable
from .t_meta import MetaTable
from .t_document import DocumentTable
from .t_user import UserTable
from .t_group import GroupTable


class AccountDatabase(AccountDBI):
    """
        Database for MingKeMing
        ~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, root: str = None, public: str = None, private: str = None):
        super().__init__()
        self.__private_table = PrivateKeyTable(root=root, public=public, private=private)
        self.__meta_table = MetaTable(root=root, public=public, private=private)
        self.__doc_table = DocumentTable(root=root, public=public, private=private)
        self.__user_table = UserTable(root=root, public=public, private=private)
        self.__group_table = GroupTable(root=root, public=public, private=private)

    def show_info(self):
        self.__private_table.show_info()
        self.__meta_table.show_info()
        self.__doc_table.show_info()
        self.__user_table.show_info()
        self.__group_table.show_info()

    #
    #   PrivateKey DBI
    #

    # Override
    def save_private_key(self, key: PrivateKey, identifier: ID, key_type: str = 'M') -> bool:
        return self.__private_table.save_private_key(key=key, identifier=identifier, key_type=key_type)

    # Override
    def private_keys_for_decryption(self, identifier: ID) -> List[DecryptKey]:
        return self.__private_table.private_keys_for_decryption(identifier=identifier)

    # Override
    def private_key_for_signature(self, identifier: ID) -> Optional[SignKey]:
        return self.__private_table.private_key_for_signature(identifier=identifier)

    # Override
    def private_key_for_visa_signature(self, identifier: ID) -> Optional[SignKey]:
        return self.__private_table.private_key_for_visa_signature(identifier=identifier)

    #
    #   Meta DBI
    #

    # Override
    def save_meta(self, meta: Meta, identifier: ID) -> bool:
        # check meta with ID
        if not Meta.match_id(meta=meta, identifier=identifier):
            raise ValueError('meta not match: %s => %s' % (identifier, meta))
        return self.__meta_table.save_meta(meta=meta, identifier=identifier)

    # Override
    def meta(self, identifier: ID) -> Optional[Meta]:
        return self.__meta_table.meta(identifier=identifier)

    #
    #   Document DBI
    #

    # Override
    def save_document(self, document: Document) -> bool:
        # check with exists
        meta = self.__meta_table.meta(identifier=document.identifier)
        if meta is None:
            raise LookupError('meta not exists: %s' % document.identifier)
        if not (document.valid or document.verify(public_key=meta.key)):
            raise ValueError('document error: %s' % document.identifier)
        return self.__doc_table.save_document(document=document)

    # Override
    def document(self, identifier: ID, doc_type: str = '*') -> Optional[Document]:
        return self.__doc_table.document(identifier=identifier, doc_type=doc_type)

    #
    #   User DBI
    #

    # Override
    def local_users(self) -> List[ID]:
        return self.__user_table.local_users()

    # Override
    def save_local_users(self, users: List[ID]) -> bool:
        return self.__user_table.save_local_users(users=users)

    # Override
    def contacts(self, identifier: ID) -> List[ID]:
        return self.__user_table.contacts(identifier=identifier)

    # Override
    def save_contacts(self, contacts: List[ID], identifier: ID) -> bool:
        return self.__user_table.save_contacts(contacts=contacts, identifier=identifier)

    #
    #   Group DBI
    #

    # Override
    def founder(self, identifier: ID) -> Optional[ID]:
        return self.__group_table.founder(identifier=identifier)

    # Override
    def owner(self, identifier: ID) -> Optional[ID]:
        return self.__group_table.owner(identifier=identifier)

    # Override
    def members(self, identifier: ID) -> List[ID]:
        return self.__group_table.members(identifier=identifier)

    # Override
    def assistants(self, identifier: ID) -> List[ID]:
        return self.__group_table.assistants(identifier=identifier)

    # Override
    def save_members(self, members: List[ID], identifier: ID) -> bool:
        return self.__group_table.save_members(members=members, identifier=identifier)

    # Override
    def save_assistants(self, assistants: List[ID], identifier: ID) -> bool:
        return self.__group_table.save_assistants(assistants=assistants, identifier=identifier)
