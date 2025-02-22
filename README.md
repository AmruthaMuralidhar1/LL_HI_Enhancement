## Setup Instructions

# 1. **Upload Folders to Google Drive**
To run the Python scripts on Google Colab, follow these steps to set up the necessary directories:

- **Upload the following folders to your Google Drive:**
  - **Colab Notebooks**
  - **Set14_results**
  - **srgan_output**

- **Create the following additional folders (if not already present):**
  - Folder 1: `train_images`
  - Folder 2: `test_images`
  - Folder 3: `models`
  - Folder 4: `results`

Ensure that the folder structure on your Google Drive mirrors the screenshot provided (`Google drive Screen Shot.png`).

# 2. **Upload Images**
- **Training Folder (`train_images`)**: Upload your training images here.
- **Testing Folder (`test_images`)**: Upload your testing images here.

# 3. **Upload Python Scripts to Google Colab**
All Python files need to be uploaded manually to Google Colab. You can do this by opening your Colab notebook, going to the Files tab, and uploading your scripts.

# 4. **Automatic Files**
Some files, such as `.json` files and model files, will be automatically created during the training and evaluation processes.

# 5. **Training Process**
- The total number of epochs will be dynamically calculated based on a formula embedded in the script. You don't need to worry about manually setting the number of epochs.

---

## Evaluation

After training the model, you can evaluate its performance using the following command:

```bash
!python eval.py
