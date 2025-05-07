from app import app # Hoặc nơi bạn khởi tạo Flask app và db
from models_db import db, User # Import db và model của bạn

with app.app_context(): # Cần app context để truy cập db
    all_users = User.query.all()
    if not all_users:
        print("Không tìm thấy user nào.")
    else:
        print(f"Tìm thấy {len(all_users)} user(s):")
        for user in all_users:
            # In ra các thuộc tính bạn muốn xem
            print(f" - ID: {user.id}, Username: {user.username}, Email: {user.email}")

    # Bạn có thể truy vấn các bảng khác tương tự
    # all_products = Product.query.all()
    # for product in all_products:
    #    print(product)