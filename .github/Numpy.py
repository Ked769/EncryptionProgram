
from tensorflow import keras
import keras_cv
# Visualization
import matplotlib.pyplot as plt

# Save the image
from PIL import Image


def do():
    keras.mixed_precision.set_global_policy("mixed_float16")
    model = keras_cv.models.StableDiffusion(img_height=512,
                                            img_width=512,
                                            jit_compile=True)
    images = model.text_to_image(prompt="A painting of a city by vincent van gogh, highly detailed,\
                                      sharp focused, impressionism, oil painting", batch_size=2)

    # Plot the images
    plot_images(images)
    import os
    os.mkdir("D:/AIcv")

    Image.fromarray(images[0]).save("van_gogh_city1.png")
    Image.fromarray(images[1]).save("van_gogh_city2.png")


def plot_images(images):
    # Set figure size
    plt.figure(figsize=(20, 20))
    # Loop through each image
    for i in range(len(images)):
        # Subplot setup
        ax = plt.subplot(1, len(images), i + 1)
        # Plot each image
        plt.imshow(images[i])
        print(type(ax))
        # Do not show axis
        plt.axis("off")
