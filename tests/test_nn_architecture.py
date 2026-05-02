import json
from src.nn_architecture import check_architecture


def test_valid_conv_shape():
    spec = {"input_shape": [3, 64, 64], "layers": [
        {"name": "conv1", "type": "Conv2d", "out_channels": 32,
         "kernel_size": 3, "stride": 1, "padding": 1}
    ]}
    result = check_architecture(json.dumps(spec))
    assert "[32, 64, 64]" in result
    assert "✅" in result


def test_deconv_upsamples():
    spec = {"input_shape": [32, 16, 16], "layers": [
        {"name": "deconv1", "type": "ConvTranspose2d", "out_channels": 16,
         "kernel_size": 4, "stride": 2, "padding": 1}
    ]}
    result = check_architecture(json.dumps(spec))
    assert "[16, 32, 32]" in result


def test_invalid_json_returns_error():
    result = check_architecture("not valid json")
    assert "ERROR" in result


def test_dimension_collapse_warning():
    spec = {"input_shape": [3, 3, 3], "layers": [
        {"name": "bad_conv", "type": "Conv2d", "out_channels": 8,
         "kernel_size": 5, "stride": 1, "padding": 0}
    ]}
    result = check_architecture(json.dumps(spec))
    assert "WARNING" in result or "⚠️" in result
