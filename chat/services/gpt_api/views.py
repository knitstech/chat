import uvicorn
from fastapi import APIRouter, FastAPI

from chat.services.gpt_api.schema import GPTModel

router = APIRouter()
app = FastAPI()  # for test


@app.get("/model_info")
async def send_model_info() -> GPTModel:
    """# noqa: D202 D400 D205
    Sends info about model used in project

    :returns: GPTModel.
    """

    # test response without api-key
    return GPTModel(
        id="test_mode",
        object="some_mode",
        created_at=51248129,  # noqa: WPS432
        owned_by="KnitsTech",
    )


# to run app for debugging
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)  # noqa: WPS432 S104
