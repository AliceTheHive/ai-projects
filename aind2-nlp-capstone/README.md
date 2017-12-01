# Introduction
In this notebook, you will build a deep neural network that functions as part of an end-to-end machine translation pipeline. Your completed pipeline will accept English text as input and return the French translation.

# Launch on EC2 GPU Instance with udacity-aind AMI
* Follow Steps 1 to 10 in instructions_launch_ec2_gpu_instance.pdf
* Follow Step 11 in instructions_launch_ec2_gpu_instance.pdf to Login with:
	```
	ssh aind2@X.X.X.X
	```
* Follow Step 12 on EC2 GPU instance. Ensure correct Python kernel version in Jupyter https://stackoverflow.com/questions/30492623/using-both-python-2-x-and-python-3-x-in-ipython-notebook
	```
	git clone https://github.com/ltfschoen/aind2-nlp-capstone
	cd aind2-nlp-capstone
	conda create --name aind-nlp-capstone python=3.5 numpy
	source activate aind-nlp-capstone
	conda install notebook ipykernel
	ipython kernel install --user
	pip install tensorflow-gpu -U
	pip install keras -U
	KERAS_BACKEND=tensorflow python -c "from keras import backend"
	jupyter notebook --ip=0.0.0.0 --no-browser
	```
	* Open in browser the URL shown in terminal and replace IP address
	with that in the AWS EC2 Dashboard http://<EC2_IP_address>:8888/?token=3156e..
	* Click machine_translation.ipynb
	* Within Jupyter Notebook, running `!python --version` returns:
		`Python 3.5.3 :: Continuum Analytics, Inc.`

# Setup
## Install
- Python 3
- NumPy
- TensorFlow 1.x
- Keras 2.x

# Start
This project is within a [Jupyter Notebook](http://jupyter.org/).  To start the notebook, run the command `jupyter notebook machine_translation.ipynb` in this directory.
Follow the instructions within the notebook.

# Submission
When you are ready to submit your project, do the following steps:
1. Ensure you pass all points on the [rubric](https://review.udacity.com/#!/rubrics/1004/view).
2. Submit the following in a zip file:
  - `helper.py`
  - `machine_translation.ipynb`
  - `machine_translation.html` - You can export the notebook by navigating to **File -> Download as -> HTML (.html)**.
