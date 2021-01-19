## Description
딥러닝 프로젝트에 사용될 이미지의 간단한 augmenation을 도와주는 파이썬 모듈 . augmentation 변수의 범위를 설정하고 dataset이 들어있는 폴더의 이름만 입력하면 augmentation된 image가 들어있는 dataset폴더 생성

## Requirement
opencv 라이브러리를 이용하여 이미지 처리를 했기 때문에 다음 명령어로 라이브러리를 설치
```
pip install opencv-python
```
## Examples

images 폴더의 image file augmentation

imageaug.py 의Randomaffine, RadomBrCtBl 함수에서 변수 범위 설정후
targetfolder와 augmented image가 들어갈 폴더 경로를 지정해주고 Randomautoaug를 실행하면 자동으로 augmentation을 해서 파일에 저장됨

```
targetfolderpath = 'path/images'
augmentedfolder = 'path/augmented_output/'
Randomautoaug(targetfolderpath,augmentedfolder)
```
![before_aug](https://user-images.githubusercontent.com/69490987/105013417-92cba500-5a82-11eb-965a-d4af8d582186.PNG)
![aug](https://user-images.githubusercontent.com/69490987/105013449-9c550d00-5a82-11eb-98d4-6de9eca57177.PNG)
