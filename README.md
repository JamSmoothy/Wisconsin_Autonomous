# Wisconsin_Autonomous

## Methodology
I downloaded Python 3, Jupyter, Anaconda and OpenCV. I then asked ChatGPT how to display images using OpenCV and promptly copied its code. It also told me to switch to HSV, so I did that. Then, I used it to figure out how to isolate the red cones and fiddled around with the lower and upper bounds so that the door would not show in the image, but the cones would remain. Shockingly, I then asked ChatGPT how to use erosion to remove the extra specks around the image that were ruining it. I then asked it to pinpoint the x,y coordinate of each cone and it managed to do it using _findContours_ which managed to work. At this point, I noticed that the left-side cones and right-side cones were each on seperate halves of the image, so I created left-hand and right-hand lists, then ran them through a linear regression and drew a line using their coordinates.

## Failures
My masking and erosion functions do not preserve the cones very well (as seen in 'color.png') and so I think that that would be an area I need to work on in the future, because they might not work on other data sets. I tried searching up how to intelligently split the cones into two groups based on their sides, but I could not find an answer and by this point it was like 9 pm, so I decided to just hard-code them into two separate groups. I hope that in the future I will get better at machine learning (this was my first attempt ever, which is why I needed ChatGPT's help so much) and I am excited to learn.

## Libraries
1. Numpy
2. OpenCV
