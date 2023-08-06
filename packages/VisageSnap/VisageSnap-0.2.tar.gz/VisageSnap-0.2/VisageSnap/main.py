import face_recognition
from dataclasses import dataclass
import os
import numpy as np
from sklearn.semi_supervised import LabelPropagation
from sklearn.exceptions import NotFittedError
import pickle

@dataclass
class Face():
    label: str
    encodings: np.ndarray
    filenames: list

@dataclass
class From():
    LABEL = "Label"
    FILENAME = "Filename"

@dataclass
class To():
    NAME = "Name"
    NUMBER = "Number"

@dataclass
class As():
    LABELED = True
    UNLABELED = False

# Make a class to semi-supervised the face recognition
class Core():
    def __init__(self):
        """
        VisageSnap Core Class
        ---------------------
        """
        _default_dir = os.getcwd()
        self.faces: list[Face] = []

        # Directory
        self.unlabeled_dir = os.path.join(_default_dir, "unlabeled")
        self.labeled_dir = os.path.join(_default_dir, "labeled")

        self.model_dir = os.path.join(_default_dir, "model", "face_model.pkl")

        self.predict_dir = os.path.join(_default_dir, "predict")

        self.label: dict = {}

        self.threshold = 0.42

        self.model = self._load_model()

    @staticmethod
    def _isImage(filename: str) -> bool:
        """
        This function checks if the file is an image file.
        
        Parameters
        ----------
        filename (str) : target filename.
        """
        list = [
            ".jpg",
            ".png",
            ".jpeg"
            ]

        for i in list:
            if filename.endswith(i):
                return True
        return False

    def get_faceObject(self, target: str, value: str) -> Face:
        """
        This function returns the face object with the given label.
        
        Parameters
        ----------
        target (str) :
            - "From.LABEL" : label of the face object. (name of the person)
            - "From.FILENAME" : filename of the face object.
        
        value (str) : value of the target.
        """
        for face in self.faces:
            if target == "Label":
                if face.label == value:
                    return face
            elif target == "Filename":
                if value in face.filenames:
                    return face
        return None



    def _load_labeled(self): # 미리 주어지는 데이터는 한 사진에 한 사람만 있어야 한다.
        """
        This function loads the labeled data from the labeled directory.
        """
        for filename in os.listdir(self.labeled_dir):
            if self._isImage(filename):
                print("Loading labeled data: {}".format(filename))
                label = (filename.split(".")[0]).split("-")[0] # 파일 형식은 이름-번호.jpg
                image = face_recognition.load_image_file(os.path.join(self.labeled_dir, filename))
                encodings = face_recognition.face_encodings(image)[0]

                # 만약 두개의 얼굴이 같은 사진에 있다면
                if len(face_recognition.face_encodings(image)) > 1:
                    print("There are more than one face in the image: {}".format(filename))
                    continue
                
                # 같은 이름이 있는지 확인
                face_found = False
                for i, face in enumerate(self.faces):
                    if face.label == label:
                        print("The label is already in the list: {}".format(filename))
                        # 동일한 인코딩이 있는지 확인
                        if np.array_equal(face.encodings, encodings):
                            print("The encoding is already in the list: {}".format(filename))
                            continue
                        self.faces[i].encodings = np.vstack((face.encodings, encodings))
                        self.faces[i].filenames.append(filename)
                        face_found = True
                        break
                
                if not face_found:
                    self.faces.append(Face(label, encodings, [filename]))


    def _load_unlabeled(self):
        """
        This function loads the unlabeled data from the unlabeled directory.
        """
        for filename in os.listdir(self.unlabeled_dir):
            if self._isImage(filename):
                print("Loading unlabeled data: {}".format(filename))
                image = face_recognition.load_image_file(os.path.join(self.unlabeled_dir, filename))
                encodings = face_recognition.face_encodings(image)

                if len(encodings) == 0:
                    print("There is no face in the image: {}".format(filename))
                    continue

                for encoding in encodings:
                    self.faces.append(Face("unknown", encoding, [filename]))


    def _load_model(self) -> LabelPropagation:
        try:
            with open(self.model_dir, "rb") as f:
                self.model, self.faces = pickle.load(f)
                print("Model loaded.")
                return self.model
        except:
            print("There is no model in the model directory. create a new model.")
            self.model = LabelPropagation()
            self.faces = [] # 초기화
            return self.model

    def _save_model(self):
        data = (self.model, self.faces)
        with open(self.model_dir, "wb") as f:
            pickle.dump(data, f)

    def convert_labelType(self, value, to: str):
        """
        This function converts the label type. (numberLabel -> nameLabel, nameLabel -> numberLabel)
        
        Parameters
        ----------
        value (str or int) : target value.
        to (str) :
            - "To.NAME" : convert to name label.
            - "To.NUMBER" : convert to number label.
        """
        if to == "Name":
            for name, number in self.label.items():
                if number == value:
                    return name
        elif to == "Number":
            return self.label.get(value, -1)
        return None

    def set_label(self, person):
        """
        This function sets the label dictionary.
        
        Parameters
        ----------
        person (list or dict) : label list or dictionary.

        Example
        -------
        person = ["name1", "name2", "name3", ...]

        OR

        person = {
            "name1": 0,
            "name2": 1,
            "name3": 2,
            ...
        }

        - name1, name2, name3, ... : name of the person
        - 0, 1, 2, ... : number label (MUST NOT BE -1)
        """
        
        if type(person) == dict:
            self.label = person
        elif type(person) == list:
            for i in range(len(person)):
                self.label[person[i]] = i

    def set_directory(self, dict: dict):
        """
        This function sets the directory.
        
        Parameters
        ----------
        dict (dict) : directory dictionary.

        Example
        -------
        dict = {
            "labeled": "labeled",
            "unlabeled": "unlabeled",
            "model": "model"
        }
        - labeled : directory of the labeled data
        - unlabeled : directory of the unlabeled data
        - model : directory of the model

        Default
        -------
        labeled : "labeled"
        unlabeled : "unlabeled"
        model : "model"
        """
        if "labeled" in dict:
            self.labeled_dir = dict["labeled"]
        if "unlabeled" in dict:
            self.unlabeled_dir = dict["unlabeled"]
        if "model" in dict:
            self.model_dir = dict["model"]
        

    def _train(self, labeled: bool):
        if labeled:
            self._load_labeled()
        else:
            self._load_unlabeled()

        t_names = []
        t_encodings =[]

        for face in self.faces:
            for encoding in face.encodings:
                numberLabel = self.convert_labelType(face.label, To.NUMBER)
                if labeled and numberLabel == -1:
                    continue
                t_names.append(numberLabel)
                t_encodings.append(encoding)

        t_encodings = np.array(t_encodings)
        t_names = np.array(t_names)
        
        print("Training the labeled data...")
        self.model.fit(t_encodings, t_names)
        self._save_model()
        print("Labeled training is done. The model is saved in the model directory.")

    def train_labeled_data(self):
        self._train(As.LABELED)

    def train_unlabeled_data(self):
        self._train(As.UNLABELED)

    
    @staticmethod
    def _get_average(face: Face):
        """
        This function returns the average of the encodings.
        
        Parameters
        ----------
        face (Face) : target face.
        """
        return np.average(face.encodings, axis=0)

    @staticmethod
    def _get_distance(encoding1, encoding2):
        """
        This function returns the distance between two encodings.
        
        Parameters
        ----------
        encoding1 (np.array) : encoding1.
        encoding2 (np.array) : encoding2.
        """
        return np.linalg.norm(encoding1 - encoding2)

    def _isNotUnknown(self, encoding):
        """
        This function checks whether the encoding is unknown.
        
        Parameters
        ----------
        encoding (np.array) : target encoding.
        """
        print("Checking whether the encoding is unknown...")
        min_distance = 1
        for face in self.faces:
            print(face.label)
            average = self._get_average(face) # 저장된 얼굴 평균 구하고
            distance = self._get_distance(encoding, average) # 타겟과의 거리를 구한다
            if distance < min_distance:
                min_distance = distance

        print("min_distance : ", min_distance)
        print("ended")

        if min_distance < self.threshold:
            print("아는사람")
            return True # 모르는 사람이 아니다
        print("모르는사람")
        return False # 모르는 사람이다

    def predict(self, image) -> list:
        predictions_dict = {}

        target_encodings = face_recognition.face_encodings(image)
        if len(target_encodings) == 0:
            return None
        
        result = []
        for target_encoding in target_encodings:
            if self._isNotUnknown(target_encoding): # 모르는 사람이 아니면
                result.append(self.model.predict([target_encoding])[0])
            else:
                result.append(-1)
        
        return result # list 



    def predict_all(self):
        result = {}
        for filename in os.listdir(self.predict_dir):
            if self._isImage(filename) == False:
                return
            
            image = face_recognition.load_image_file(os.path.join(self.predict_dir, filename))
            prediction = self.predict(image)

            if prediction == None:
                raise("There is no face in the image.")
            
            if len(prediction) == 1:
                result[filename] = self.convert_labelType(prediction[0], To.NAME)
            else:
                result[filename] = []
                for p in prediction:
                    result[filename].append(self.convert_labelType(p, To.NAME))
        return result