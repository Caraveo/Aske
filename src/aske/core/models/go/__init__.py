"""Go framework models"""
from .base import GoModel  # Import from base.py
from .gin import GinModel  # Default framework

# Export GinModel as GoBaseModel since it's our default
GoBaseModel = GinModel

__all__ = [
    'GoModel',  # Pure Go model
    'GinModel'  # Default framework model
] 