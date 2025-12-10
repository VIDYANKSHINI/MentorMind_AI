import os
import onnxruntime as ort

sess_options = ort.SessionOptions()
providers = ['CPUExecutionProvider']

session = ort.InferenceSession("clarity_model.onnx", sess_options=sess_options, providers=providers)
session = ort.InferenceSession("engagement_model.onnx", sess_options=sess_options, providers=providers)
session = ort.InferenceSession("filler_model.onnx", sess_options=sess_options, providers=providers)
session = ort.InferenceSession("pace_model.onnx", sess_options=sess_options, providers=providers)
session = ort.InferenceSession("tech_depth_model.onnx", sess_options=sess_options, providers=providers)




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")





def load_model(path):
    session = ort.InferenceSession(path)
    print("\n🔍 MODEL LOADED:", path)

    print("➡ Inputs:", [i.name for i in session.get_inputs()])
    print("➡ Outputs:", [o.name for o in session.get_outputs()])

    return session

