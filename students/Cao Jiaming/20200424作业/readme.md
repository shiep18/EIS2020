# 20200424 operation

1. Search the openvino installation method and read

2. Install the software in the downloaded package

3. Use today's Yolo to speed up code testing


# 20200424作业
1.自己搜索一下Openvino安装方法，阅读  
2.用下载的包里面的软件安装  
3.用今天的yolo加速代码测试  

# OpenVINO 安装及使用

安装
https://docs.openvinotoolkit.org/latest/_docs_install_guides_installing_openvino_linux.html

使用
文档：https://software.intel.com/en-us/openvino-toolkit/documentation/featured

$ --input 一定要给定节点名和端口号
$ python3 /opt/intel/openvino/deployment_tools/model_optimizer/mo_tf.py --input_model ./recognition_frozen_model.pb --input DatasetToSingleElement:0 --input_shape=[32,32,32,1] --output text_resnet15/conv5_0/relu --log_level=DEBUG
（1）TensorFlow 模型转换成 OpenVINO 的 IR 模型：
https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_TensorFlow.html

（2）OpenVINO 支持的 TensorFlow 的 Layers：
https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_Supported_Frameworks_Layers.html
如果 OpenVINO 中没有 TensorFlow 的 Layers，可以自定义 Layers：
https://docs.openvinotoolkit.org/latest/_docs_HOWTO_Custom_Layers_Guide.html
https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_customize_model_optimizer_Customize_Model_Optimizer.html
目前 OpenVINO 不支持的 TensorFlow Op：

tf.math.tanh：https://tensorflow.google.cn/api_docs/python/tf/math/tanh
tf.math.less_equal：https://tensorflow.google.cn/api_docs/python/tf/math/less_equal
tf.debugging.Assert：https://tensorflow.google.cn/api_docs/python/tf/debugging/Assert
tf.select：https://stackoverflow.com/questions/41505746/what-is-the-use-of-tf-select
tf.math.ceil：https://tensorflow.google.cn/api_docs/python/tf/math/ceil
tf.math.log：https://tensorflow.google.cn/api_docs/python/tf/math/log
tf.keras.backend.all：https://tensorflow.google.cn/api_docs/python/tf/keras/backend/all
（3）模型转成 IR 模型后，通过 OpenVINO 的 API 实现高效的 inference：
https://docs.openvinotoolkit.org/latest/_docs_IE_DG_Integrate_with_customer_application_new_API.html

（4）自定义模型中的 json + pipeline.config 说明
