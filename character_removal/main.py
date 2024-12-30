import cv2
import numpy as np
import torch
from torchvision import models, transforms
from skimage.restoration import inpaint_biharmonic

class CharacterRemoval:
    def __init__(self):
        self.model = models.detection.maskrcnn_resnet50_fpn(pretrained=True)
        self.model.eval()
        self.transform = transforms.Compose([transforms.ToTensor()])

    def remove_character(self, frame):
        # Convert frame to tensor
        image_tensor = self.transform(frame).unsqueeze(0)

        # Get predictions
        with torch.no_grad():
            predictions = self.model(image_tensor)

        masks = predictions[0]['masks'].cpu().numpy()
        if len(masks) == 0:
            return frame  # No characters detected

        # Combine masks
        combined_mask = np.sum(masks[:, 0, :, :], axis=0) > 0.5

        # Inpaint characters
        result = inpaint_biharmonic(frame, combined_mask, multichannel=True)
        return np.uint8(result * 255)

    def process_video(self, input_video, output_video):
        cap = cv2.VideoCapture(input_video)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = None

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            result_frame = self.remove_character(frame)

            if out is None:
                height, width, _ = frame.shape
                out = cv2.VideoWriter(output_video, fourcc, 30, (width, height))

            out.write(result_frame)

        cap.release()
        out.release()

if __name__ == "__main__":
    remover = CharacterRemoval()
    remover.process_video("input.mp4", "output.mp4")
