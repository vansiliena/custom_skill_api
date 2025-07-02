from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import re

router = APIRouter()

class ConditionRequest(BaseModel):
    text: str = ""
    tags: list[str] = []

@router.post('/map-condition')
def map_condition(data: ConditionRequest):
    text = data.text.lower()
    tags = data.tags

    conditions = [
        {
            "pattern": r"chảy dính|rạn|vàng",
            "tags": ["yellow", "sticky", "cracked"],
            "condition": "Chảy dính, rạn, vàng",
            "cause": "Lão hóa tự nhiên hoặc do khách hàng",
            "handling": "Miễn phí nếu lỗi nhà sản xuất; tính phí nếu do khách hàng"
        },
        {
            "pattern": r"nứt|rách",
            "tags": ["torn", "cracked"],
            "condition": "Nứt, rách",
            "cause": "Nhà sản xuất hoặc khách hàng",
            "handling": "Miễn phí nếu lỗi vận chuyển; tính phí nếu do khách hàng"
        },
        {
            "pattern": r"lún",
            "tags": ["sagging", "dent"],
            "condition": "Lún",
            "cause": "Nhà sản xuất hoặc khách hàng",
            "handling": "Tư vấn tiếp tục sử dụng hoặc thay vạt giường"
        },
        {
            "pattern": r"biến dạng|dư|thiếu",
            "tags": ["deformed", "oversized", "undersized"],
            "condition": "Biến dạng, dư, thiếu kích thước",
            "cause": "Nhà sản xuất hoặc khách hàng",
            "handling": "Miễn phí nếu lỗi nhà sản xuất; tính phí nếu do khách hàng"
        },
        {
            "pattern": r"đen|dơ|bụi",
            "tags": ["dirty", "dusty", "black"],
            "condition": "Đen, dơ, bụi",
            "cause": "Nhà sản xuất hoặc khách hàng",
            "handling": "Vệ sinh tính phí hoặc tư vấn tiếp tục sử dụng"
        },
        {
            "pattern": r"mùi hôi",
            "tags": ["smell", "odor"],
            "condition": "Có mùi hôi",
            "cause": "Nhà sản xuất hoặc khách hàng",
            "handling": "Vệ sinh tính phí hoặc tư vấn tiếp tục sử dụng"
        },
        {
            "pattern": r"độ cứng|độ mềm",
            "tags": ["hard", "soft"],
            "condition": "Độ cứng, mềm khác nhau",
            "cause": "Nhà sản xuất hoặc khách hàng",
            "handling": "Tư vấn tiếp tục sử dụng hoặc thay vật tư tính phí"
        },
        {
            "pattern": r"phồng|rộp|khuyết",
            "tags": ["bulging", "blistered"],
            "condition": "Phồng, rộp, khuyết",
            "cause": "Nhà sản xuất hoặc khách hàng",
            "handling": "Tư vấn tiếp tục sử dụng hoặc thay vật tư tính phí"
        },
        {
            "pattern": r"cong thành",
            "tags": ["bent", "curved"],
            "condition": "Cong thành",
            "cause": "Khách hàng",
            "handling": "Tư vấn tiếp tục sử dụng hoặc bảo hành tính phí"
        },
        {
            "pattern": r"lò xo kêu",
            "tags": ["spring", "noise"],
            "condition": "Lò xo kêu",
            "cause": "Khách hàng",
            "handling": "Bảo hành miễn phí (nếu còn thời hạn) hoặc tính phí"
        },
        {
            "pattern": r"kiến",
            "tags": ["ants", "insects"],
            "condition": "Có kiến",
            "cause": "Khách hàng",
            "handling": "Vệ sinh tính phí hoặc tư vấn tiếp tục sử dụng"
        },
        {
            "pattern": r"co rút",
            "tags": ["shrunk", "shrunken"],
            "condition": "Áo nệm co rút",
            "cause": "Khách hàng",
            "handling": "Mua áo nệm mới tính phí"
        },
        {
            "pattern": r"móp|mé",
            "tags": ["dented", "deformed"],
            "condition": "Góc nệm móp, méo",
            "cause": "Khách hàng",
            "handling": "Tư vấn tiếp tục sử dụng hoặc thay tấm mới tính phí"
        }
    ]

    for cond in conditions:
        text_match = re.search(cond["pattern"], text)
        tag_match = any(tag in tags for tag in cond["tags"])
        if text_match or tag_match:
            return {
                "condition": cond["condition"],
                "cause": cond["cause"],
                "handling": cond["handling"]
            }

    return JSONResponse(
        content={
            "condition": "Không xác định",
            "cause": "Không xác định",
            "handling": "Cần kiểm tra thêm"
        },
        status_code=400
    )