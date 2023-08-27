{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "02e93b47-060f-4900-bea6-3647c7b5e2df",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "import mediapipe as mp\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9d5db62-3a44-4da7-97fd-8a16fd27c49e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "\n",
    "class handDetector():\n",
    "    def __init__(self,mode = False,maxHands = 2,DetectionCOn = 0.5, trackcon = 0.5):\n",
    "        #initialising variable for Hands thought not used here \n",
    "        self.mode = mode\n",
    "        self.maxHands = maxHands\n",
    "        self.DetectionCOn = DetectionCOn\n",
    "        self.trackcon = trackcon\n",
    "        \n",
    "        #using hands funtion to get the hand detected\n",
    "        self.mpHands = mp.solutions.hands\n",
    "        self.hands = self.mpHands.Hands()\n",
    "        self.mpDraw = mp.solutions.drawing_utils\n",
    "\n",
    "    #drawing basic hand  \n",
    "    def findHands(self, img,draw = True):\n",
    "        self.imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)\n",
    "        self.results = self.hands.process(self.imgRGB)\n",
    "        #print(results.multi_hand_landmarks)   #will print co-ordinatates of hand\n",
    "\n",
    "\n",
    "        #Getting the image and masking the nodes on it\n",
    "        if self.results.multi_hand_landmarks:\n",
    "            for handLms in self.results.multi_hand_landmarks:\n",
    "                if draw:\n",
    "                    self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)\n",
    "        return img\n",
    "\n",
    "\n",
    "#Add this as well below for loop if you want edge by edge\n",
    "    def findPosition(self, img, handNo = 0, draw = True):\n",
    "        lmlist= []\n",
    "        if self.results.multi_hand_landmarks:\n",
    "            myHand = self.results.multi_hand_landmarks[handNo]\n",
    "            \n",
    "            for id,lm in enumerate(myHand.landmark):\n",
    "                            h,w,c = img.shape\n",
    "                            cx,cy = int(lm.x*w) , int(lm.y*h)\n",
    "                            lmlist.append([id,cx,cy])  #this will give the point and the coordinate of the point\n",
    "                            if  draw:   #Checking which id is where and creating a circle around it\n",
    "                                cv2.circle(img,(cx,cy),15,(255,0,0),cv2.FILLED)    \n",
    "        return lmlist\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f568ca1e-1c97-461e-8a02-a50ff99aee4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    #Getting FPS\n",
    "    pTime = 0\n",
    "    cTime = 0  \n",
    "    # Setup camera\n",
    "    cap = cv2.VideoCapture(0)\n",
    "    #calling class\n",
    "    detector  = handDetector()\n",
    "    while True:\n",
    "\n",
    "        #reading the basic image\n",
    "        success , img = cap.read()\n",
    "    \n",
    "        detector.findHands(img)\n",
    "        lmlist = detector.findPosition(img)\n",
    "        \n",
    "        if len(lmlist) !=0:\n",
    "            print(lmlist[4])\n",
    "         #fps module\n",
    "        cTime = time.time()\n",
    "        fps = 1/(cTime-pTime)\n",
    "        pTime = cTime\n",
    "\n",
    "        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,2,(250,30,32),3)\n",
    "\n",
    "        cv2.imshow('Image', img)\n",
    "\n",
    "        if cv2.waitKey(1) == ord('q'):\n",
    "            break\n",
    "            \n",
    "            \n",
    "    cap.release()\n",
    "    cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2ef8e11-d53d-467a-9cf4-0ba4c0e5c60b",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7df0eaf7-d6a6-458f-bf09-b4d89e7d36b0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd207f4a-f5d4-4084-95b9-0a4ed7debed5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Bankai",
   "language": "python",
   "name": "bankai"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
