import cv2


def img2sketch(photo, k_size):
    # Read Image
    img = cv2.imread(photo)

    # Convert to Grey Image
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img = cv2.bitwise_not(grey_img)
    # invert_img=255-grey_img

    # Blur image
    blur_img = cv2.GaussianBlur(invert_img, (k_size, k_size), 0)

    # Invert Blurred Image
    invblur_img = cv2.bitwise_not(blur_img)
    # invblur_img=255-blur_img

    # Sketch Image
    sketch_img = cv2.divide(grey_img, invblur_img, scale=256.0)

    # Save Sketch
    cv2.imwrite('results/' + photo.split("/")[-1], sketch_img)

    # Display sketch
    # cv2.namedWindow('sketch image', 0)
    # cv2.imshow('sketch image', sketch_img)

    # cv2.namedWindow('original image', 0)
    # cv2.imshow('original image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# Function call
img2sketch(photo='images/1.jpg', k_size=7)
img2sketch(photo='images/2.jpg', k_size=7)
img2sketch(photo='images/3.jpg', k_size=7)