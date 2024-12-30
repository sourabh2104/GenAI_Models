from diffusers import StableDiffusionPipeline
import cv2
import numpy as np

class VideoGenerator:
    def __init__(self):
        self.pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
        self.pipeline.to("cuda")  # Use GPU for faster generation

    def generate_frame(self, prompt):
        image = self.pipeline(prompt).images[0]
        return np.array(image)

    def generate_video(self, prompt, output_video, num_frames=30):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = None

        for i in range(num_frames):
            frame = self.generate_frame(f"{prompt}, frame {i}")
            if out is None:
                height, width, _ = frame.shape
                out = cv2.VideoWriter(output_video, fourcc, 30, (width, height))

            out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

        out.release()

if __name__ == "__main__":
    generator = VideoGenerator()
    generator.generate_video("A scenic landscape", "generated_video.mp4")
