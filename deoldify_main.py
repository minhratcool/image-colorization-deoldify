
#NOTE:  This must be the first call in order to work properly!
from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import *
import warnings
import cv2
import sys # to access the system
from flask import abort



def process(source_url=None):
    try:
        #choices:  CPU, GPU0...GPU7
        device.set(device=DeviceId.CPU)


        plt.style.use('dark_background')
        torch.backends.cudnn.benchmark=True
        warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

        colorizer = get_image_colorizer(artistic=True)

        #NOTE:  Max is 45 with 11GB video cards. 35 is a good default
        render_factor=35
        #NOTE:  Make source_url None to just read from file at ./video/source/[file_name] directly without modification
        source_path = 'test_images/image.png'
        result_path = None

        if source_url is not None:
            result_path = colorizer.plot_transformed_image_from_url(url=source_url, path=source_path, render_factor=render_factor, compare=False)
        else:
            result_path = colorizer.plot_transformed_image(path=source_path, render_factor=render_factor, compare=False)
    except Exception as e:
        print(str(e))
        abort(500)
