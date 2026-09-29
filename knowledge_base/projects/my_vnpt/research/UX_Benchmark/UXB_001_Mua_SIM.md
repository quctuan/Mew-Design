# Báo cáo UX Benchmark: Luồng mua SIM (Đối thủ cạnh tranh My VNPT)

## 1. Mục tiêu
Nghiên cứu, đánh giá và học hỏi trải nghiệm người dùng (UX) trong **Luồng mua SIM (vật lý & eSIM)** từ các đối thủ cạnh tranh trực tiếp của My VNPT tại thị trường Việt Nam (Viettel, Mobifone) cũng như các best practice quốc tế (VD: Singtel GOMO). 
Mục đích chính là tìm ra cách giảm thiểu ma sát (friction) trong quá trình onboarding, đặc biệt là khâu định danh điện tử (eKYC) và lựa chọn gói cước, nhằm tăng tỷ lệ chuyển đổi (conversion rate) cho ứng dụng My VNPT.

## 2. Giải pháp tham khảo trên thị trường
Việc mua SIM hiện nay đang chuyển dịch mạnh mẽ từ mô hình "đại lý vật lý" sang "digital-first" (thuần số).

*   **Viettel (My Viettel):** 
    *   *Giải pháp:* Cho phép người dùng mua SIM vật lý (giao tận nhà) hoặc eSIM trực tiếp trên app. Tích hợp sâu kho số đẹp, số phong thủy. 
    *   *Nhược điểm:* App tích hợp quá nhiều dịch vụ (ViettelPay, Viettel++...) đôi khi gây rối rắm cho luồng mua SIM cơ bản. Quy trình eKYC đôi lúc vẫn yêu cầu ra quầy nếu giấy tờ không khớp.
*   **Mobifone (My Mobifone):** 
    *   *Giải pháp:* Đẩy mạnh số hóa thủ tục hành chính, cho phép đăng ký thông tin thuê bao qua app.
    *   *Nhược điểm:* Trải nghiệm eKYC chưa thực sự mượt mà, nhiều người dùng phàn nàn về việc app bị crash hoặc bắt chụp lại CCCD nhiều lần.
*   **Singtel / GOMO (Singapore):**
    *   *Giải pháp (Best Practice):* GOMO là thương hiệu thuần số của Singtel. Trải nghiệm mua eSIM cực kỳ mượt mà nhờ tích hợp thẳng với hệ thống định danh quốc gia (SingPass). Khách hàng mua và kích hoạt eSIM chỉ trong chưa đầy 3 phút mà không cần scan giấy tờ thủ công.

## 3. Phân tích Flow step-by-step (Luồng chuẩn)
Một luồng mua SIM tối ưu (Digital-first) thường bao gồm các bước sau:

1.  **Khám phá & Chọn gói cước (Plan Selection):** 
    *   Hiển thị dạng thẻ (Cards) dễ so sánh các thông số: Data, Phút gọi nội/ngoại mạng, Giá cước. Có highlight gói "Phổ biến nhất".
2.  **Lựa chọn loại SIM & Số (SIM Type & Number):** 
    *   *Loại SIM:* Tùy chọn SIM vật lý (nhập địa chỉ giao hàng) hoặc eSIM (nhận mã QR qua email/app).
    *   *Chọn số:* Cho phép tìm kiếm số theo đuôi năm sinh, số may mắn.
3.  **Định danh điện tử (eKYC):** 
    *   Chụp ảnh mặt trước/sau CCCD. Hệ thống tự động OCR điền thông tin (Không bắt người dùng nhập tay).
    *   Quét khuôn mặt (Liveness Check) để đối chiếu.
4.  **Thanh toán (Checkout):** 
    *   Hiển thị minh bạch tổng tiền (giá SIM + giá gói cước + phí ship nếu có). Hỗ trợ thanh toán qua Ví điện tử (VNPay, Momo), thẻ tín dụng.
5.  **Hoàn tất & Theo dõi (Confirmation):** 
    *   Hiển thị màn hình Tracking giao hàng (với SIM vật lý) hoặc nút "Cài đặt eSIM ngay" (với eSIM).

## 4. Links Video/UI tham khảo
Dưới đây là các tài liệu và luồng UI tham khảo được thu thập:

### UI Flow & Visuals (Thiết kế luồng)
1. **[Mobbin - Telecom Onboarding Flows]**: Phân tích các màn hình chọn gói cước và eKYC của các nhà mạng lớn trên thế giới. Giúp học hỏi cách thiết kế Progressive Disclosure (Hiển thị thông tin tăng dần).
   *(Search keywords trên Mobbin: "SIM purchase", "Setting up", "Subscribing")*
2. **[Dribbble - eSIM Activation Concept]**: Các concept UI hiện đại cho bước quét QR eSIM, sử dụng animation để hướng dẫn người dùng cài đặt.

### Articles & Research (Bài viết phân tích)
3. **[UX Best Practices for Telecom (Lollypop Design)]**: Bài viết phân tích tầm quan trọng của việc giảm thiểu các bước nhập liệu form và sử dụng công nghệ OCR trong eKYC.
4. **[Digital Transformation in Telecom (Medium)]**: Báo cáo về cách các sub-brand (như GOMO) tách biệt luồng mua sắm khỏi ứng dụng gốc để tạo trải nghiệm "frictionless" (không ma sát).

## 5. Đề xuất / Key Takeaways cho hệ thống VNPT

### ✅ Nên làm (Do's):
*   **Tối giản hóa màn hình chọn gói:** Không hiển thị quá nhiều text dài dòng. Sử dụng Icon và Typography lớn để nổi bật dung lượng Data và Giá tiền.
*   **Tối ưu hóa eKYC (Trải nghiệm lõi):** Tích hợp công nghệ OCR tốt nhất có thể. Nếu quét thành công, auto-fill toàn bộ form. Cho phép người dùng chỉnh sửa nhanh nếu OCR nhận diện sai 1-2 ký tự, thay vì bắt chụp lại từ đầu.
*   **eSIM Instant Activation:** Với người dùng chọn eSIM, cung cấp nút "Thêm vào máy" (Add to Cellular Plan) trực tiếp bằng API của iOS/Android thay vì chỉ gửi ảnh QR code qua email.
*   **Progressive Disclosure:** Luôn có thanh tiến trình (Progress Bar: 1/4, 2/4...) để người dùng biết họ đang ở bước nào và sắp xong chưa.

### ❌ Không nên làm (Don'ts):
*   **Bắt buộc Đăng nhập/Tạo tài khoản sớm:** Cho phép người dùng (Guest) xem gói cước và chọn số thoải mái. Chỉ yêu cầu đăng nhập/nhập thông tin cá nhân ở bước eKYC và Thanh toán.
*   **Nhồi nhét quảng cáo:** Tuyệt đối không chèn các banner quảng cáo dịch vụ chéo (cross-sell) vào giữa luồng thanh toán hoặc eKYC làm đứt đoạn sự tập trung của khách hàng.
*   **Báo lỗi chung chung:** Tại bước eKYC, nếu ảnh bị lóa, hãy báo chính xác: "Ảnh CCCD bị lóa góc phải, vui lòng chụp lại", đừng báo "Hệ thống lỗi".
