# 使用OpenCV人脸识别功能
def detect_face(img):
    # 将测试图像转换为灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 加载OpenCV人脸检测，默认使用快速运行的LBP
    # 可以选用更准确但速度较慢的Haar分类
    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')
    # 检测多尺度某些（图像可能比其他图像更靠近相机）图像
    # 输出一张面孔列表
    Faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    # 如果未检测到脸部，则返回原始img
    if len(Faces) == 0:
        return None, None
    # 在假设只有一张脸的情况下，提取脸部区域
    (x, y, w, h) = Faces[0]
    # 仅返回图片种的脸部区域
    return gray[y:y + w, x:x + h], Faces[0]
# 现在使用的是OpenCV的** LBP人脸检测**
# 在_line 4_上，将图像转换为灰度，因为OpenCV中的大多数操作都是在灰度下执行的
# 在_line 8_上，使用`cv2.CascadeClassifier`类加载了LBP人脸检测
# 在_line 12_上，使用`cv2.CascadeClassifier`类的'`detectMultiScale`函数来检测图像中的所有面孔
# 在_line 20_上，仅从检测到的人脸中选择第一张人脸，因为在一张图像中将只有一个人脸（假设只有一个突出的人脸）
# 由于用detectMultiScale函数返回的人脸实际上是矩形（x，y，宽度，高度），而不是实际人脸图像，因此必须从主图像中提取人脸图像区域
# 在_line 23_上，从灰度图像中提取了脸部区域，并返回了脸部图像区域和脸部矩形
# 现在已经创建了一个人脸检测


# In[4]:
# 此功能将读取所有人的训练图像，从每个图像中检测出人脸，并将返回两个大小完全相同的列表，一个是人脸列表，以及每个人脸标签对应的另一个人脸列表
def prepare_training_data(data_folder_path):
    # ------STEP-1--------
    # g获取数据文件夹中的目录（每个对象一个目录）
    dirs = os.listdir(data_folder_path)
    # 列出所有对象的面孔
    Faces = []
    # 列出所有对象的标签
    Labels = []
    # 遍历每个目录并读取其中的图像
    for dir_name in dirs:
        # 对象目录以字母's'开头，因此忽略任何不相关的目录（如果有的话）
        if not dir_name.startswith("s"):
            continue
        # ------STEP-2--------
        # 从dir_name中提取对象的标签号
        # 目录名称的格式= s+label，因此从dir_name中删除字母's'将数字给到标签
        label = int(dir_name.replace("s", ""))
        # 为当前对象图像中的目录包含路径构建路径
        # 样本 subject_dir_path = "training-data/s1"
        subject_dir_path = data_folder_path + "/" + dir_name
        # 获取给定对象目录中的图像名称
        subject_images_names = os.listdir(subject_dir_path)
        # ------STEP-3--------
        # 遍历每个图像名称，读取图像，检测人脸并将人脸信息添加到人脸列表中
        for image_name in subject_images_names:
            # 忽略.DS_Store之类的系统文件
            if image_name.startswith("."):
                continue
            # 建立映像路径
            # 样本图像 path = training-data/s1/1.pgm
            image_path = subject_dir_path + "/" + image_name
            # 读取图像
            image = cv2.imread(image_path)
            # 显示图像窗口以显示图像
            cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            cv2.waitKey(100)
            # 检测脸
            face, rect = detect_face(image)
            # ------STEP-4--------
            # for the purpose of this tutorial
            # 忽略未检测到的脸部
            if face is not None:
                # 将面孔添加到面孔列表
                Faces.append(face)
                # 为此人添加标签
                Labels.append(label)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    return Faces, Labels
# 该函数采用存储训练对象文件夹的路径作为参数
# 此功能遵循上述相同的4个准备数据子步骤
# **(step-1)**
# 在_line 8_上，使用`os.listdir`函数来读取存储在传递给函数作为参数的路径上的所有文件夹的名称
# 在_line 10-13_上，定义标签和人脸向量
# **(step-2)**
# 遍历所有对象的文件夹名称，并在_line 27_上对每个对象的文件夹名称中进行遍历，然后提取标签信息
# 由于文件夹名称遵循s+Label命名约定，因此从文件夹名称中删除字母s后将对应数字分配给该对象的标签
# **(step-3)**
# 在_line 34_上，读取了正在遍历的当前对象的所有图像名称
# 在_line 39-66_上，遍历了这些图像
# 在第53-54行，使用OpenCV的imshow（window_title，image）和OpenCV的waitKey（interval）函数来显示当前被遍历的图像
# `waitKey（interval）`函数将代码流暂停给定的间隔（毫秒）（默认100毫秒）
# 在_57行上，从正在遍历的当前图像中检测人脸
# **(step-4)**
# 在_line 62-66_上，将检测到的脸部和标签添加到它们各自的向量中
# 记下来准备用于训练人脸识别的数据


# In[5]:
# 首先准备训练数据
# 数据将在保存两个相同大小的列表中
# 一个列表将包含所有面孔，另一个列表将包含每个面孔各自的标签
print("Preparing data...")
faces, labels = prepare_training_data("training-data")
print("Data prepared")
# 输出全部面孔和标签
print("Total faces: ", len(faces))
print("Total labels: ", len(labels))
# ### 训练人脸识别
# OpenCV配备了三个人脸识别
# 1. EigenFace Recognizer: 可以使用`cv2.face.createEigenFaceRecognizer()`创建
# 2. FisherFace Recognizer: 可以使用`cv2.face.createFisherFaceRecognizer()`创建
# 3. Local Binary Patterns Histogram (LBPH): 可以使用`cv2.face.LBPHFisherFaceRecognizer()`创建
# 默认使用LBPH人脸识别
# 无论选择使用哪种OpenCV人脸识别，只需要更改一行，即下面给出的人脸识别初始化行，其他代码都将保持不变


# In[6]:
# 创建LBPH人脸识别
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# 或者使用 EigenFaceRecognizer 通过将上面的行替换为
# face_recognizer = cv2.face.EigenFaceRecognizer_create()
# 或者使用 FisherFaceRecognizer 通过将上面的行替换为
# face_recognizer = cv2.face.FisherFaceRecognizer_create()
# 现在已经初始化了脸部识别，通过调用人脸识别的“ train（faces-vector，labels-vector）”函数来训练脸部识别


# In[7]:
# 训练人脸识别
print(labels)
face_recognizer.train(faces, np.array(labels))


# In[8]:
# 根据给定的（x，y）坐标和给定宽度和高度用函数在图像上绘制矩形
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


# 函数从传递的（x，y）坐标开始在给定图像上绘制文本
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
# 函数`draw_rectangle`根据传递的矩形坐标在图像上绘制一个矩形
# 使用OpenCV的内置函数`cv2.rectangle（img，topLeftPoint，bottomRightPoint，rgbColor，lineWidth）`在测试图像中检测到的人脸周围绘制一个矩形
# 函数`draw_text`使用OpenCV的内置函数`cv2.putText（img，text，startPoint，font，fontSize，rgbColor，lineWidth）`在图像上绘制文本
# 通过调用`predict（face）`函数即可在测试图像上测试人脸识别


# In[9]:
# 此功能可识别所通过图像中的人物，并在检测到的人脸周围绘制一个带有对象名称的矩形
def predict(test_img):
    # 复制图像，保留更改原始图像
    img = test_img.copy()
    # 从图像中检测人脸
    face, rect = detect_face(img)
    cv2.imshow("face", face)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    # 使用人脸识别预测图像
    label, confidence = face_recognizer.predict(face)
    print("label,confidence", label, confidence)
    # 获取人脸识别返回的各个标签的名称
    label_text = subjects[label]
    # 在检测到的人脸周围绘制一个矩形
    draw_rectangle(img, rect)
    # 绘制预测人物的名字
    draw_text(img, label_text, rect[0], rect[1] - 5)
    return img
# 现在已经很好地定义了预测功能，下一步是在测试图像上实际调用此功能，并显示这些测试图像，以查看人脸识别是否正确识别了它们


# In[10]:
print("Predicting images...")
# 加载测试图像
test_img1 = cv2.imread("test-data/test1.jpg")
test_img2 = cv2.imread("test-data/test2.jpg")
test_img3 = cv2.imread("test-data/test3.jpg")
# 执行预测
predicted_img1 = predict(test_img1)
predicted_img2 = predict(test_img2)
predicted_img3 = predict(test_img3)
print("Prediction complete")
# 显示所有图像
cv2.imshow(subjects[1], cv2.resize(predicted_img1, (400, 500)))
cv2.imshow(subjects[2], cv2.resize(predicted_img2, (400, 500)))
cv2.imshow(subjects[3], cv2.resize(predicted_img3, (400, 500)))
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.destroyAllWindows()
