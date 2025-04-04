from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib

# Criar a instância do FastAPI
app = FastAPI()


# Criar uma classe que terá os dados do request
class request_body(BaseModel):
  A_id: int
  Size: float
  Weight: float
  Sweetness: float
  Crunchiness: float
  Juiciness	: float
  Ripeness: float
  Acidity	: float

# Carregar Modelo para realizar a classificação
quality_model = joblib.load('./fruit_quality_model.pkl')


@app.post('/classify')
def predict(data: request_body):
  # Preparar features

  input_features = [[data.Size, data.Weight, data.Sweetness, data.Crunchiness, data.Juiciness, data.Ripeness, data.Acidity]]

  # Classificar Fruta
  y_pred = quality_model.predict(input_features)[0].astype(int)
  y_prob = quality_model.predict_proba(input_features)[0].astype(float)

  response = 'Boa' if y_pred == 1 else 'Ruim'
  probability = y_prob[y_pred]

  return {
    "qualidade": response,
    "probability": probability
  }