---
name: Web Benchmark Skill
description: Hướng dẫn chi tiết cách tìm kiếm, tóm tắt và tổng hợp dữ liệu UX Benchmark từ đa nguồn web.
---

# 🌐 Skill: Kỹ năng Khảo sát và Phân tích UX Benchmark từ Web (`/web-benchmark`)

Skill này định nghĩa cách Agent tìm kiếm, chọn lọc và phân tích dữ liệu thị trường để tạo ra một bản UX Benchmark chất lượng cao.

## 1. Nguyên tắc Tìm kiếm (Search Principles)
- **Tự động dịch thuật:** Luôn luôn dịch các keyword trọng tâm từ Tiếng Việt sang Tiếng Anh để có được nguồn tài liệu chất lượng và phong phú nhất trên thế giới. (Ví dụ: "chuyển tiền nhanh" -> "fast money transfer UX flow").
- **Tư duy từ khóa đa chiều:** Sử dụng tổ hợp các keyword: 
  - `[Feature] + UX case study`
  - `[Feature] + UI flow Mobbin / Behance / Dribbble`
  - `Best practices for + [User Problem]`
  - `[App name] + [Feature] + review / teardown`
- **Mở rộng phạm vi:** KHÔNG giới hạn trong cùng lĩnh vực (domain). Nếu bài toán là "Gamification cho ứng dụng viễn thông", hãy thoải mái tham khảo từ Duolingo, Shopee, hoặc Starbucks.

## 2. Các Nhóm Nguồn bắt buộc phải quét
Khi thực hiện khảo sát, Agent PHẢI tìm đa dạng từ cả 3 nhóm sau:

**Nhóm 1: Articles / Research Reports (Kiến thức nền & Insight)**
- *Nguồn tiêu biểu:* Medium (UX Collective, Bootcamp), NN/g (Nielsen Norman Group), Smashing Magazine.
- *Mục tiêu:* Tìm kiếm ít nhất 3 bài phân tích sâu, các research report nói về cách giải quyết pain-point đó.

**Nhóm 2: UI Flow / Visual Layouts (Giao diện trực quan)**
- *Nguồn tiêu biểu:* Mobbin, Behance, Dribbble, UI8, Pinterest.
- *Mục tiêu:* Lấy link của ít nhất 3 luồng giao diện (User Flow) xuất sắc đang chạy trên thị trường thực.

**Nhóm 3: Video Demo / Review (Trải nghiệm thực tế)**
- *Nguồn tiêu biểu:* Youtube, Tiktok (sử dụng keyword như `"app [name] review"`, `"app [name] [feature] demo"`).
- *Mục tiêu:* Lấy URL và Title của ít nhất 3 video cho thấy tính năng đó hoạt động trơn tru trong thực tế. Kèm theo mô tả ngắn về giá trị của video đó.

*Số lượng giới hạn:* Thu thập **tối thiểu 3, tối đa 10** ví dụ cho MỖI NHÓM để giữ tài liệu cô đọng.

## 3. Khung phân tích Dữ liệu (Analysis Framework)
Khi đã có đủ data, Agent vận dụng framework sau để chắt lọc trước khi ghi vào báo cáo:
- **Nguyên lý gốc:** Giải pháp này đang dùng đòn bẩy tâm lý nào? (Ví dụ: Sự khẩn cấp, Phần thưởng định kỳ, Giảm thiểu Cognitive Load...).
- **Flow bóc tách (Step-by-step):** Tái tạo lại luồng các bước (A -> B -> C) mà các app đối thủ thường làm.
- **Pros & Cons:** Nêu nhanh MỘT ưu điểm và MỘT nhược điểm của luồng trải nghiệm này.

## 4. Tiêu chuẩn File Output
Kết quả trả về phải là một file Markdown lưu tại `/Users/Shared/Previously Relocated Items/Security/Documents/GDS-MyVNPT/knowledge base/research/UX_Benchmark/UXB_[ID]_[Tên_tính_năng].md` với cấu trúc sau:

```markdown
# 📊 UX Benchmark: [Tên Bài Toán / Tính Năng]

## 1. Tóm tắt Bối cảnh và Mục tiêu (Context & Goal)
- **Pain point / Yêu cầu gốc:** [Đoạn tóm tắt từ Bước 1 của quy trình]
- **Mục tiêu Benchmark:** [Kết quả kỳ vọng đạt được sau khi tham khảo thị trường]

## 2. Lý thuyết Tâm lý & Giải pháp trên thị trường
[Trình bày cơ chế chung mà các sản phẩm đang sử dụng để xử lý nỗi đau này]

## 3. Phân tích Flow tiêu biểu (Step-by-Step)
[Mô tả từ 1 đến 2 luồng thao tác xuất sắc nhất phân tích được, ghi rõ các bước 1 -> 2 -> 3]

## 4. Thư viện Links Tham Khảo (Cần chia nhóm)
### 4.1. Bài viết Phân tích chuyên sâu (Articles)
- [Tiêu đề bài viết](URL) - *1 câu tóm tắt insight*
- ...

### 4.2. Giao diện / Luồng UI (Mobbin/Behance...)
- [Tên App - Luồng thao tác](URL) - *1 câu nhận xét điểm hay của UI này*
- ...

### 4.3. Video Demo / Review (Youtube/Tiktok...)
- [Tên Video](URL) - *1 câu mô tả tính năng/cảm xúc mang lại*
- ...

## 5. Key Takeaways cho VNPT (Do & Don't)
- **Do (Nên làm):**
  - [Hành động 1]
  - [Hành động 2]
- **Don't (Tránh làm):**
  - [Hành động 1]
```
