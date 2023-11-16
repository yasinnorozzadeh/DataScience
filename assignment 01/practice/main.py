import cv2

class CropFace:
    def __init__(self):
        self.normal_image = cv2.imread(r"imgs\normal.jpg")
        self.happy_image = cv2.imread(r"imgs\happy.jpg")
        self.sad_image = cv2.imread(r"imgs\sad.jpg")
        self.wondered_image = cv2.imread(r"imgs\wondered.jpg")
        self.angry_image = cv2.imread(r"imgs\angry.jpg")

        rimg = self.resize_image(self.normal_image)
        face = rimg[170:260, 125:190]
        cv2.imwrite("output images/normal_face.jpg", face)


    def crop_angry_image(self, img):
        rimg = self.resize_image(img)
        face = rimg[155:240, 320:380]
        # show(rimg)
        self.show(face)
        cv2.imwrite("output images/angry_face.jpg", face)
        return face

    def crop_sad_image(self, img):
        rimg = self.resize_image(img)
        face = rimg[150:270, 270:360]
        # show(rimg)
        self.show(face)
        cv2.imwrite("output images/sad_face.jpg", face)
        return face

    def crop_happy_image(self, img):
        rimg = self.resize_image(img)
        face = rimg[230:310, 205:260]
        # show(rimg)
        self.show(face)
        cv2.imwrite("output images/happy_face.jpg", face)
        return face

    def crop_wondered_image(self, img):
        rimg = self.resize_image(img)
        face = rimg[80:190, 295:365]
        # show(rimg)
        self.show(face)
        cv2.imwrite("output images/wondered_face.jpg", face)
        return face

    def show(self, img, name="face"):
        cv2.imshow(name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def resize_image(self, img):
        r, c, _ = img.shape
        rimg = cv2.resize(img, (c//2, r//2))
        return rimg


class Draw_rectangle(CropFace):
    def __init__(self):
        super().__init__()
        
    def draw_on_happy_image(self):
        img = self.happy_image
        img = self.resize_image(img)
        # 230:310, 205:260
        cv2.rectangle(img, (260, 230), (205, 310), (255, 255, 20), 5)
        self.show(img, "rectangle")
        cv2.imwrite("output images/draw_rectangle_on_happy_face.jpg", img)
    
    def draw_on_angry_image(self):
        img = self.angry_image
        img = self.resize_image(img)
        # 155:240, 320:380
        cv2.rectangle(img, (380, 155), (320, 240), (20, 255, 255), 5)
        self.show(img, "rectangle")
        cv2.imwrite("output images/draw_rectangle_on_angry_face.jpg", img)

    def draw_on_normal_image(self):
        img = self.normal_image
        img = self.resize_image(img)
        # 170:260, 125:190
        cv2.rectangle(img, (190, 170), (125, 260), (20, 255, 255), 5)
        self.show(img, "rectangle")
        cv2.imwrite("output images/draw_rectangle_on_normal_face.jpg", img)

    def draw_on_sad_image(self):
        img = self.sad_image
        img = self.resize_image(img)
        # 150:270, 270:360
        cv2.rectangle(img, (360, 150), (270, 270), (20, 255, 255), 5)
        self.show(img, "rectangle")
        cv2.imwrite("output images/draw_rectangle_on_sad_face.jpg", img)

    def draw_on_wondered_image(self):
        img = self.wondered_image
        img = self.resize_image(img)
        # 80:190, 295:365
        cv2.rectangle(img, (365, 80), (295, 190), (20, 255, 255), 5)
        self.show(img, "rectangle")
        cv2.imwrite("output images/draw_rectangle_on_wondered_face.jpg", img)

class ChangeFace(CropFace):
    def __init__(self):
        super().__init__()
        self.main_image = self.normal_image
        self.main_image = self.resize_image(self.main_image)
    # 170:260, 125:190    
    def change_normal_to_happy(self):
        rface = cv2.resize(self.crop_happy_image(self.happy_image), (190-125, 260-170))
        self.main_image[170:260, 125:190] = rface
        self.show(self.main_image, "changed")
        cv2.imwrite("output images/change_normal_to_happy.jpg", self.main_image)

    def change_normal_to_sad(self):
        rface = cv2.resize(self.crop_sad_image(self.sad_image), (190-125, 260-170))
        self.main_image[170:260, 125:190] = rface
        self.show(self.main_image, "changed")
        cv2.imwrite("output images/change_normal_to_sad.jpg", self.main_image)

    def change_normal_to_angry(self):
        rface = cv2.resize(self.crop_angry_image(self.angry_image), (190-125, 260-170))
        self.main_image[170:260, 125:190] = rface
        self.show(self.main_image, "changed")
        cv2.imwrite("output images/change_normal_to_angry.jpg", self.main_image)

    def change_normal_to_wondered(self):
        rface = cv2.resize(self.crop_wondered_image(self.wondered_image), (190-125, 260-170))
        self.main_image[170:260, 125:190] = rface
        self.show(self.main_image, "changed")
        cv2.imwrite("output images/change_normal_to_wondered.jpg", self.main_image)

if __name__ == "__main__":
    draw = Draw_rectangle()
    draw.draw_on_angry_image()
    draw.draw_on_happy_image()
    draw.draw_on_normal_image()
    draw.draw_on_sad_image()
    draw.draw_on_wondered_image()
    ############################################################
    c = ChangeFace()
    c.change_normal_to_happy()
    c.change_normal_to_sad()
    c.change_normal_to_angry()
    c.change_normal_to_wondered()
