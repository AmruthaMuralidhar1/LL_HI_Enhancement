My Offer Letter link: https://drive.google.com/file/d/1Du7FCjEhqQpKv2X6UJtyymE8t5-UTVye/view

Result Super-Resolved Image: https://github.com/V-KennyPhilip/Samsung-Prism-Project/blob/main/super_resolved_image.png 

Image Super Resolution <3

Setup:
If you want to run the python scripts on google colab, make sure you first upload the folders appearing in the screen shot "Google drive Screen Shot.png"
Except for the folders "Colab Notebooks", "Set14_results" and "srgan_output", create the other folders
After creating the folders, add images to each folder for training and testing process

All the python files need to be uploaded on google colab, manually
Note: few files like .json will automatically be created, as well as the models(duhhh)
The total number of epochs is dynamic, it is calculated based on a formula!!

Evaluation:
!python eval.py will evaluate the models and give us the PSNR and SSIM values

Results:
!python super_resolve.py will perform the operation on the images present in one of the test folders(from drive), and also creates a "folder_resluts" file

Further work:
The current output of images goes directly to the drive folder: need to output it on the running colab cell
