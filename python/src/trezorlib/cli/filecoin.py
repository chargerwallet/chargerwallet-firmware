#!/usr/bin/env python3

# This file is part of the Trezor project.
#
# Copyright (C) 2012-2022 Chargerwallet and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

from typing import TYPE_CHECKING

import click

from .. import filecoin, tools
from . import with_client

if TYPE_CHECKING:
    from ..client import TrezorClient


PATH_HELP = "BIP-32 path to key, e.g. m/44'/461'/0'/0/0"


@click.group(name="filecoin")
def cli():
    """Filecoin commands."""


@cli.command()
@click.option("-n", "--address", required=True, help=PATH_HELP)
@click.option("-d", "--show-display", is_flag=True)
@click.option("-t", "--testnet", is_flag=True)
@with_client
def get_address(client: "TrezorClient", address: str, show_display: bool, testnet: bool):
    """Get filecoin address for specified path."""
    address_n = tools.parse_path(address)
    return filecoin.get_address(client, address_n, show_display, testnet)


@cli.command()
@click.option("-n", "--address", required=True, help=PATH_HELP)
@click.option("-t", "--testnet", is_flag=True)
@click.argument("message")
@with_client
def sign_raw_transaction(client: "TrezorClient", address: str, message: str, testnet: bool):
    """Sign a hex-encoded transaction ."""
    address_n = tools.parse_path(address)
    ret = filecoin.sign_tx(client, address_n, bytes.fromhex(message), testnet)
    output = {
        "signature": "0x%s" % ret.signature.hex(),
    }
    return output
