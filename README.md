# Mezon FunBox

## 1. Ý tưởng 
Tên bot: Mezon FunBox.
Mục tiêu: Tạo ra một trợ lý vui vẻ, cung cấp các nội dung ngẫu nhiên giúp người dùng thư giãn, truyền cảm hứng và tạo động lực học tập/làm việc ngay trên nền tảng Mezon. Bot mang tính giải trí, thư giãn và tạo không khí tích cực.

## 2. Logic hoạt động
Bot hoạt động theo quy trình sau:
1. Người dùng nhập một lệnh (ví dụ: /joke) trên Mezon.
2. Mezon gửi yêu cầu đến API server của bot thông qua webhook.
3. Bot nhận yêu cầu và phân tích lệnh.
4. Dựa trên lệnh, bot lấy ngẫu nhiên nội dung tương ứng từ một danh sách có sẵn.
5. Bot trả kết quả về cho Mezon để hiển thị ngay trên khung chat.

## 3. Cách sử dụng
Để tương tác với bot, bạn có thể sử dụng các lệnh sau:

| Lệnh | Mô tả |
|---|---|
| /quote | Random một câu trích dẫn truyền cảm hứng |
| /joke | Random một câu đùa vui nhẹ nhàng |
| /funfact | Random một sự thật thú vị |
| /challenge | Random một thử thách học tập hoặc công việc nhỏ trong ngày |
| /lucky | Random lời tiên tri may mắn hôm nay |

## 4. Công nghệ sử dụng
- Ngôn ngữ: Python 3.10+ 
- Framework: FastAPI 
- Nền tảng triển khai: Render/Railway 

## 5. Cài đặt và Chạy

### Yêu cầu hệ thống
- Python 3.10 trở lên
- pip (Python package manager)

### Các bước cài đặt

1. Clone repository:
```bash
git clone <repository-url>
cd mezon-funbox
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

3. Chạy ứng dụng:
```bash
uvicorn main:app --reload
```

Ứng dụng sẽ chạy tại `http://localhost:8000`

### Cấu trúc dự án
```
mezon-funbox/
├── main.py           # File chính chứa logic xử lý webhook
├── content.py        # Chứa các danh sách nội dung
├── requirements.txt  # Danh sách các thư viện cần thiết
└── README.md        # Tài liệu hướng dẫn
```

## 6. API Endpoints

### GET /
- Kiểm tra trạng thái hoạt động của server
- Response: `{"message": "Mezon FunBox is running!"}`

### POST /webhook
- Endpoint chính để nhận lệnh từ Mezon
- Request body: `{"text": "/command"}`
- Response: `{"text": "nội dung phản hồi"}`

## 7. Đóng góp
Mọi đóng góp đều được hoan nghênh! Vui lòng tạo issue hoặc pull request để đóng góp.

## 8. Giấy phép
Dự án này được phát hành dưới giấy phép MIT. 