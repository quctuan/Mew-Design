# Thiết kế Luồng Trải nghiệm Người dùng (UX Flow)
**Tính năng**: Mua gói cước di động
**Người chịu trách nhiệm (Role)**: UX (UX Designer)
**Dựa trên**: UR Research (JTBD & Competitor Insights)

---

## 1. Nguyên tắc thiết kế (Design Principles)
- **Minh bạch (Transparency)**: Hiển thị rõ giá, chu kỳ gia hạn, và dung lượng quy đổi sang thói quen (TikTok, Web).
- **Tốc độ (Speed)**: Giảm thiểu chạm, ưu tiên gói cước cá nhân hóa ngay màn hình đầu.
- **An tâm (Trust)**: Cho phép bật/tắt tự động gia hạn ngay tại bước xác nhận mua.

---

## 2. Sơ đồ luồng UX (User Flow Chart)

```mermaid
graph TD
    %% Khởi đầu
    Start([Người dùng mở App My VNPT]) --> Home[Màn hình Trang chủ]
    
    %% Điểm chạm chính
    Home --> Shortcut{Hết Data?}
    Shortcut -- Có --> QuickBuy[Sticky Bar: 'Bạn sắp hết Data! Mua nhanh gói cứu trợ 1 ngày?']
    Shortcut -- Không --> DataSection[Khu vực Gói cước di động]
    
    %% Lựa chọn gói cước
    QuickBuy --> ReviewOrder
    DataSection --> SmartTier[Tab 1: Gợi ý cho bạn - 3 gói P0/P1/P2]
    DataSection --> BrowseTier[Tab 2: Tất cả các gói - Category: Ngày/Tháng/Combo]
    
    SmartTier --> SelectPlan[Chọn Gói cước phù hợp]
    BrowseTier --> SelectPlan
    
    %% Chi tiết & Quy đổi
    SelectPlan --> PlanDetail[Chi tiết Gói cước: <br/>- Giá/Ngày <br/>- Quy đổi: Xem được N giờ TikTok <br/>- Switch Tự động gia hạn]
    
    %% Thanh toán
    PlanDetail --> BuyBtn([Bấm Mua Ngay])
    BuyBtn --> PayMethod{Số dư tài khoản chính?}
    
    PayMethod -- Đủ tiền --> OneTapBuy[Nút Mua 1 Chạm: Chớp vân tay/FaceID]
    PayMethod -- Thiếu tiền --> ExternalPay[Phương thức khác: Apple Pay, Momo, ZaloPay]
    
    OneTapBuy --> Success[Màn hình Thành công: <br/>Hiệu ứng Celebration <br/>Đồng hồ đếm ngược dung lượng thực]
    ExternalPay --> Success
    
    %% Kết thúc
    Success --> BackToContext([Quay lại tác vụ đang dở dang lúc trước])
```
![alt text](image.png)
---

## 3. Mô tả các màn hình chính (Screens Breakdown)

### 3.1. Smart Selection (Màn hình Gợi ý)
- Thay vì danh sách 50 gói, UR Research đề xuất chỉ hiển thị 3 thẻ (Card) lớn:
    - **Gói 1 (Daily Fix):** Dành cho ai hay hết data dọc đường.
    - **Gói 2 (Social King):** Dành cho hệ người dùng xem YouTube/TikTok nhiều.
    - **Gói 3 (Economical Yearly):** Thuê bao muốn tiết kiệm dài hạn.

### 3.2. Plan Detail & Transparency (Độ minh bạch)
- Một thanh Switch **"Tự động gia hạn gói này"** nằm nổi bật ngay dưới nút Mua, mặc định theo thói quen người dùng nhưng không giấu giếm.
- Câu lệnh mô tả: *"Hệ thống sẽ cộng 2GB vào tài khoản. Tương đương với khoảng 4 tiếng xem video chất lượng cao."*

### 3.3. Celebration Success (Cảm xúc sau mua)
- Giai đoạn **Success** trong Design Thinking: Sau khi thanh toán xong, luồng không chỉ "thanh toán thành công" khô khan.
- Sẽ có hiệu ứng pháo hoa nhẹ và quan trọng nhất: Một **Widget thời gian thực** hiển thị: "Bạn đang có 2.00 GB/2.00 GB. Sẵn sàng lướt web!".

---
*Tài liệu này được lưu tại: `knowledge base/ux-design-output/ux/flow-buy-data-plan.md`*
