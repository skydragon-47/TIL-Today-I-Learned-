
# 상품 기본 정보 변수 선언
milk_name = "우유"
milk_price = 2300
milk_qty = 2

bread_name = "빵"
bread_price = 1800
bread_qty = 1

egg_name = "계란"
egg_price = 5200
egg_qty = 1

# 아이템 딕셔너리 설정
item_milk = {
    "name": milk_name,
    "price": milk_price,
    "qty": milk_qty
}

item_bread = {
    "name": bread_name,
    "price": bread_price,
    "qty": bread_qty
}

item_egg = {
    "name": egg_name,
    "price": egg_price,
    "qty": egg_qty
}

# 카트에 담기
cart = [item_milk, item_bread, item_egg]

# 총합 계산
milk_total = cart[0]["price"] * cart[0]["qty"]
bread_total = cart[1]["price"] * cart[1]["qty"]
egg_total = cart[2]["price"] * cart[2]["qty"]

subtotal = milk_total + bread_total + egg_total

# 배송비 및 최종 결제 금액
delivery_fee = 3000
final_total = subtotal + delivery_fee

# 평균 가격 계산
avg_price = subtotal / (
    cart[0]["qty"] + cart[1]["qty"] + cart[2]["qty"]
)

# 할인 여부 계산
has_discount = (final_total >= 10000)

# 문자열 포매팅
summary = (
    f"장바구니: {cart[0]['name']} {cart[0]['qty']}개, "
    f"{cart[1]['name']} {cart[1]['qty']}개, "
    f"{cart[2]['name']} {cart[2]['qty']}개 | "
    f"상품합계 {subtotal}원 | "
    f"배송비 {delivery_fee}원 | "
    f"최종 {final_total}원 | "
    f"할인대상 {has_discount}"
)

print(summary)
