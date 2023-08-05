import datetime
from typing import List, Optional, Union, Dict
from pydantic import BaseModel


class AutodlImageDO(BaseModel):
    name: str
    image_id: int
    image_uuid: str


class AutodlContainerUserSettingDO(BaseModel):
    region_sign: str
    gpu_name_set: List[str]
    gpu_num: int
    memory_size_from: int
    memory_size_to: int
    cpu_num_from: int
    cpu_num_to: int
    price_from: int
    price_to: int
    image_uuid: str
    cmd: str


class AutodlNodeUserSettingDO(BaseModel):
    name: str
    deployment_type: str
    replica_num: Optional[int] = None
    parallelism_num: Optional[int] = None
    container_template: AutodlContainerUserSettingDO
    

class AutodlNodeInfoDO(BaseModel):
    name: str
    uid: int
    id: int
    uuid: str
    deployment_type: str
    replica_num: int
    parallelism_num: int
    image_uuid: str
    template: AutodlContainerUserSettingDO


class AutodlContainerInfoDO(BaseModel):
    ssh_command: str
    root_password: str
    proxy_host: str
    custom_port: str


class AutodlContainerDO(BaseModel):
    uuid: str
    deployment_uuid: str
    machine_id: str
    status: str
    gpu_name: str
    gpu_num: int
    cpu_num: int
    memory_size: int
    image_uuid: str
    price: float
    info: AutodlContainerInfoDO