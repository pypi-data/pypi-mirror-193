"""Data types definitions."""
from dataclasses import dataclass, field
from ipaddress import (
    AddressValueError, IPv4Address, IPv4Network, NetmaskValueError)
import logging
from pathlib import Path
import re
from typing import Dict, List, Optional, Tuple, Union

from click import BadArgumentUsage, BadParameter
from dataclasses_json import config, dataclass_json
from ruamel.yaml import YAML
from ruamel.yaml.scanner import ScannerError
from validators import (
    domain as is_domain, email as is_email_address, url as is_url)

import vss_cli.const as const
from vss_cli.exceptions import ValidationError
from vss_cli.validators import validate_email

_LOGGING = logging.getLogger(__name__)


class Url(str):
    """URL data class."""

    def __new__(cls, val):
        """Create new class method."""
        if is_url(val):
            return str.__new__(cls, val)
        else:
            raise ValidationError(f'{val} is not a valid URL')


@dataclass_json
@dataclass
class ConfigFileGeneral:
    """Configuration General section class."""

    check_for_updates: bool = const.DEFAULT_CHECK_UPDATES
    check_for_messages: bool = const.DEFAULT_CHECK_MESSAGES
    default_endpoint_name: str = const.DEFAULT_ENDPOINT_NAME
    s3_server: str = const.DEFAULT_S3_SERVER
    debug: bool = const.DEFAULT_DEBUG
    output: str = const.DEFAULT_RAW_OUTPUT
    table_format: str = const.DEFAULT_TABLE_FORMAT
    timeout: int = const.DEFAULT_TIMEOUT
    verbose: bool = const.DEFAULT_VERBOSE
    columns_width: int = const.DEFAULT_COLUMNS_WIDTH
    wait_for_requests: bool = const.DEFAULT_WAIT_FOR_REQUESTS


@dataclass_json
@dataclass
class ConfigEndpoint:
    """Configuration endpoint class."""

    url: Url
    name: Optional[str] = None
    auth: Optional[str] = None
    token: Optional[str] = None
    tf_enabled: Optional[bool] = False

    def __post_init__(self):
        """Post init method."""

        def get_hostname_from_url(
            url: str, hostname_regex: str = const.DEFAULT_HOST_REGEX
        ) -> str:
            """Parse hostname from URL."""
            re_search = re.search(hostname_regex, url)
            _, _hostname = re_search.groups() if re_search else ('', '')
            _host = _hostname.split('.')[0] if _hostname.split('.') else ''
            return _host

        if not self.name:
            self.name = get_hostname_from_url(self.url)


@dataclass_json
@dataclass
class ConfigFile:
    """Configuration file data class."""

    general: ConfigFileGeneral
    endpoints: Optional[Union[List[ConfigEndpoint]]] = field(
        default_factory=lambda: []
    )

    def get_endpoint(self, ep_name_or_url: str) -> List[ConfigEndpoint]:
        """Get endpoint by name or url."""
        if self.endpoints:
            ep = list(
                filter(lambda i: ep_name_or_url == i.name, self.endpoints)
            ) or list(
                filter(lambda i: ep_name_or_url == i.url, self.endpoints)
            )
            return ep
        else:
            return []

    def update_endpoint(
        self, endpoint: ConfigEndpoint
    ) -> List[ConfigEndpoint]:
        """Update single endpoint."""
        if self.endpoints:
            for idx, val in enumerate(self.endpoints):
                if val.name == endpoint.name:
                    self.endpoints[idx] = endpoint
                    return self.endpoints
        else:
            self.endpoints = []
        # adding
        self.endpoints.append(endpoint)
        return self.endpoints

    def update_endpoints(
        self, *endpoints: List[ConfigEndpoint]
    ) -> List[ConfigEndpoint]:
        """Update multiple endpoints."""
        for endpoint in endpoints:
            self.update_endpoint(endpoint)
        return self.endpoints


class Email(str):
    """Email address."""

    def __new__(cls, val):
        """Create new."""
        if is_email_address(val):
            return str.__new__(cls, val)
        else:
            raise ValidationError(f'{val} is not a valid email address')


class IP(str):
    """Class IP address."""

    def __new__(cls, val):
        """Create new instance."""
        try:
            IPv4Address(val)
            return str.__new__(cls, val)
        except AddressValueError as e:
            raise ValidationError(
                f'{val} is not a valid IP address. Hint: {e.args[0]}'
            )


class Domain(str):
    """Domain."""

    def __new__(cls, val):
        """Create instance."""
        if is_domain(val):
            return str.__new__(cls, val)
        else:
            raise ValidationError(f'{val} is not a valid domain name')


class NetMask(str):
    """Net mask."""

    def __new__(cls, val):
        """Create instance."""
        try:
            IPv4Network('0.0.0.0/' + val)
            return str.__new__(cls, val)
        except NetmaskValueError as e:
            raise ValidationError(
                f'{val} is not a valid IP network mask. Hint: {e.args[0]}'
            )


@dataclass_json
@dataclass
class VmDisk:
    """Vm Disk spec."""

    capacity_gb: int
    backing_mode: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    backing_sharing: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    scsi: Optional[int] = field(
        default=0, metadata=config(exclude=lambda x: x is None)
    )


@dataclass_json
@dataclass
class VmScsi:
    """Vm SCSI."""

    bus: int
    sharing: str
    type: str


@dataclass_json
@dataclass
class VmMachine:
    """Vm Machine."""

    name: str
    folder: Optional[str] = None
    source: Optional[str] = None
    disks: List[VmDisk] = field(default_factory=lambda: VmDisk(capacity_gb=40))
    cpu: Optional[int] = field(default_factory=lambda: 1)
    os: Optional[str] = None
    domain: Optional[str] = None
    power_on: Optional[bool] = False
    template: Optional[bool] = False
    tpm: Optional[bool] = False
    vbs: Optional[bool] = False
    memory_gb: Optional[int] = field(default_factory=lambda: 1)
    firmware: Optional[str] = field(default_factory=lambda: 'bios')
    storage_type: Optional[str] = field(default_factory=lambda: 'hdd')
    version: Optional[str] = field(default_factory=lambda: 'vmx-19')
    source_snapshot: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )


@dataclass_json
@dataclass
class VmNetwork:
    """Vm network."""

    network: str
    network_id: Optional[str] = None
    type: Optional[str] = field(default_factory=lambda x: 'vmxnet3')

    def to_dict(self):
        """Convert to dict."""
        return {'type': self.type, 'network': self.network_id}


@dataclass_json
@dataclass
class VmNetworking:
    """Vm networking."""

    interfaces: List[VmNetwork]


@dataclass_json
@dataclass
class VmMetaAdmin:
    """VM meta admin."""

    name: Optional[str]
    email: Optional[Email]
    phone: Optional[str]


@dataclass_json
@dataclass
class VmMeta:
    """Vm meta."""

    description: str
    usage: str
    client: str
    inform: Optional[List[str]] = None
    admin: Optional[VmMetaAdmin] = None
    vss_service: Optional[str] = None
    notes: Optional[List[Dict]] = None
    vss_options: Optional[List[str]] = None


@dataclass_json
@dataclass
class VmCloudInit:
    """Vm Cloud init."""

    user_data: Union[Path]
    userdata: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    userdata_encoding: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    network_data: Optional[Path] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    networkconfig: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    networkconfig_encoding: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )

    @staticmethod
    def _load_yaml_file(path: Path, attr: str) -> Tuple[str, str]:
        """Load Yaml."""
        from pyvss.helper import compress_encode_string

        try:
            fp = Path(path)
            txt = fp.read_text()
            _ = YAML().load(txt)
            return (
                compress_encode_string(txt),
                'gzip+base64',
            )
        except FileNotFoundError:
            raise BadArgumentUsage(f'{attr} must a valid file path.')
        except ScannerError as ex:
            raise BadParameter(f'Invalid yaml provided: {str(ex)}')

    def __post_init__(self):
        """Run post initializing."""
        self.userdata, self.userdata_encoding = self._load_yaml_file(
            self.user_data, 'user_data'
        )

        if self.network_data is not None:
            (
                self.networkconfig,
                self.networkconfig_encoding,
            ) = self._load_yaml_file(self.network_data, 'network_data')


@dataclass_json
@dataclass
class VmCustomSpecIface:
    """Vm Custom Spec."""

    dhcp: Optional[bool] = False
    ip: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    gateway: Optional[List[IPv4Address]] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    mask: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )

    def __post_init__(self):
        """Run post init."""
        if not self.dhcp:
            if self.ip:
                ip = IPv4Network(self.ip, False)
                self.ip = str(self.ip).partition('/')[0]
                self.mask = str(ip.netmask)
            else:
                raise ValidationError('Either set dhcp=true or ip and gateway')
        else:
            pass


@dataclass_json
@dataclass
class VmCustomSpec:
    """Vm Custom Sepc."""

    hostname: str
    domain: Domain
    interfaces: List[VmCustomSpecIface]
    dns: Optional[List[IP]] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    time_zone: Optional[Union[str, int]] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )


@dataclass_json
@dataclass
class VmCliSpec:
    """Vm Cli spec."""

    built: str
    machine: VmMachine
    networking: VmNetworking
    metadata: VmMeta
    custom_spec: Optional[VmCustomSpec] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    cloud_init: Optional[VmCloudInit] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    extra_config: Optional[Union[List[str], List[Dict]]] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )

    @staticmethod
    def _process_extra_config(value: List[str]) -> List[Dict[str, str]]:
        """Process extra configuration."""
        from vss_cli.helper import to_tuples

        _options = to_tuples(','.join(value))
        return [{opt[0]: opt[1]} for opt in _options]

    def __post_init__(self):
        """Process and rewrite."""
        if self.extra_config is not None:
            self.extra_config = self._process_extra_config(self.extra_config)


@dataclass_json
@dataclass
class UserData:
    """User data."""

    userdata: str
    userdata_encoding: str
    networkconfig: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    networkconfig_encoding: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )


@dataclass_json
@dataclass
class VmApiSpec:
    """Vm api spec."""

    built_from: str
    usage: str
    client: str
    cpu: int
    description: str
    disks: List[VmDisk]
    domain: Optional[str]
    firmware: str
    folder: str
    inform: List[str]
    memory: int
    name: str
    networks: List[VmNetwork]
    os: str
    version: str
    storage_type: Optional[str] = 'hdd'
    tpm: Optional[bool] = False
    vbs: Optional[bool] = False
    power_on: Optional[bool] = False
    scsi: Optional[List[VmScsi]] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    vss_options: Optional[List[str]] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    vss_service: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    custom_spec: Optional[VmCustomSpec] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    extra_config: Optional[List[str]] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    user_data: Optional[UserData] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    admin_email: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    admin_name: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    admin_phone: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    notes: Optional[List[Dict]] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    source: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    source_template: Optional[str] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )
    source_snap_id: Optional[int] = field(
        default=None, metadata=config(exclude=lambda x: x is None)
    )

    @classmethod
    def from_cli_spec(cls, cli_spec: VmCliSpec, session=None):
        """Create from cli spec."""
        data = dict(built_from=cli_spec.built)
        name = cli_spec.machine.name
        # machine
        if cli_spec.built in ['clib', 'clone', 'image', 'template']:
            if cli_spec.built in ['clone', 'template']:
                source_id = session.get_vm_by_id_or_name(
                    cli_spec.machine.source
                )[0]['moref']
                data['source'] = source_id
                source_spec = session.get_vm_spec(source_id)
                del source_spec['built_from']
                if source_spec['extra_config']:
                    del source_spec['extra_config']
                data.update(source_spec)
                name = f"{source_spec['name']}-f{cli_spec.built}"
                if cli_spec.machine.firmware != source_spec['firmware']:
                    _LOGGING.warning(
                        f'{cli_spec.machine.firmware} differs from source.'
                        f'Overriding with {source_spec["firmware"]} to avoid '
                        f'issues...'
                    )
                    cli_spec.machine.firmware = source_spec['firmware']
                if cli_spec.built in ['template']:
                    data['source_template'] = source_id
                if (
                    cli_spec.built in ['clone']
                    and cli_spec.machine.source_snapshot
                ):
                    data[
                        'source_snap_id'
                    ] = session.get_vm_snapshot_by_id_name_or_desc(
                        source_id, cli_spec.machine.source_snapshot
                    )[
                        0
                    ][
                        'id'
                    ]

        if cli_spec.machine.folder:
            data['folder'] = session.get_folder_by_name_or_moref_path(
                cli_spec.machine.folder
            )[0]['moref']
        if cli_spec.networking:
            networks = []
            for iface in cli_spec.networking.interfaces:
                net_id = session.get_network_by_name_or_moref(
                    iface.network_id or iface.network
                )[0]['moref']
                networks.append({'network': net_id, 'type': iface.type})
            data['networks'] = []

        if cli_spec.machine.disks:
            data['disks'] = [disk.to_dict() for disk in cli_spec.machine.disks]
        if cli_spec.custom_spec:
            data['custom_spec'] = VmCustomSpec.from_dict(
                cli_spec.custom_spec.to_dict()
            )
        if cli_spec.machine.memory_gb:
            data['memory'] = cli_spec.machine.memory_gb
        data['name'] = cli_spec.machine.name or name
        if cli_spec.machine.cpu:
            data['cpu'] = cli_spec.machine.cpu
        if cli_spec.machine.firmware:
            data['firmware'] = session.get_vm_firmware_by_type_or_desc(
                cli_spec.machine.firmware
            )[0]['type']
        if cli_spec.machine.os:
            data['os'] = session.get_os_by_name_or_guest(cli_spec.machine.os)[
                0
            ]['guest_id']
        if cli_spec.machine.version:
            data['version'] = cli_spec.machine.version
        if cli_spec.machine.storage_type:
            data['storage_type'] = session.get_vm_storage_type_by_type_or_desc(
                cli_spec.machine.storage_type
            )[0]['type']
        if cli_spec.machine.domain:
            data['domain'] = cli_spec.machine.domain
        if cli_spec.machine.tpm:
            data['cls'] = cli_spec.machine.tpm
        if cli_spec.machine.vbs:
            data['vbs'] = cli_spec.machine.vbs
        if cli_spec.machine.power_on:
            data['power_on'] = cli_spec.machine.power_on
        # metadata
        if cli_spec.metadata.usage:
            data['usage'] = cli_spec.metadata.usage
        if cli_spec.metadata.client:
            data['client'] = cli_spec.metadata.client
        data['description'] = cli_spec.metadata.description
        if cli_spec.metadata.admin.name:
            data['admin_name'] = cli_spec.metadata.admin.name
        if cli_spec.metadata.admin.email:
            data['admin_email'] = validate_email(
                None, 'admin_email', cli_spec.metadata.admin.email
            )
        if cli_spec.metadata.admin.phone:
            data['admin_phone'] = cli_spec.metadata.admin.phone
        if cli_spec.metadata.inform:
            data['inform'] = [
                validate_email(None, 'inform', i)
                for i in cli_spec.metadata.inform
            ]
        if cli_spec.metadata.vss_service:
            data['vss_service'] = session.get_vss_service_by_name_label_or_id(
                cli_spec.metadata.vss_service
            )[0]['id']
        if cli_spec.metadata.vss_options:
            data['vss_options'] = cli_spec.metadata.vss_options
        if cli_spec.cloud_init:
            data['user_data'] = UserData.from_dict(
                cli_spec.cloud_init.to_dict()
            )
        if cli_spec.extra_config:
            data['extra_config'] = cli_spec.extra_config
        if cli_spec.metadata.notes:
            data['notes'] = cli_spec.metadata.notes
        return cls.from_dict(data)
