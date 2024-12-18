# This file is part of the ChargerWallet project, https://chargerwallet.com/
#
# Copyright (C) 2021 ChargerWallet Team <core@chargerwallet.com>
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.

from typing import TYPE_CHECKING

import click

from .. import lnurl
from . import with_client

if TYPE_CHECKING:
    from ..client import TrezorClient


@click.group(name="lnurl")
def cli():
    """Lnurl commands."""


@cli.command()
@click.option("-d", "--domain", required=True)
@click.option("-r", "--random-data")
@with_client
def auth(client: "TrezorClient", domain: str, random_data: str) -> str:
    """Get lnurl address in hex encoding."""
    return lnurl.auth(client, domain.encode("utf-8"), bytes.fromhex(random_data))
