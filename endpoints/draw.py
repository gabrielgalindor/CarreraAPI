from urllib import response
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
import os
import json
from models.drawModel import drawM


router = APIRouter()
base_url = "/home/ilana/others/carp_api/api/src/imgs"

@router.get("/test_answer")
def device_get():
    return JSONResponse({'msg': 'The API connection is up'})


@router.get("/get_image")
def return_img(data: drawM):
    img_url = f"{base_url}/{data.collection}_{data.part}{data.variation}.png"
    print(img_url)
    return JSONResponse({'img_url': img_url})


