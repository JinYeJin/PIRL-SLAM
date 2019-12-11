# Postech PIRL 연구인턴 7기 SLAM
> 본 레포지토리는 ORB-SLAM2의 예제 실행 및 수정방법을 정리하였습니다.


## Contents  
- [Summary](#summary)
- [Environment](#environment)
- [Building ORB-SLAM2 Library](#building-orb-slam2-library)
- [Monocular Example](#monocular example)
- [Weekly Record](https://github.com/JinYeJin/legendary-octo-adventure/wiki/Development-Record)
- [Reference](https://github.com/JinYeJin/legendary-octo-adventure/wiki/Reference)


## Summary

ORB-SLAM을 이용하여 연구를 하기 위해 정리하는 깃 레포지토리입니다.

- ORB-SALM 선정이유
    - [ORB-SLAM](https://github.com/raulmur/ORB_SLAM) Cited by 2371
    - [ORB-SLAM2](https://github.com/raulmur/ORB_SLAM) Cited by 1186
    - 두 버전 모두 오픈소스로 공유됨

## Environment

local에 직접설치, pip, conda 등의 방법이 있지만, conda를 기준으로 적었습니다.

### conda 설치
Ubuntu 16.04 (Debian) 기준으로 [Anaconda Official Documentation](https://docs.anaconda.com/anaconda/install/linux/)에 나와있는 [Installation](https://docs.anaconda.com/anaconda/install/linux/#installation) 과정을 따라하면 됩니다.

### 가상환경 생성

`conda create -n slam python=3.7`

### 필요 라이브러리 설치

`conda install -c menpo opencv3`


## Building ORB-SLAM2 Library

ORB-SALM2의 [build과정](https://github.com/raulmur/ORB_SLAM2#2-prerequisites)을 따릅니다.

## Monocular Example

ORB-SLAM2의 2, 3 과정을 완료한 뒤에 TUM Dataset의 예제를 기반으로 진행합니다.

### Camera Calibration
카메라 캘리브리이션의 개념 [Link](https://darkpgmr.tistory.com/32)

[**camera_calibration.py**](https://github.com/JinYeJin/legendary-octo-adventure/blob/master/camera_calibration.py)가 있는 폴더에서 다음 명령어를 실행합니다. python version은 3.xx입니다.

`python camera_calibration.py [calibaration/image/folder/location]`

### yaml 수정

```
cd ORB_SLAM2/Examples/Monocular
cp TUM_1.yaml custom.yaml
vi custom.yaml
```

결과를 opencv 공식 페이지의 튜토리얼에 적혀있는 [Basics](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html#basics)에 나온 camera matrix와 Distortion coefficients의 구조를 보고 예제실행에 필요한 `custom.yaml`파일을 수정합니다.

### Generate Image Sequence

`Videotofile.py [videopath] [imagefolder] orb-slam2`

videopath에 영상의 경로를 적어주고, imagefolder에 이미지 시퀀스가 생성되길 원하는 폴더의 경로를 적어줍니다. mono_tum 파일을 이용하여 실행되기 위해서 TUM Dataset을 따르기에

```
rgb/
rgb.txt
```

와 같은 구조로 파일들이 생성됩니다. rgb 안에는 이미지 시퀀스가 생성되고, rgb.txt는 rgb파일 안의 이미지들의 타임라인을 나타냅니다.

### 예제 실행

```
cd ORB_SLAM2
./Examples/Monocular/mono_tum Vocabulary/ORBvoc.txt Examples/Monocular/custom.yaml PATH_TO_SEQUENCE_FOLDER
```

`PATH_TO_SEQUENCE_FOLDER`에 `rgb`폴더의 상위 폴더를 적으면 됩니다.
