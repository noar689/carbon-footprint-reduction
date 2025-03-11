from fastapi import FastAPI
from recommendation1 import recommend_low_carbon

app = FastAPI()

@app.get("/recommend/")
def get_recommendations(product_name: str, top_n: int = 5):
    recommendations = recommend_low_carbon(product_name, top_n)
    if recommendations is None or recommendations.empty:
        return {"message": "No recommendations found"}
    
    return recommendations.to_dict(orient="records")



