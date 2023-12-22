# 2023_Echo-project_Where-are-you-go

## Introduction
Indoor Navigation System for the Visually Impaired Using Indoor Visual Localization Technology | Team "Where Are You Going?"

## 1. By RGB image
We want get accurate location of camera by using PoseNet. PoseNet inferences x, y, z location and qw, qx, qy, qz quaternion orientation.
We tried hard to train the posenet for DKU engineering building. But, it was hard to get high accuracy for localization.

In echo_localization directory, We applied RGB localization approach to get location.
By using turtlebot, we make an dataset for PoseNet.
By using IMU, motor encoder and LiDAR, we can do SLAM in indoor.
So we get occupancy map to make dataset. We use smartphone camera to get dataset.
When turtlebot goes toward, it's odometry is location and orientation in indoor environment. So we could get smartphone camera's accurate position by syncronize video which was recorded by smartphone and odometry which was obtanined by turtlebot.
![image](https://github.com/gigohe2/2023_Echo-project_Where-are-you-go/assets/59073888/d0921b77-6ee1-4423-bda4-ed60f51adc63)

As i said it before, It was very hard to get high accuracy in indoor environment. It may because our test bed for localization was too featureless so that RGB image doesnt' have any information about where it is.

## 2. By QR code
To make localizatio easy, we applied QR code method.

