# Standard-Chartered Hackathon:

**Live Links**

- **Video Presentation:** 

![WhatsApp Image 2024-03-15 at 10 49 06_8eb09984](https://github.com/MithileshEN/Standard-Chartered/assets/87403588/26149caf-6bca-48b2-b84b-f482867871da)
## Problem Statement
Faster Cheque Clearing: Bank handles large volumes of cheques in the clearing process. The process involves many technical verifications including signature verification. Some of these steps are manual and require human intervention to complete the process. The current process requires the high human capital deployment and longer processing time.
Solution
## Admin side Dashboard

    -Process the cheque electronically
    -Automation of sign verification,MICR detection,pattern matching,OCR extraction,handwriting recognition,whitespace reduction
    -Stats on Total cheques processed and inward and outward pending cheques
    -View the online complaints filed by the bank customers
    -Reply/respond the actions to those complaints
## Customer side interface
      -Process the cheque electronically from anywhere using the webapplication
      -Perform sign verification
      -Raise the complaints on any cheque processing or other bank related issues
      -View the status of the complaints already sent
      -An intelligent system support(Chatbot) to address any queries
      -Chatbot transfers the queries those which it cannot answer and admin will reply to those queries
## Screenshots of the dashboard

![WhatsApp Image 2024-03-15 at 08 38 24_91972bc5](https://github.com/MithileshEN/Standard-Chartered/assets/87403588/243e9797-da49-4095-bf60-c02aaba782da)

![WhatsApp Image 2024-03-15 at 10 14 06_581c8a07](https://github.com/MithileshEN/Standard-Chartered/assets/87403588/6a0e5c76-f9fb-4381-8fe6-cb570b38e85c)

![image](https://github.com/MithileshEN/Standard-Chartered/assets/87403588/c82b3373-a801-4dcb-b7db-eb935886d7f1)

![image](https://github.com/MithileshEN/Standard-Chartered/assets/87403588/e82b1e09-456a-49dc-8714-fe2ef1ca126c)

![image](https://github.com/MithileshEN/Standard-Chartered/assets/87403588/0e3a76b9-a66e-41cb-8c4a-fd87273bd146)

![image](https://github.com/MithileshEN/Standard-Chartered/assets/87403588/300cb252-93d3-454e-ae72-4526abb87e57)

![image](https://github.com/MithileshEN/Standard-Chartered/assets/87403588/157f6630-5a88-40df-9bff-0535bc8b3d2b)

![image](https://github.com/MithileshEN/Standard-Chartered/assets/87403588/443bc95c-330b-4d92-ba56-6954d427ff90)

## Admin side basically has the same structure 
Reply to a complaint
![image](https://github.com/MithileshEN/Standard-Chartered/assets/87403588/25048198-551e-41a9-a6f5-c49a88d73c38)




## MICR ENTIRE CODE
https://colab.research.google.com/drive/1QxR_MfBY6JmD0A_A6R0vmxgGjIg9yOm7?authuser=0#scrollTo=n0loZB88JtKT

## A dictionary named chars containing keys representing characters and corresponding values as Numpy arrays representing binary images

![Screenshot1](https://github.com/MithileshEN/Standard-Chartered/assets/102873408/07932204-f803-4693-84e1-7254dab678cf)

-**This code initializes a list of reference character names, representing digits and special symbols, each corresponding to specific information found on checks.
the image is then loaded and then it is converted to grayscale. white characters with black bg
Find Contours: It finds contours in the reference image (ref) using the cv2.findContours() function. Contours are detected based on the provided retrieval mode (cv2.RETR_EXTERNAL) and contour approximation method (cv2.CHAIN_APPROX_SIMPLE). The resulting contours are stored in refCnts, while the second return value is discarded (denoted by _).**
![Screenshot (146)](https://github.com/MithileshEN/Standard-Chartered/assets/102873408/4e0f2aed-46d0-4ac3-bbc9-1ba00e5a94d8)

-**This code snippet initializes a rectangular kernel and an empty list for storing the output of the check Optical Character Recognition (OCR) process. It also loads input images, grabs their dimensions, and extracts the bottom 20% of each image where the account information is typically located.**

![Screenshot (150)](https://github.com/MithileshEN/Standard-Chartered/assets/102873408/8a7ff4ca-a85c-4143-9178-2e5b22719d01)
![Screenshot (149)](https://github.com/MithileshEN/Standard-Chartered/assets/102873408/5ffa9314-d6c1-41e9-b389-aa2bb19df57b)

-**The bounding box coordinates (x, y, w, h) are computed using cv2.boundingRect(c).
A green bounding box is drawn around the contour on the clone image using cv2.rectangle(). The rectangle's corners are defined by the top-left and bottom-right points of the bounding box.**
-**The result is an image (clone) with green bounding boxes drawn around each detected contour, indicating the regions of interest (ROIs) in the reference image. This process is typically performed as a preprocessing step for template matching or character recognition tasks.
Then each character is displayed after conversion to a greyscale format in a vertical manner**
-**Tesseract , pillow and other required libraries and packages are installed
Import necessary packages for detecting texts in the cheque image. Load the image and then detect all the possible text components and print the same. The main components like Accoount number, SAAMP no, MICR, IFSC code , Cheque number  are stored in the csv and json format**
![Screenshot (145)](https://github.com/MithileshEN/Standard-Chartered/assets/102873408/816e9398-1f09-4551-91f4-1a8aee365d0b)












