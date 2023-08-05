# Copyright 2022 Sony Semiconductor Israel, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from typing import Dict

import numpy as np
import tensorflow as tf
from tensorflow.python.framework.tensor_shape import TensorShape
from model_compression_toolkit.core.common.constants import RANGE_MIN, RANGE_MAX
from model_compression_toolkit.core.common.target_platform import QuantizationMethod
from model_compression_toolkit.qat.common.constants import FQ_MIN, FQ_MAX
from model_compression_toolkit.qat.keras.quantizer.quant_utils import adjust_range_to_include_zero
from model_compression_toolkit.core.common.quantization.quantizers.quantizers_helpers import fix_range_to_include_zero
from model_compression_toolkit import quantizers_infrastructure as qi, TrainingMethod
from model_compression_toolkit.core.common import constants as C
import model_compression_toolkit.quantizers_infrastructure.keras.inferable_quantizers as iq
from model_compression_toolkit.qat.keras.quantizer.base_keras_qat_quantizer import BaseKerasQATTrainableQuantizer
from model_compression_toolkit.quantizers_infrastructure import TrainableQuantizerWeightsConfig, \
    TrainableQuantizerActivationConfig
from model_compression_toolkit.quantizers_infrastructure.common.base_inferable_quantizer import mark_quantizer


@mark_quantizer(quantization_target=qi.QuantizationTarget.Weights,
                quantization_method=[QuantizationMethod.UNIFORM],
                quantizer_type=TrainingMethod.STE)
class STEUniformWeightQuantizer(BaseKerasQATTrainableQuantizer):
    """
    Trainable constrained quantizer to quantize a layer inputs.
    """

    def __init__(self, quantization_config: TrainableQuantizerWeightsConfig):
        """
        Initialize a TrainableWeightQuantizer object with parameters to use
        for the quantization.

        Args:
            quantization_config: a trainable quantizer config class with attributes for the quantization.

        """
        super().__init__(quantization_config)
        self.max_values = quantization_config.weights_quantization_params[RANGE_MAX]
        self.min_values = quantization_config.weights_quantization_params[RANGE_MIN]
        self.num_bits = self.quantization_config.weights_n_bits
        self.per_channel = self.quantization_config.weights_per_channel_threshold
        self.channel_axis = self.quantization_config.weights_channels_axis
        self.min_max_shape = np.asarray(self.max_values).shape
        self.max = np.reshape(self.max_values, [-1]) if self.per_channel else float(self.max_values)
        self.min = np.reshape(self.min_values, [-1]) if self.per_channel else float(self.min_values)

        if self.per_channel and self.channel_axis not in [-1, len(self.min_max_shape) - 1]:
            # Tensorflow's fake_quant_with_min_max_vars_per_channel only works on last axis, so
            # need to move the quantization axis to the last axis
            self.perm_vec = list(np.arange(len(self.min_max_shape)))
            self.perm_vec[self.channel_axis] = len(self.min_max_shape) - 1
            self.perm_vec[len(self.min_max_shape) - 1] = self.channel_axis
        else:
            self.perm_vec = None

        self.quantizer_parameters = {}

    def initialize_quantization(self,
                                tensor_shape: TensorShape,
                                name: str,
                                layer: qi.KerasQuantizationWrapper) -> Dict[str, tf.Variable]:
        """
        Add min and max variables to layer.
        Args:
            tensor_shape: Tensor shape the quantizer quantize.
            name: Prefix of variables names.
            layer: Layer to add the variables to. The variables are saved
            in the layer's scope.

        Returns:
            Dictionary of new variables.
        """
        fq_min = layer.add_weight(
            name + FQ_MIN,
            shape=len(self.min) if self.per_channel else (),
            initializer=tf.keras.initializers.Constant(-1.0),
            trainable=False)
        fq_min.assign(self.min)

        fq_max = layer.add_weight(
            name + FQ_MAX,
            shape=len(self.max) if self.per_channel else (),
            initializer=tf.keras.initializers.Constant(1.0),
            trainable=False)
        fq_max.assign(self.max)

        # save the quantizer added parameters for later calculations
        self.quantizer_parameters = {FQ_MIN: fq_min, FQ_MAX: fq_max}
        return self.quantizer_parameters

    def __call__(self, inputs: tf.Tensor,
                 training: bool):
        """
        Quantize a tensor.
        Args:
            inputs: Input tensor to quantize.
            training: Whether the graph is in training mode.

        Returns:
            The quantized tensor.
        """

        _min = self.quantizer_parameters[FQ_MIN]
        _max = self.quantizer_parameters[FQ_MAX]
        _min, _max = adjust_range_to_include_zero(_min, _max, self.num_bits)

        if self.per_channel:
            if self.perm_vec:
                inputs = tf.transpose(inputs, perm=self.perm_vec)

            q_tensor = tf.quantization.fake_quant_with_min_max_vars_per_channel(inputs, _min, _max,
                                                                                num_bits=self.num_bits)
            if self.perm_vec:
                q_tensor = tf.transpose(q_tensor, perm=self.perm_vec)
        else:
            q_tensor = tf.quantization.fake_quant_with_min_max_vars(inputs, _min, _max,
                                                                    num_bits=self.num_bits)

        return q_tensor

    def convert2inferable(self) -> qi.BaseKerasInferableQuantizer:
        """
        Convert quantizer to inferable quantizer.

        Returns:
            BaseKerasInferableQuantizer object.
        """
        min_range, max_range = fix_range_to_include_zero(self.quantizer_parameters[FQ_MIN].numpy(),
                                                         self.quantizer_parameters[FQ_MAX].numpy(),
                                                         self.num_bits)
        return iq.WeightsUniformInferableQuantizer(num_bits=self.num_bits,
                                                   min_range=list(min_range.flatten()),
                                                   max_range=list(max_range.flatten()),
                                                   per_channel=self.per_channel,
                                                   channel_axis=self.channel_axis,
                                                   input_rank=len(self.min_max_shape))


@mark_quantizer(quantization_target=qi.QuantizationTarget.Activation,
                quantization_method=[QuantizationMethod.UNIFORM],
                quantizer_type=TrainingMethod.STE)
class STEUniformActivationQuantizer(BaseKerasQATTrainableQuantizer):
    """
    Trainable constrained quantizer to quantize a layer outputs.
    """

    def __init__(self, quantization_config: TrainableQuantizerActivationConfig):
        """
        Initialize a STEUniformActivationQuantizer object with parameters to use
        for the quantization.

        Args:
            quantization_config: trainable quantizer config class
        """
        super().__init__(quantization_config)

        self.num_bits = quantization_config.activation_n_bits
        self.min_range = quantization_config.activation_quantization_params[C.RANGE_MIN]
        self.max_range = quantization_config.activation_quantization_params[C.RANGE_MAX]
        self.quantizer_parameters = {}

    def initialize_quantization(self,
                                tensor_shape: TensorShape,
                                name: str,
                                layer: qi.KerasQuantizationWrapper) -> Dict[str, tf.Variable]:
        """
        Add min and max variables to layer.
        Args:
            tensor_shape: Tensor shape the quantizer quantize.
            name: Prefix of variables names.
            layer: Layer to add the variables to. The variables are saved
            in the layer's scope.

        Returns:
            Dictionary of new variables.
        """
        fq_min = layer.add_weight(
            name + FQ_MIN,
            shape=(),
            initializer=tf.keras.initializers.Constant(-1.0),
            trainable=False)
        fq_min.assign(self.min_range)

        fq_max = layer.add_weight(
            name + FQ_MAX,
            shape=(),
            initializer=tf.keras.initializers.Constant(1.0),
            trainable=False)
        fq_max.assign(self.max_range)

        # save the quantizer added parameters for later calculations
        self.quantizer_parameters = {FQ_MIN: fq_min, FQ_MAX: fq_max}
        return self.quantizer_parameters

    def __call__(self,
                 inputs: tf.Tensor,
                 training: bool):
        """
        Quantize a tensor.
        Args:
            inputs: Input tensor to quantize.
            training: Whether the graph is in training mode.

        Returns:
            The quantized tensor.
        """

        _min = self.quantizer_parameters[FQ_MIN]
        _max = self.quantizer_parameters[FQ_MAX]
        _min, _max = adjust_range_to_include_zero(_min, _max, self.num_bits)
        q_tensor = tf.quantization.fake_quant_with_min_max_vars(inputs, _min, _max,
                                                                num_bits=self.num_bits)

        return q_tensor

    def convert2inferable(self) -> qi.BaseKerasInferableQuantizer:
        """
        Convert quantizer to inferable quantizer.

        Returns:
            BaseKerasInferableQuantizer object.
        """
        min_range, max_range = fix_range_to_include_zero(self.quantizer_parameters[FQ_MIN].numpy(),
                                                         self.quantizer_parameters[FQ_MAX].numpy(),
                                                         self.num_bits)
        return iq.ActivationUniformInferableQuantizer(num_bits=self.num_bits,
                                                      # In activation quantization is per-tensor only - thus we pass
                                                      # the min/max as lists with a len of 1
                                                      min_range=[min_range],
                                                      max_range=[max_range])
