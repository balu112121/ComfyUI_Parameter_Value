import torch
from .value_nodes import *

# 节点映射
NODE_CLASS_MAPPINGS = {
    "Parameter_Value_Number": ValueNumberNode,
    "Parameter_Value_Switch": ValueSwitchNode
}

# 节点显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "Parameter_Value_Number": "值数",
    "Parameter_Value_Switch": "值数切换"
}