import pathlib
from typing import Optional

from neuro_cli.click_types import CLUSTER, ORG
from neuro_cli.formatters.secrets import (
    BaseSecretsFormatter,
    SecretsFormatter,
    SimpleSecretsFormatter,
)
from neuro_cli.formatters.utils import URIFormatter, uri_formatter

from .root import Root
from .utils import argument, command, group, option, parse_org_name


@group()
def secret() -> None:
    """
    Operations with secrets.
    """


@command()
@option(
    "--cluster",
    type=CLUSTER,
    help="Look on a specified cluster (the current cluster by default).",
)
@option("--full-uri", is_flag=True, help="Output full disk URI.")
async def ls(root: Root, full_uri: bool, cluster: Optional[str]) -> None:
    """
    List secrets.
    """
    if root.quiet:
        secrets_fmtr: BaseSecretsFormatter = SimpleSecretsFormatter()
    else:
        if full_uri:
            uri_fmtr: URIFormatter = str
        else:
            uri_fmtr = uri_formatter(
                username=root.client.username,
                cluster_name=cluster or root.client.cluster_name,
                org_name=root.client.config.org_name,
            )
        secrets_fmtr = SecretsFormatter(
            uri_fmtr,
        )

    secrets = []
    with root.status("Fetching secrets") as status:
        async with root.client.secrets.list(cluster_name=cluster) as it:
            async for secret in it:
                secrets.append(secret)
                status.update(f"Fetching secrets ({len(secrets)} loaded)")

    with root.pager():
        root.print(secrets_fmtr(secrets))


@command()
@option(
    "--cluster",
    type=CLUSTER,
    help="Perform on a specified cluster (the current cluster by default).",
)
@option(
    "--org",
    type=ORG,
    help="Look on a specified org (the current org by default).",
)
@argument("key")
@argument("value")
async def add(
    root: Root, key: str, value: str, cluster: Optional[str], org: Optional[str]
) -> None:
    """
    Add secret KEY with data VALUE.

    If VALUE starts with @ it points to a file with secrets content.

    Examples:

      neuro secret add KEY_NAME VALUE
      neuro secret add KEY_NAME @path/to/file.txt
    """
    org_name = parse_org_name(org, root)
    await root.client.secrets.add(
        key, read_data(value), cluster_name=cluster, org_name=org_name
    )


@command()
@option(
    "--cluster",
    type=CLUSTER,
    help="Perform on a specified cluster (the current cluster by default).",
)
@option(
    "--org",
    type=ORG,
    help="Look on a specified org (the current org by default).",
)
@argument("key")
async def rm(root: Root, key: str, cluster: Optional[str], org: Optional[str]) -> None:
    """
    Remove secret KEY.
    """

    org_name = parse_org_name(org, root)
    await root.client.secrets.rm(key, cluster_name=cluster, org_name=org_name)
    if root.verbosity > 0:
        root.print(f"Secret with key '{key}' was successfully removed")


secret.add_command(ls)
secret.add_command(add)
secret.add_command(rm)


def read_data(value: str) -> bytes:
    if value.startswith("@"):
        # Read from file
        data = pathlib.Path(value[1:]).expanduser().read_bytes()
    else:
        data = value.encode("utf-8")
    return data
