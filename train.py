import os
import numpy
from get_dataset import get_dataset
from get_model import get_model, save_model
from tensorflow import keras
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard


epochs = 15
batch_size = 32


def train_model(model, x_dataset, x_test, y_dataset, y_test):
    """
    This will train the model.
    :param model: Which model to train
    :param x: x
    :param x_test: x_test
    :param y: y
    :param y_test: y_test
    :return: model
    """
    if not os.path.exists('Data/Checkpoints/'):
        os.makedirs('Data/Checkpoints/')

    checkpoints = [ModelCheckpoint(
        'Data/Checkpoints/best_weights.h5',
        monitor='val_loss',
        verbose=0,
        save_best_only=True,
        save_weights_only=True,
        mode='auto',
        period=1,
    ), TensorBoard(log_dir='Data/Checkpoints/./logs', histogram_freq=0, write_graph=True, write_images=False,
                   embeddings_freq=0, embeddings_layer_names=None, embeddings_metadata=None)]

    model.fit(x_dataset, y_dataset, batch_size=batch_size, epochs=epochs, validation_data=(x_test, y_test), shuffle=True,
              callbacks=checkpoints)

    return model


def main():
    """
    The main function.
    :return: model
    """
    x_dataset, x_test, y_dataset, y_test, action_total = get_dataset()
    print(action_total)
    model = get_model(action_total)
    model = train_model(model, x_dataset, x_test, y_dataset, y_test)
    save_model(model)
    return model


if __name__ == '__main__':
    main()
