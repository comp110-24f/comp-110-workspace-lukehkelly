"""Examples of dictionary syntax with Ice Cream Ship order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

print(len(ice_cream))

ice_cream["mint"] = 10

mint_orders: int = ice_cream["mint"]
print(mint_orders)

ice_cream["mint"] += 1

ice_cream.pop("strawberry")
