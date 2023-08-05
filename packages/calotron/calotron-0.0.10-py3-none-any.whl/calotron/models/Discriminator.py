import tensorflow as tf

from calotron.layers import DeepSets


class Discriminator(tf.keras.Model):
    def __init__(
        self,
        latent_dim,
        output_units,
        output_activation=None,
        hidden_layers=3,
        hidden_units=128,
        dropout_rate=0.1,
        name=None,
        dtype=None,
    ) -> None:
        super().__init__(name=name, dtype=dtype)
        assert latent_dim >= 1
        self._latent_dim = int(latent_dim)
        assert output_units >= 1
        self._output_units = int(output_units)
        self._output_activation = output_activation
        assert hidden_layers >= 1
        self._hidden_layers = int(hidden_layers)
        assert hidden_units >= 1
        self._hidden_units = int(hidden_units)
        assert dropout_rate >= 0.0
        self._dropout_rate = float(dropout_rate)

        self._deepsets = DeepSets(
            latent_dim=self._latent_dim,
            num_layers=self._hidden_layers,
            hidden_units=self._hidden_units,
            dropout_rate=self._dropout_rate,
            dtype=self.dtype,
        )

        self._seq = [
            tf.keras.layers.Dense(
                self._latent_dim, activation="relu", dtype=self.dtype
            ),
            tf.keras.layers.Dropout(self._dropout_rate, dtype=self.dtype),
            tf.keras.layers.Dense(
                self._latent_dim, activation="relu", dtype=self.dtype
            ),
            tf.keras.layers.Dropout(self._dropout_rate, dtype=self.dtype),
        ]
        self._seq += [
            tf.keras.layers.Dense(
                self._output_units, activation=self._output_activation, dtype=self.dtype
            )
        ]

    def call(self, x) -> tf.Tensor:
        x = self._deepsets(x)
        for layer in self._seq:
            x = layer(x)
        return x

    @property
    def latent_dim(self) -> int:
        return self._latent_dim

    @property
    def output_units(self) -> int:
        return self._output_units

    @property
    def output_activation(self):  # TODO: add Union[None, activation]
        return self._output_activation

    @property
    def hidden_layers(self) -> int:
        return self._hidden_layers

    @property
    def hidden_units(self) -> int:
        return self._hidden_units

    @property
    def dropout_rate(self) -> float:
        return self._dropout_rate

    @property
    def deepsets(self) -> DeepSets:
        return self._deepsets
