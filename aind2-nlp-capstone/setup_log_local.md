$ source deactivate aind-nlp-capstone
$ conda remove --name aind-nlp-capstone --all
$ conda create --name aind-nlp-capstone python=3.5.3 numpy
Fetching package metadata .........
Solving package specifications: .

Package plan for installation in environment /Users/PC/miniconda3/envs/aind-nlp-capstone:

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

(aind-nlp-capstone) $ conda install notebook ipykernel
Fetching package metadata .........
Solving package specifications: .

Package plan for installation in environment /Users/PC/miniconda3/envs/aind-nlp-capstone:

The following NEW packages will be INSTALLED:

    appnope:          0.1.0-py35_0 
		...

(aind-nlp-capstone) $ ipython kernel install --user
Installed kernelspec python3 in /Users/PC/Library/Jupyter/kernels/python3


(aind-nlp-capstone) $ pip install tensorflow-gpu -U
Collecting tensorflow-gpu
  Using cached tensorflow_gpu-1.1.0-cp35-cp35m-macosx_10_11_x86_64.whl
Requirement already up-to-date: wheel>=0.26 in /Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages (from tensorflow-gpu)
Collecting werkzeug>=0.11.10 (from tensorflow-gpu)
  Using cached Werkzeug-0.12.2-py2.py3-none-any.whl
Requirement already up-to-date: numpy>=1.11.0 in /Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages (from tensorflow-gpu)
Requirement already up-to-date: six>=1.10.0 in /Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages (from tensorflow-gpu)
Collecting protobuf>=3.2.0 (from tensorflow-gpu)
Collecting setuptools (from protobuf>=3.2.0->tensorflow-gpu)
  Using cached setuptools-36.0.1-py2.py3-none-any.whl
Installing collected packages: werkzeug, setuptools, protobuf, tensorflow-gpu
  Found existing installation: setuptools 27.2.0
    Uninstalling setuptools-27.2.0:
      Successfully uninstalled setuptools-27.2.0
Successfully installed protobuf-3.3.0 setuptools-36.0.1 tensorflow-gpu-1.1.0 werkzeug-0.12.2
Traceback (most recent call last):
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/bin/pip", line 6, in <module>
    sys.exit(pip.main())
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/pip/__init__.py", line 249, in main
    return command.main(cmd_args)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/pip/basecommand.py", line 252, in main
    pip_version_check(session)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/pip/utils/outdated.py", line 102, in pip_version_check
    installed_version = get_installed_version("pip")
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/pip/utils/__init__.py", line 838, in get_installed_version
    working_set = pkg_resources.WorkingSet()
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/pip/_vendor/pkg_resources/__init__.py", line 644, in __init__
    self.add_entry(entry)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/pip/_vendor/pkg_resources/__init__.py", line 700, in add_entry
    for dist in find_distributions(entry, True):
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/pip/_vendor/pkg_resources/__init__.py", line 1949, in find_eggs_in_zip
    if metadata.has_metadata('PKG-INFO'):
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/pip/_vendor/pkg_resources/__init__.py", line 1463, in has_metadata
    return self.egg_info and self._has(self._fn(self.egg_info, name))
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/pip/_vendor/pkg_resources/__init__.py", line 1823, in _has
    return zip_path in self.zipinfo or zip_path in self._index()
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/pip/_vendor/pkg_resources/__init__.py", line 1703, in zipinfo
    return self._zip_manifests.load(self.loader.archive)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/pip/_vendor/pkg_resources/__init__.py", line 1643, in load
    mtime = os.stat(path).st_mtime
FileNotFoundError: [Errno 2] No such file or directory: '/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/setuptools-27.2.0-py3.5.egg'


(aind-nlp-capstone) $ pip install tensorflow -U
Collecting tensorflow
  Using cached tensorflow-1.2.1-cp35-cp35m-macosx_10_11_x86_64.whl
  ...
Installing collected packages: backports.weakref, html5lib, markdown, tensorflow
  Found existing installation: html5lib 0.999
    DEPRECATION: Uninstalling a distutils installed project (html5lib) has been deprecated and will be removed in a future version. This is due to the fact that uninstalling a distutils project will only partially uninstall the project.
    Uninstalling html5lib-0.999:
      Successfully uninstalled html5lib-0.999
Successfully installed backports.weakref-1.0rc1 html5lib-0.9999999 markdown-2.6.8 tensorflow-1.2.1




(aind-nlp-capstone) $ pip install keras -U
Collecting keras
Collecting pyyaml (from keras)
...
Collecting theano (from keras)
Requirement already up-to-date: numpy>=1.9.1 in /Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages (from theano->keras)
Collecting scipy>=0.14 (from theano->keras)
  Using cached scipy-0.19.1-cp35-cp35m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Installing collected packages: pyyaml, scipy, theano, keras
Successfully installed keras-2.0.5 pyyaml-3.12 scipy-0.19.1 theano-0.9.0






About Jupyter Notebook
Server Information:

You are using Jupyter notebook.

The version of the notebook server is 5.0.0 and is running on:
Python 3.5.3 |Continuum Analytics, Inc.| (default, Mar  6 2017, 12:15:08) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)]

Current Kernel Information:

Python 3.5.3 |Continuum Analytics, Inc.| (default, Mar  6 2017, 12:15:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.









Input shape is 3D tensor with shape (batch_size, timesteps, input_dim):  (137861, 21, 1)
Output space dimensionality:  21
English vocab size:  199
French vocab size:  344
Padded Sequences:  [[17 23  1 ...,  0  0  0]
 [ 5 20 21 ...,  0  0  0]
 [22  1  9 ...,  0  0  0]
 ..., 
 [24  1 10 ...,  0  0  0]
 [ 5 84  1 ...,  0  0  0]
 [ 0  0  0 ...,  0  0  0]]
Reshaped tmp_x:  (137861, 21, 1)
Input shape is 3D tensor with shape (batch_size, timesteps, input_dim):  (137861, 21, 1)
Output space dimensionality:  21
English vocab size:  199
French vocab size:  344
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
simple_rnn_2 (SimpleRNN)     (None, 21, 21)            483       
_________________________________________________________________
dropout_2 (Dropout)          (None, 21, 21)            0         
_________________________________________________________________
time_distributed_3 (TimeDist (None, 21, 688)           15136     
_________________________________________________________________
time_distributed_4 (TimeDist (None, 21, 344)           237016    
=================================================================
Total params: 252,635
Trainable params: 252,635
Non-trainable params: 0
_________________________________________________________________
Model Summary:  None
Train on 110288 samples, validate on 27573 samples
Epoch 1/2
109568/110288 [============================>.] - ETA: 0s - loss: 2.9606 - sparse_categorical_accuracy: 0.4377
---------------------------------------------------------------------------
InvalidArgumentError                      Traceback (most recent call last)
~/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tensorflow/python/client/session.py in _do_call(self, fn, *args)
   1138     try:
-> 1139       return fn(*args)
   1140     except errors.OpError as e:

~/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tensorflow/python/client/session.py in _run_fn(session, feed_dict, fetch_list, target_list, options, run_metadata)
   1120                                  feed_dict, fetch_list, target_list,
-> 1121                                  status, run_metadata)
   1122 

~/miniconda3/envs/aind-nlp-capstone/lib/python3.5/contextlib.py in __exit__(self, type, value, traceback)
     65             try:
---> 66                 next(self.gen)
     67             except StopIteration:

~/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tensorflow/python/framework/errors_impl.py in raise_exception_on_not_ok_status()
    465           compat.as_text(pywrap_tensorflow.TF_Message(status)),
--> 466           pywrap_tensorflow.TF_GetCode(status))
    467   finally:

InvalidArgumentError: Received a label value of 344 which is outside the valid range of [0, 344).  Label values: 7 88 1 64 16 13 14 5 7 83 1 40 13 14 0 0 0 0 0 0 0 11 30 1 67 15 25 22 47 6 3 1 58 69 2 56 0 0 0 0 0 0 62 1 92 2 41 5 
...
198 22 164 2 186 187 0 0 0 0 0 0 0 0 0 0 0 0 0 4 32 31 1 9 22 102 15 25 22 47 5 3 1 8 66 15 42 0 0 0
	 [[Node: SparseSoftmaxCrossEntropyWithLogits_1/SparseSoftmaxCrossEntropyWithLogits = SparseSoftmaxCrossEntropyWithLogits[T=DT_FLOAT, Tlabels=DT_INT64, _device="/job:localhost/replica:0/task:0/cpu:0"](Reshape_4, Cast_4)]]

During handling of the above exception, another exception occurred:

InvalidArgumentError                      Traceback (most recent call last)
<ipython-input-8-95da4938e93f> in <module>()
    105                      epochs=2,
    106                      validation_split=0.2,
--> 107                      verbose=1)
    108 
    109 # Print prediction(s)

~/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/keras/models.py in fit(self, x, y, batch_size, epochs, verbose, callbacks, validation_split, validation_data, shuffle, class_weight, sample_weight, initial_epoch, **kwargs)
    868                               class_weight=class_weight,
    869                               sample_weight=sample_weight,
--> 870                               initial_epoch=initial_epoch)
    871 
    872     def evaluate(self, x, y, batch_size=32, verbose=1,

~/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/keras/engine/training.py in fit(self, x, y, batch_size, epochs, verbose, callbacks, validation_split, validation_data, shuffle, class_weight, sample_weight, initial_epoch, **kwargs)
   1505                               val_f=val_f, val_ins=val_ins, shuffle=shuffle,
   1506                               callback_metrics=callback_metrics,
-> 1507                               initial_epoch=initial_epoch)
   1508 
   1509     def evaluate(self, x, y, batch_size=32, verbose=1, sample_weight=None):

~/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/keras/engine/training.py in _fit_loop(self, f, ins, out_labels, batch_size, epochs, verbose, callbacks, val_f, val_ins, shuffle, callback_metrics, initial_epoch)
   1168                         val_outs = self._test_loop(val_f, val_ins,
   1169                                                    batch_size=batch_size,
-> 1170                                                    verbose=0)
   1171                         if not isinstance(val_outs, list):
   1172                             val_outs = [val_outs]

~/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/keras/engine/training.py in _test_loop(self, f, ins, batch_size, verbose)
   1270                 ins_batch = _slice_arrays(ins, batch_ids)
   1271 
-> 1272             batch_outs = f(ins_batch)
   1273             if isinstance(batch_outs, list):
   1274                 if batch_index == 0:

~/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/keras/backend/tensorflow_backend.py in __call__(self, inputs)
   2267         updated = session.run(self.outputs + [self.updates_op],
   2268                               feed_dict=feed_dict,
-> 2269                               **self.session_kwargs)
   2270         return updated[:len(self.outputs)]
   2271 

~/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tensorflow/python/client/session.py in run(self, fetches, feed_dict, options, run_metadata)
    787     try:
    788       result = self._run(None, fetches, feed_dict, options_ptr,
--> 789                          run_metadata_ptr)
    790       if run_metadata:
    791         proto_data = tf_session.TF_GetBuffer(run_metadata_ptr)

~/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tensorflow/python/client/session.py in _run(self, handle, fetches, feed_dict, options, run_metadata)
    995     if final_fetches or final_targets:
    996       results = self._do_run(handle, final_targets, final_fetches,
--> 997                              feed_dict_string, options, run_metadata)
    998     else:
    999       results = []

~/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tensorflow/python/client/session.py in _do_run(self, handle, target_list, fetch_list, feed_dict, options, run_metadata)
   1130     if handle is None:
   1131       return self._do_call(_run_fn, self._session, feed_dict, fetch_list,
-> 1132                            target_list, options, run_metadata)
   1133     else:
   1134       return self._do_call(_prun_fn, self._session, handle, feed_dict,

~/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tensorflow/python/client/session.py in _do_call(self, fn, *args)
   1150         except KeyError:
   1151           pass
-> 1152       raise type(e)(node_def, op, message)
   1153 
   1154   def _extend_graph(self):

InvalidArgumentError: Received a label value of 344 which is outside the valid range of [0, 344).  Label values: 7 88 1 64 16 13 14 5 7 83 1 40 13 14 0 0 0 0 0 0 0 11 30 1 67 15 25 22 47 6 3 1 58 69 2 56 0 0 0 0 0 0 62 1 92 2 41 5 
...
0 0 3 1 198 22 164 2 186 187 0 0 0 0 0 0 0 0 0 0 0 0 0 4 32 31 1 9 22 102 15 25 22 47 5 3 1 8 66 15 42 0 0 0
	 [[Node: SparseSoftmaxCrossEntropyWithLogits_1/SparseSoftmaxCrossEntropyWithLogits = SparseSoftmaxCrossEntropyWithLogits[T=DT_FLOAT, Tlabels=DT_INT64, _device="/job:localhost/replica:0/task:0/cpu:0"](Reshape_4, Cast_4)]]

Caused by op 'SparseSoftmaxCrossEntropyWithLogits_1/SparseSoftmaxCrossEntropyWithLogits', defined at:
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/ipykernel_launcher.py", line 16, in <module>
    app.launch_new_instance()
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/traitlets/config/application.py", line 658, in launch_instance
    app.start()
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/ipykernel/kernelapp.py", line 477, in start
    ioloop.IOLoop.instance().start()
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/zmq/eventloop/ioloop.py", line 177, in start
    super(ZMQIOLoop, self).start()
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tornado/ioloop.py", line 888, in start
    handler_func(fd_obj, events)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tornado/stack_context.py", line 277, in null_wrapper
    return fn(*args, **kwargs)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/zmq/eventloop/zmqstream.py", line 440, in _handle_events
    self._handle_recv()
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/zmq/eventloop/zmqstream.py", line 472, in _handle_recv
    self._run_callback(callback, msg)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/zmq/eventloop/zmqstream.py", line 414, in _run_callback
    callback(*args, **kwargs)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tornado/stack_context.py", line 277, in null_wrapper
    return fn(*args, **kwargs)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/ipykernel/kernelbase.py", line 283, in dispatcher
    return self.dispatch_shell(stream, msg)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/ipykernel/kernelbase.py", line 235, in dispatch_shell
    handler(stream, idents, msg)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/ipykernel/kernelbase.py", line 399, in execute_request
    user_expressions, allow_stdin)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/ipykernel/ipkernel.py", line 196, in do_execute
    res = shell.run_cell(code, store_history=store_history, silent=silent)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/ipykernel/zmqshell.py", line 533, in run_cell
    return super(ZMQInteractiveShell, self).run_cell(*args, **kwargs)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2698, in run_cell
    interactivity=interactivity, compiler=compiler, result=result)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2802, in run_ast_nodes
    if self.run_code(code, result):
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2862, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-8-95da4938e93f>", line 95, in <module>
    len(french_tokenizer.word_index))
  File "<ipython-input-8-95da4938e93f>", line 79, in simple_model
    metrics=['sparse_categorical_accuracy'] # or 'accuracy'
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/keras/models.py", line 788, in compile
    **kwargs)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/keras/engine/training.py", line 911, in compile
    sample_weight, mask)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/keras/engine/training.py", line 436, in weighted
    score_array = fn(y_true, y_pred)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/keras/losses.py", line 53, in sparse_categorical_crossentropy
    return K.sparse_categorical_crossentropy(y_pred, y_true)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/keras/backend/tensorflow_backend.py", line 2784, in sparse_categorical_crossentropy
    logits=logits)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tensorflow/python/ops/nn_ops.py", line 1690, in sparse_softmax_cross_entropy_with_logits
    precise_logits, labels, name=name)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tensorflow/python/ops/gen_nn_ops.py", line 2486, in _sparse_softmax_cross_entropy_with_logits
    features=features, labels=labels, name=name)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tensorflow/python/framework/op_def_library.py", line 767, in apply_op
    op_def=op_def)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tensorflow/python/framework/ops.py", line 2506, in create_op
    original_op=self._default_original_op, op_def=op_def)
  File "/Users/PC/miniconda3/envs/aind-nlp-capstone/lib/python3.5/site-packages/tensorflow/python/framework/ops.py", line 1269, in __init__
    self._traceback = _extract_stack()

InvalidArgumentError (see above for traceback): Received a label value of 344 which is outside the valid range of [0, 344).  Label values: 7 88 1 64 16 13 14 5 7 83 1 40 13 14 0 0 0 0 0 0 0 11 30 1 67 15 25 22 47 6 3 1 58 69 2 56 0 0 0 0 0 0 62 1 
...
14 0 0 0 0 0 0 0 0 3 100 4 73 4 159 6 4 75 0 0 0 0 0 0 0 0 0 0 0 0 3 1 198 22 164 2 186 187 0 0 0 0 0 0 0 0 0 0 0 0 0 4 32 31 1 9 22 102 15 25 22 47 5 3 1 8 66 15 42 0 0 0
	 [[Node: SparseSoftmaxCrossEntropyWithLogits_1/SparseSoftmaxCrossEntropyWithLogits = SparseSoftmaxCrossEntropyWithLogits[T=DT_FLOAT, Tlabels=DT_INT64, _device="/job:localhost/replica:0/task:0/cpu:0"](Reshape_4, Cast_4)]]



(aind-nlp-capstone) $ jupyter notebook machine_translation.ipynb 
[I 20:37:53.153 NotebookApp] Serving notebooks from local directory: /Users/PC/code/aind-projects/aind2-nlp-capstone
[I 20:37:53.153 NotebookApp] 0 active kernels 
[I 20:37:53.153 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/?token=2f17f102b53856e784878b0eddec2bdd50f9bd152b49d829
[I 20:37:53.153 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 20:37:53.155 NotebookApp] 
    
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=2f17f102b53856e784878b0eddec2bdd50f9bd152b49d829
[I 20:37:53.570 NotebookApp] Accepting one-time-token-authenticated connection from ::1
[W 20:37:55.132 NotebookApp] Notebook machine_translation.ipynb is not trusted
[W 20:37:55.625 NotebookApp] 404 GET /nbextensions/widgets/notebook/js/extension.js?v=20170703203752 (::1) 10.13ms referer=http://localhost:8888/notebooks/machine_translation.ipynb
[I 20:38:07.485 NotebookApp] Kernel started: 86c6430e-ab19-4a8d-b1f8-cc1a81423f3f
[I 20:38:07.491 NotebookApp] 302 GET /notebooks/images/bidirectional.png (::1) 2.42ms
[I 20:38:07.493 NotebookApp] 302 GET /notebooks/images/embedding.png (::1) 1.92ms
[I 20:38:07.496 NotebookApp] 302 GET /notebooks/images/rnn.png (::1) 1.95ms
[I 20:38:16.691 NotebookApp] Adapting to protocol v5.1 for kernel 86c6430e-ab19-4a8d-b1f8-cc1a81423f3f
[I 20:40:08.223 NotebookApp] Saving file at /machine_translation.ipynb
[W 20:40:39.471 NotebookApp] IOPub data rate exceeded.
    The notebook server will temporarily stop sending output
    to the client in order to avoid crashing it.
    To change this limit, set the config variable
    `--NotebookApp.iopub_data_rate_limit`.
[W 20:40:39.709 NotebookApp] iopub messages resumed
[W 20:41:08.105 NotebookApp] IOPub data rate exceeded.
    The notebook server will temporarily stop sending output
    to the client in order to avoid crashing it.
    To change this limit, set the config variable
    `--NotebookApp.iopub_data_rate_limit`.
[W 20:41:09.174 NotebookApp] iopub messages resumed
2017-07-03 20:41:41.396016: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-03 20:41:41.396066: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
[I 20:42:08.402 NotebookApp] Saving file at /machine_translation.ipynb
[I 20:44:08.534 NotebookApp] Saving file at /machine_translation.ipynb
2017-07-03 20:44:09.773062: W tensorflow/core/framework/op_kernel.cc:1158] Invalid argument: Received a label value of 344 which is outside the valid range of [0, 344).  Label values: 7 88 1 64 16 13 14 5 7 83 1 40 13 14 0 0 0 0 0 0 0 11 30 1 67 15 25 22 47 6 3 1 58 69 2 56 0 0 0 0 0 0 62 1 92 2 41 