import tensorflow as tf
from tensorflow.keras.losses import BinaryCrossentropy as TF_BCE
from tensorflow.keras.losses import MeanSquaredError as TF_MSE

from calotron.losses.BaseLoss import BaseLoss


class CaloLoss(BaseLoss):
    def __init__(
        self,
        alpha=0.1,
        from_logits=False,
        label_smoothing=0.0,
        axis=-1,
        reduction="auto",
        name="calo_loss",
    ) -> None:
        super().__init__(name)
        self._alpha = float(alpha)
        self._mse_loss = TF_MSE(reduction=reduction)
        self._bce_loss = TF_BCE(
            from_logits=from_logits,
            label_smoothing=label_smoothing,
            axis=axis,
            reduction=reduction,
        )

    def discriminator_loss(
        self, discriminator, target_true, target_pred, sample_weight=None
    ) -> tf.Tensor:
        rnd_true = tf.random.normal(
            tf.shape(target_true), stddev=0.05, dtype=target_true.dtype
        )
        y_true = discriminator(target_true + rnd_true, training=True)
        loss_real = self._bce_loss(
            tf.ones_like(y_true), y_true, sample_weight=sample_weight
        )
        loss_real = tf.cast(loss_real, dtype=target_true.dtype)
        rnd_pred = tf.random.normal(
            tf.shape(target_pred), stddev=0.05, dtype=target_pred.dtype
        )
        y_pred = discriminator(target_pred + rnd_pred, training=True)
        loss_fake = self._bce_loss(
            tf.zeros_like(y_pred), y_pred, sample_weight=sample_weight
        )
        loss_fake = tf.cast(loss_fake, dtype=target_pred.dtype)
        return (loss_real + loss_fake) / 2.0

    def transformer_loss(
        self, discriminator, target_true, target_pred, sample_weight=None
    ) -> tf.Tensor:
        mse_loss = self._mse_loss(target_true, target_pred, sample_weight=sample_weight)
        mse_loss = tf.cast(mse_loss, dtype=target_true.dtype)
        rnd_pred = tf.random.normal(
            tf.shape(target_pred), stddev=0.05, dtype=target_pred.dtype
        )
        y_pred = discriminator(target_pred + rnd_pred, training=False)
        bce_loss = self._bce_loss(
            tf.ones_like(y_pred), y_pred, sample_weight=sample_weight
        )
        bce_loss = tf.cast(bce_loss, dtype=target_pred.dtype)
        return mse_loss + self._alpha * bce_loss
