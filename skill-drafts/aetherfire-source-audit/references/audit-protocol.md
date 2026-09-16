# Quy trình đối chiếu AetherFire

Dùng reference này cho BOUNDED_AUDIT và FULL_AUDIT. Với LOOKUP, không nạp toàn bộ quy trình nếu câu hỏi đã trả lời được từ nguồn trực tiếp; chỉ ghi nguồn đã đọc và giới hạn.

## Nguồn và phạm vi

Ghi các file user yêu cầu và các nguồn phụ thuộc đã mở, vai trò, phạm vi quyền quyết định, trạng thái đọc đủ/thiếu. Đường dẫn và đề mục/dòng phải trỏ tới nội dung đã đọc. Có thể ghi SHA-256 để nhận biết bản bị đổi, nhưng hash không xác lập quyền canon.

Chỉ mở rộng sang nguồn trực tiếp cần để xác minh tham chiếu, định nghĩa hoặc hệ quả. Ghi lý do mở rộng. Nếu phải sang một mảng project khác hẳn phạm vi, hỏi trước; nếu không truy cập được nguồn, ghi UNKNOWN và giới hạn kiểm tra. Không dùng tìm kiếm không có kết quả làm bằng chứng phủ định canon.

## Các lượt rà nội dung

Trong `FULL_AUDIT`, đánh dấu đã kiểm/không áp dụng/chưa kiểm cho từng nhóm liên quan; nêu phần chưa kiểm và lý do. Trong `BOUNDED_AUDIT`, chỉ áp dụng các nhóm chạm trực tiếp target và phụ thuộc gần:

| Nhóm | Câu hỏi kiểm tra |
| --- | --- |
| Định nghĩa và đồng nhất | Cùng từ có đổi nghĩa? Hai thực thể/trục khác nhau bị nhập làm một? |
| Phạm vi và điều kiện | “Một số” thành “mọi”? Điều kiện bị mất? Ngoại lệ vô hiệu hóa quy tắc? |
| Chân trị và bằng chứng | Chưa xác lập bị viết thành không có? Yêu cầu/đề xuất bị viết thành dữ kiện? |
| Quan hệ và quyền hạn | Tương tác bị đổi thành sở hữu? Nguồn gốc bị đổi thành quản trị? Quyền quyết định và khả năng thực hiện bị nhập? |
| Chuyển trạng thái | Có đầu vào, điều kiện, tác nhân và đầu ra? Điều kiện cần có bị bỏ qua hoặc coi là đủ? |
| Thời gian/canon/POV | Khác biệt có cùng thời kỳ/lớp không? Nhân vật có biết điều chưa thể biết? |
| Nhân quả và phụ thuộc | Tiền đề mới làm kết luận cũ mất căn cứ? Có phụ thuộc vòng mà nguồn không cho điểm khởi đầu? |
| Số lượng/tài nguyên | Khi nguồn có số liệu: đơn vị, tổng, giới hạn, nguồn cấp và sức chứa có nhất quán? Không tự dựng số để kiểm. |
| Mất và thêm nội dung | Bản mới bỏ điều kiện/unknown/deferred nào? Có thêm khẳng định không có nguồn hoặc quyết định? |
| Thay thế phiên bản | Khác biệt đã được chốt thay thế hay là conflict còn mở? Bản cũ có bị dùng lại ngoài vai trò hợp lệ? |

So sánh theo mệnh đề và quan hệ, không chỉ từ khóa. Với thay đổi A → B, truy các kết luận thực sự phụ thuộc A và chỉ ra phần nào cần xem lại. Không mở vô hạn mọi suy đoán có thể có.

## Hồ sơ phát hiện

Mỗi phát hiện trong `BOUNDED_AUDIT`/`FULL_AUDIT` có ID ổn định, ví dụ AF-001. Với `LOOKUP`, chỉ tạo finding khi thật sự phát hiện conflict/unknown/logic issue cần theo dõi. Dùng bảng khi ngắn, từng mục khi dẫn chứng dài:

- Loại: CONFLICT / UNKNOWN / DEFERRED / LOGIC; một mục có thể mang nhiều loại.
- Trạng thái: OPEN / PROPOSED / DEFERRED / RESOLVED / SUPERSEDED.
- Nguồn cũ: đường dẫn, đề mục/dòng và trích đoạn đủ chứng minh.
- Nguồn mới: đường dẫn, đề mục/dòng và trích đoạn; nếu là bỏ sót, ghi mệnh đề mất và phạm vi đã kiểm thay vì bịa dòng chứng minh sự vắng mặt.
- Mệnh đề/vấn đề: hai phát biểu nào xung đột hoặc liên kết nào chưa xác lập.
- Điều kiện: đối tượng, nghĩa, thời kỳ/lớp canon và giả định cần để kết luận.
- Căn cứ và hệ quả: kết luận ngắn có thể kiểm chứng, phân biệt chắc chắn với nghi vấn.
- Quyền ưu tiên: quyết định nào cho phép thay thế; nếu thiếu, ghi chưa xác định.
- Xử lý: giữ, sửa, hỏi, hoãn hoặc thay thế; đề xuất và quyết định phải tách riêng.
- Phụ thuộc: vị trí khác cần cập nhật và ID liên quan.
- Đóng mục: quyết định đã chấp nhận và vị trí kiểm chứng trong file đầu ra mới. Nếu chưa có, chưa đóng.

Chỉ cần điền trường phù hợp nhưng không được bỏ nguồn và lý do kết luận. Một quyết định retcon đã xác nhận có thể tạo khác biệt lịch sử được ghi SUPERSEDED, không phải conflict hiện hành; vẫn lưu nguồn gốc. Một mục deferred có thể đồng thời là conflict chưa giải quyết.

## Hồ sơ chuyển mốc sau chốt

Đặt trong báo cáo đối chiếu hoặc phần metadata của bản chốt theo cấu trúc tài liệu; không bắt buộc tạo hệ thống quản lý mới. Hồ sơ tối thiểu gồm:

| Trường | Nội dung cần ghi |
| --- | --- |
| Quyết định chốt | Lượt/xác nhận có thể nhận diện và nội dung đã đồng ý; không suy từ tên file |
| Mốc tiền nhiệm | Đường dẫn và phạm vi bản cũ |
| Đầu vào được xét | Đường dẫn file đề xuất, phân biệt với đầu ra cuối |
| File chốt thực tế | Đường dẫn chính xác của từng file mới và nhận diện phiên bản; hash nếu hữu ích |
| Phạm vi thay thế | Phần nào chuyển mốc, phần nào vẫn dùng nguồn khác |
| Kiểm chứng đầu ra | Đã đọc lại file nào, đối chiếu quyết định nào, kết quả và giới hạn |
| Mục mang sang | ID OPEN/UNKNOWN/DEFERRED, căn cứ hoãn và điều kiện mở lại nếu có |
| Mốc lượt kế | Đường dẫn file mới đã kiểm chứng; chỉ ghi sau khi hoàn tất bước này |

Nếu chưa được phép ghi báo cáo/file, trình bày hồ sơ trong câu trả lời và chỉ rõ chưa có bản chốt trên ổ đĩa. Không bịa đường dẫn hoặc nói đã chuyển mốc sang file chưa tồn tại.
