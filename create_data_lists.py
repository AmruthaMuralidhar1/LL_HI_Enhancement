# Import the create_data_lists function from utils
from utils import create_data_lists

# Define the main function
if __name__ == '__main__':

    create_data_lists(train_folders=['/content/drive/MyDrive/train2014',
                                     '/content/drive/MyDrive/val2014'],
                      test_folders=['/content/drive/MyDrive/BSDS100',
                                    '/content/drive/MyDrive/Set5',
                                    '/content/drive/MyDrive/Set14'],
                      min_size=100,
                      output_folder='/content/drive/MyDrive/srgan_output/')
