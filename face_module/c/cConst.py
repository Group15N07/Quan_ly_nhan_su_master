import os

class Const:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    det_weight = os.path.join(BASE_DIR, "../face_module/weights/det_10g.onnx")
    rec_weight = os.path.join(BASE_DIR, "../face_module/weights/w600k_r50.onnx")
    faces_dir = os.path.join(BASE_DIR, "../app/static/faces")
    output_images_dir = os.path.join(BASE_DIR, "../face_module/output_images")

    max_num = 1
    similarity_thresh = 0.5
    confidence_thresh = 0.6
