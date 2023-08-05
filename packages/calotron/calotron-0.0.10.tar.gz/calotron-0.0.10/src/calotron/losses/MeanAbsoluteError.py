import tensorflow as tf
from tensorflow.keras.losses import MeanAbsoluteError as TF_MAE

from calotron.losses.BaseLoss import BaseLoss


class MeanAbsoluteError(BaseLoss):
    def __init__(self, reduction="auto", name="mae_loss") -> None:
        super().__init__(name)
        self._loss = TF_MAE(reduction=reduction)

    def discriminator_loss(
        self, discriminator, target_true, target_pred, sample_weight=None
    ) -> tf.Tensor:
        y_true = discriminator(target_true, training=True)
        y_pred = discriminator(target_pred, training=True)
        loss = self._loss(y_true, y_pred, sample_weight=sample_weight)
        loss = tf.cast(loss, dtype=target_true.dtype)
        return -loss  # error maximization

    def transformer_loss(
        self, discriminator, target_true, target_pred, sample_weight=None
    ) -> tf.Tensor:
        y_true = discriminator(target_true, training=False)
        y_pred = discriminator(target_pred, training=False)
        loss = self._loss(y_true, y_pred, sample_weight=sample_weight)
        loss = tf.cast(loss, dtype=target_true.dtype)
        return loss  # error minimization
