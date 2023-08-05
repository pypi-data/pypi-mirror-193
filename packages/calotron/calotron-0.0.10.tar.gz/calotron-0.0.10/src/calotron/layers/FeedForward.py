import tensorflow as tf


class FeedForward(tf.keras.layers.Layer):
    def __init__(
        self,
        output_units,
        hidden_units,
        dropout_rate=0.1,
        residual_smoothing=True,
        name=None,
        dtype=None,
    ) -> None:
        super().__init__(name=name, dtype=dtype)
        assert output_units >= 1
        self._output_units = int(output_units)
        assert hidden_units >= 1
        self._hidden_units = int(hidden_units)
        assert dropout_rate >= 0.0
        self._dropout_rate = float(dropout_rate)
        assert isinstance(residual_smoothing, bool)
        self._residual_smoothing = residual_smoothing

        if self._residual_smoothing:
            self._emb_layer = tf.keras.layers.Dense(
                self._output_units, dtype=self.dtype
            )
        else:
            self._emb_layer = None

        self._seq = tf.keras.Sequential(
            [
                tf.keras.layers.Dense(
                    self._hidden_units, activation="relu", dtype=self.dtype
                ),
                tf.keras.layers.Dropout(self._dropout_rate, dtype=self.dtype),
                tf.keras.layers.Dense(self._output_units, dtype=self.dtype),
            ]
        )

        self._add = tf.keras.layers.Add()
        self._layer_norm = tf.keras.layers.LayerNormalization(dtype=self.dtype)

    def call(self, x) -> tf.Tensor:
        if self._emb_layer is not None:
            x = self._emb_layer(x)
        x = self._add([x, self._seq(x)])
        x = self._layer_norm(x)
        return x  # (batch_size, x_elements, output_units)

    @property
    def output_units(self) -> int:
        return self._output_units

    @property
    def hidden_units(self) -> int:
        return self._hidden_units

    @property
    def dropout_rate(self) -> float:
        return self._dropout_rate

    @property
    def residual_smoothing(self) -> bool:
        return self._residual_smoothing
