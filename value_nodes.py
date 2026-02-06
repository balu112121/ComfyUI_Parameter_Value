import torch

class ValueNumberNode:
    """
    值数节点
    可以自定义输入两个值，3位小数，范围0.01-10000，默认值1
    输出两个值，可连接值数切换节点的value1、value2
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value1": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.01,
                    "max": 10000.0,
                    "step": 0.001,
                    "display": "number",
                    "round": 0.001
                }),
                "value2": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.01,
                    "max": 10000.0,
                    "step": 0.001,
                    "display": "number",
                    "round": 0.001
                }),
            }
        }
    
    RETURN_TYPES = ("FLOAT", "FLOAT")
    RETURN_NAMES = ("value1", "value2")
    FUNCTION = "process_values"
    CATEGORY = "南光AIGC/参数数值"
    
    def process_values(self, value1: float, value2: float):
        # 确保值在有效范围内
        value1 = max(0.01, min(10000.0, value1))
        value2 = max(0.01, min(10000.0, value2))
        
        return (float(value1), float(value2))

class ValueSwitchNode:
    """
    值数切换节点
    输入端：值数1、值数2
    输出端：切换值
    默认值：1，范围1-10000
    可连接K采样器的步数、cfg、降噪等节点
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "switch_index": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 10000,
                    "step": 1,
                    "display": "number"
                }),
            },
            "optional": {
                "value1": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.01,
                    "max": 10000.0,
                    "step": 0.001,
                    "display": "number",
                    "round": 0.001
                }),
                "value2": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.01,
                    "max": 10000.0,
                    "step": 0.001,
                    "display": "number",
                    "round": 0.001
                }),
            }
        }
    
    RETURN_TYPES = ("FLOAT", "INT")
    RETURN_NAMES = ("切换值", "切换索引")
    FUNCTION = "switch_values"
    CATEGORY = "南光AIGC/参数数值"
    
    def switch_values(self, switch_index: int, value1: float = 1.0, value2: float = 1.0):
        # 确保switch_index在有效范围内
        switch_index = max(1, min(10000, switch_index))
        
        # 根据switch_index选择值（1使用value1，其他使用value2）
        if switch_index == 1:
            selected_value = value1
        else:
            selected_value = value2
        
        # 确保值在有效范围内
        selected_value = max(0.01, min(10000.0, selected_value))
        
        return (float(selected_value), int(switch_index))