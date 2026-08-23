def check_reorder(item):
    return item.count <= item.reorder_threshold

def generate_alert(item):
    return {
        "sku": item.sku,
        "message": f"Item {item.sku} is below threshold ({item.count}). Reorder recommended."
    }