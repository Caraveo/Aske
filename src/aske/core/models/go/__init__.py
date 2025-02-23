"""Go framework models"""
from .gin import GinModel

# Export GinModel as GoBaseModel since it's our default
GoBaseModel = GinModel

__all__ = [
    'GoBaseModel',
    'GinModel'
] 