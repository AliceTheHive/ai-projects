$ conda create --name aind-nlp-capstone python=3.5 numpy

Fetching package metadata .........
Solving package specifications: .

Package plan for installation in environment /home/aind2/anaconda3/envs/aind-nlp-capstone:

The following NEW packages will be INSTALLED:

    mkl:        2017.0.3-0   
    numpy:      1.13.0-py35_0
    openssl:    1.0.2l-0     
    pip:        9.0.1-py35_1 
    python:     3.5.3-1      
    readline:   6.2-2        
    setuptools: 27.2.0-py35_0
    sqlite:     3.13.0-0     
    tk:         8.5.18-0     
    wheel:      0.29.0-py35_0
    xz:         5.2.2-1      
    zlib:       1.2.8-3

$ conda install notebook ipykernel

Fetching package metadata .........
Solving package specifications: .

Package plan for installation in environment /home/aind2/anaconda3/envs/aind-nlp-capstone:

The following NEW packages will be INSTALLED:

    bleach:           1.5.0-py35_0 
    decorator:        4.0.11-py35_0
    entrypoints:      0.2.2-py35_1 
    html5lib:         0.999-py35_0 
    ipykernel:        4.6.1-py35_0 
    ipython:          6.1.0-py35_0 
    ipython_genutils: 0.2.0-py35_0 
    jedi:             0.10.2-py35_2
    jinja2:           2.9.6-py35_0 
    jsonschema:       2.6.0-py35_0 
    jupyter_client:   5.1.0-py35_0 
    jupyter_core:     4.3.0-py35_0 
    libsodium:        1.0.10-0     
    markupsafe:       0.23-py35_2  
    mistune:          0.7.4-py35_0 
    nbconvert:        5.2.1-py35_0 
    nbformat:         4.3.0-py35_0 
    notebook:         5.0.0-py35_0 
    pandocfilters:    1.4.1-py35_0 
    path.py:          10.3.1-py35_0
    pexpect:          4.2.1-py35_0 
    pickleshare:      0.7.4-py35_0 
    prompt_toolkit:   1.0.14-py35_0
    ptyprocess:       0.5.1-py35_0 
    pygments:         2.2.0-py35_0 
    python-dateutil:  2.6.0-py35_0 
    pyzmq:            16.0.2-py35_0
    simplegeneric:    0.8.1-py35_1 
    six:              1.10.0-py35_0
    terminado:        0.6-py35_0   
    testpath:         0.3.1-py35_0 
    tornado:          4.5.1-py35_0 
    traitlets:        4.3.2-py35_0 
    wcwidth:          0.1.7-py35_0 
    zeromq:           4.1.5-0  

$ source activate aind-nlp-capstone

$ ipython kernel install --user

Installed kernelspec python3 in /home/aind2/.local/share/jupyter/kernels/python3

$ pip install tensorflow-gpu -U

$ pip install keras -U

$ KERAS_BACKEND=tensorflow python -c "from keras import backend"

$ jupyter notebook --ip=0.0.0.0 --no-browser


Within Jupyter Notebook, running `!python --version` returns:

Python 3.5.3 :: Continuum Analytics, Inc.


Going to "About" displays popup:

About Jupyter Notebook
Server Information:

You are using Jupyter notebook.

The version of the notebook server is 5.0.0 and is running on:
Python 3.5.3 |Continuum Analytics, Inc.| (default, Mar  6 2017, 11:58:13) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]

Current Kernel Information:

Python 3.5.3 |Continuum Analytics, Inc.| (default, Mar  6 2017, 11:58:13) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.



~/aind2-nlp-capstone$ jupyter notebook --ip=0.0.0.0 --no-browser
[I 08:33:02.856 NotebookApp] Serving notebooks from local directory: /home/aind2/aind2-nlp-capstone
[I 08:33:02.856 NotebookApp] 0 active kernels 
[I 08:33:02.856 NotebookApp] The Jupyter Notebook is running at: http://0.0.0.0:8888/?token=23b0e8a32bb7269667cfa2aa3f9ee62594feadd7852796
[I 08:33:02.856 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 08:33:02.857 NotebookApp] 
    
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://0.0.0.0:8888/?token=23b0e8a32bb7269667cfa2aa3f9ee62594feadd7852796b
[I 08:33:21.790 NotebookApp] 302 GET /?token=23b0e8a32bb7269667cfa2aa3f9ee62594feadd7852796 (49.195.129.60) 0.61ms
[W 08:33:28.966 NotebookApp] 404 GET /nbextensions/widgets/notebook/js/extension.js?v=20170703083302 (49.195.129.60) 6.56ms referer=http://54.252.221.217:8888/notebooks/machine_translation.ipynb
[I 08:33:29.910 NotebookApp] Kernel started: c510b4d2-0749-4db2-93e6-23772169337e
[I 08:33:29.912 NotebookApp] 302 GET /notebooks/images/rnn.png (49.195.129.60) 0.88ms
[I 08:33:29.913 NotebookApp] 302 GET /notebooks/images/embedding.png (49.195.129.60) 0.68ms
[I 08:33:29.915 NotebookApp] 302 GET /notebooks/images/bidirectional.png (49.195.129.60) 0.67ms
[I 08:33:30.492 NotebookApp] Adapting to protocol v5.1 for kernel c510b4d2-0749-4db2-93e6-23772169337e
[W 08:34:30.457 NotebookApp] IOPub data rate exceeded.
    The notebook server will temporarily stop sending output
    to the client in order to avoid crashing it.
    To change this limit, set the config variable
    `--NotebookApp.iopub_data_rate_limit`.
[W 08:34:30.570 NotebookApp] iopub messages resumed
[W 08:34:51.577 NotebookApp] IOPub data rate exceeded.
    The notebook server will temporarily stop sending output
    to the client in order to avoid crashing it.
    To change this limit, set the config variable
    `--NotebookApp.iopub_data_rate_limit`.
[W 08:34:52.324 NotebookApp] iopub messages resumed
2017-07-03 08:35:00.581874: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.1 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-03 08:35:00.581908: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-03 08:35:00.581921: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-07-03 08:35:00.581936: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-03 08:35:00.581952: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
2017-07-03 08:35:03.411980: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:893] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-07-03 08:35:03.412468: I tensorflow/core/common_runtime/gpu/gpu_device.cc:940] Found device 0 with properties: 
name: Tesla K80
major: 3 minor: 7 memoryClockRate (GHz) 0.8235
pciBusID 0000:00:1e.0
Total memory: 11.17GiB
Free memory: 11.11GiB
2017-07-03 08:35:03.412497: I tensorflow/core/common_runtime/gpu/gpu_device.cc:961] DMA: 0 
2017-07-03 08:35:03.412511: I tensorflow/core/common_runtime/gpu/gpu_device.cc:971] 0:   Y 
2017-07-03 08:35:03.412527: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Creating TensorFlow device (/gpu:0) -> (device: 0, name: Tesla K80, pci bus id: 0000:00:1e.0)
2017-07-03 08:35:05.226270: I tensorflow/core/common_runtime/gpu/pool_allocator.cc:247] PoolAllocator: After 11003 get requests, put_count=10977 evicted_count=1000 eviction_rate=0.0910996 and unsatisfied allocation rate=0.102336
2017-07-03 08:35:05.226305: I tensorflow/core/common_runtime/gpu/pool_allocator.cc:259] Raising pool_size_limit_ from 100 to 110
[I 08:38:44.962 NotebookApp] Saving file at /machine_translation.ipynb
[I 08:40:55.932 NotebookApp] Saving file at /machine_translation.ipynb
[I 08:44:15.673 NotebookApp] Saving file at /machine_translation.ipynb
[I 08:46:35.832 NotebookApp] Saving file at /machine_translation.ipynb
[I 08:55:34.719 NotebookApp] Saving file at /machine_translation.ipynb
2017-07-03 09:00:46.585953: I tensorflow/core/common_runtime/gpu/pool_allocator.cc:247] PoolAllocator: After 15371 get requests, put_count=15382 evicted_count=1000 eviction_rate=0.0650111 and unsatisfied allocation rate=0.065578
2017-07-03 09:00:46.585986: I tensorflow/core/common_runtime/gpu/pool_allocator.cc:259] Raising pool_size_limit_ from 212 to 233
[I 09:18:22.030 NotebookApp] Saving file at /machine_translation.ipynb
[I 09:23:44.858 NotebookApp] Saving file at /machine_translation.ipynb
[I 09:24:58.203 NotebookApp] Saving file at /machine_translation.ipynb
[I 09:44:06.778 NotebookApp] Saving file at /machine_translation.ipynb
2017-07-03 09:45:08.178118: I tensorflow/core/common_runtime/gpu/pool_allocator.cc:247] PoolAllocator: After 62269 get requests, put_count=62314 evicted_count=1000 eviction_rate=0.0160478 and unsatisfied allocation rate=0.0160433
2017-07-03 09:45:08.178166: I tensorflow/core/common_runtime/gpu/pool_allocator.cc:259] Raising pool_size_limit_ from 493 to 542
[I 09:51:50.407 NotebookApp] Saving file at /machine_translation.ipynb
[I 09:54:08.903 NotebookApp] Saving file at /machine_translation.ipynb
[I 10:01:23.891 NotebookApp] Kernel interrupted: c510b4d2-0749-4db2-93e6-23772169337e
[I 10:10:58.038 NotebookApp] Saving file at /machine_translation.ipynb
[I 10:11:56.310 NotebookApp] Saving file at /machine_translation.ipynb
^C[I 10:16:45.828 NotebookApp] interrupted
Serving notebooks from local directory: /home/aind2/aind2-nlp-capstone
1 active kernels 
The Jupyter Notebook is running at: http://0.0.0.0:8888/?token=23b0e8a32bb7269667cfa2aa3f9ee62594feadd7852796
Shutdown this notebook server (y/[n])? y
[C 10:16:49.823 NotebookApp] Shutdown confirmed
[I 10:16:49.823 NotebookApp] Shutting down kernels