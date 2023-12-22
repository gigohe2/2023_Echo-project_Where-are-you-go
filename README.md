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

Also, we implemented SFM(Structure From Motion) method to make dataset. You can see the result of mapping indoor environment in downside image.
![image](https://github.com/gigohe2/2023_Echo-project_Where-are-you-go/assets/59073888/78db11f1-c412-4da8-b2a2-79f825daaf37)
But, this method was hard to get accurate map in long time sequence images. So, we were determineded to apply QR code.


## 2. By QR code
To make localizatio easy, we applied QR code method. 
First, we made QR code that contains location of each waypoints in indoor environment.
And then, put a qr code on the ceiling. When user pass through the waypoints, camera recognizes the QR code and get current location from the QR code.

![image](https://github.com/gigohe2/2023_Echo-project_Where-are-you-go/assets/59073888/86dfc840-bd53-4884-9e08-e6e57923bfff)

This is the map for our test bed. User can set a destination by push the tact switch on breadboard.
![image](https://github.com/gigohe2/2023_Echo-project_Where-are-you-go/assets/59073888/9684b27c-61ea-470e-9f85-b68032ab537a)


## 3. Hardware implementation
We used jetson nano development kit, raspberry pi cam, 4 x tact switch, buzzer.
By camera, jetson decodes the QR code and update the current location on map.
And Jetson provides navigation services to users through buzzer sounds.
![image](https://github.com/gigohe2/2023_Echo-project_Where-are-you-go/assets/59073888/65891056-911e-40ab-9881-d3ad5a6d8c53)

