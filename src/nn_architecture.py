import json
from typing import Any


def _infer_output_shape(input_shape: list[int], layer: dict[str, Any]) -> list[int]:
    """
    Compute output spatial shape for a single layer.

    Supports Conv2d, ConvTranspose2d, and shape-preserving layers.
    input_shape: [C, H, W]
    """
    layer_type = layer.get("type", "").lower()
    H, W = input_shape[1], input_shape[2]
    out_channels = layer.get("out_channels", input_shape[0])
    kernel = layer.get("kernel_size", 3)
    stride = layer.get("stride", 1)
    padding = layer.get("padding", 0)

    if layer_type in ("conv2d", "conv"):
        H_out = (H + 2 * padding - kernel) // stride + 1
        W_out = (W + 2 * padding - kernel) // stride + 1
    elif layer_type in ("convtranspose2d", "deconv"):
        H_out = (H - 1) * stride - 2 * padding + kernel
        W_out = (W - 1) * stride - 2 * padding + kernel
    elif layer_type in ("batchnorm2d", "relu", "sigmoid", "tanh", "dropout"):
        H_out, W_out = H, W
    else:
        return input_shape

    return [out_channels, H_out, W_out]


def check_architecture(layers_info: str) -> str:
    """
    Validate tensor shape flow through a sequence of PyTorch layers.

    Expected JSON input format::

        {
          "input_shape": [C, H, W],
          "layers": [
            {"name": "conv1", "type": "Conv2d", "out_channels": 64,
             "kernel_size": 3, "stride": 1, "padding": 1}
          ]
        }
    """
    try:
        spec = json.loads(layers_info)
    except json.JSONDecodeError as e:
        return f"ERROR: Invalid JSON — {e}. Provide a JSON object with 'input_shape' and 'layers'."

    if "input_shape" not in spec or "layers" not in spec:
        return "ERROR: JSON must contain 'input_shape' [C,H,W] and 'layers' (list of layer dicts)."

    current_shape = spec["input_shape"]
    if len(current_shape) != 3:
        return "ERROR: 'input_shape' must be [C, H, W] (exactly 3 values)."

    trace = [f"Input  → shape {current_shape}"]
    warnings = []

    for i, layer in enumerate(spec["layers"]):
        name = layer.get("name", f"layer_{i}")
        try:
            next_shape = _infer_output_shape(current_shape, layer)
        except Exception as e:
            return f"ERROR at layer '{name}': {e}"

        if next_shape[1] <= 0 or next_shape[2] <= 0:
            warnings.append(
                f"⚠️  Layer '{name}' ({layer.get('type')}): "
                f"Negative/zero spatial dimension {current_shape} → {next_shape}. "
                f"Check kernel_size / stride / padding."
            )

        trace.append(f"  [{name}] {layer.get('type', '?')} → shape {next_shape}")
        current_shape = next_shape

    result_lines = ["ARCHITECTURE SHAPE TRACE:"] + trace
    if warnings:
        result_lines += ["\nWARNINGS:"] + warnings
    else:
        result_lines.append("\n✅ All layer shapes are valid. No dimension collapse detected.")

    return "\n".join(result_lines)
