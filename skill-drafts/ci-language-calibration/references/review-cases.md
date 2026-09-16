# Các ca review

Đây là tình huống và tiêu chí đánh giá, không phải kết quả thử nghiệm đã chạy. Khi thử hành vi, đánh giá lời giải thích có giúp hoàn thành yêu cầu không; không chấm chỉ bằng số thuật ngữ hoặc việc xuất hiện đúng câu mẫu.

## 1. Biết vài từ không có nghĩa biết toàn miền

Đầu vào: “Tôi gọi API để ghi database. Vì sao retry có thể tạo hai đơn hàng?”

Cần quan sát: giải thích việc gửi lại yêu cầu có thể tạo thêm đơn nếu hệ thống không nhận ra đó là cùng một thao tác. Có thể dùng “idempotency” nếu nối ngay với tác dụng trong ví dụ. Không lấy việc người dùng nói API/database làm bằng chứng họ hiểu idempotency.

Dấu hiệu chưa đạt: “Dùng idempotency key và deduplication” được coi là lời giải thích đủ chỉ vì các từ này phổ biến ở backend.

## 2. Từ thông dụng vẫn có thể che mất ý

Đầu vào: “Cache ở đây ảnh hưởng gì đến việc tôi vừa sửa mà màn hình chưa đổi?”

Cần quan sát: nối bản dữ liệu được giữ lại để dùng nhanh với việc màn hình có thể vẫn hiển thị bản cũ. Không chỉ dịch cache thành “bộ nhớ đệm” rồi tiếp tục dùng các khái niệm chưa nối nghĩa.

## 3. Định nghĩa đủ từ nhưng thiếu quan hệ

Đầu vào: “Bạn đã giải nghĩa cache, invalidation và consistency rồi, nhưng tôi vẫn không hiểu vì sao dữ liệu cũ xuất hiện.”

Cần quan sát: giải thích trình tự cụ thể: dữ liệu gốc thay đổi, bản được lưu để đọc nhanh chưa được cập nhật hoặc bỏ đi, lần đọc sau vẫn nhận bản cũ. Không mặc định người dùng cần thêm một bảng thuật ngữ.

## 4. Phản hồi làm thay đổi giả định

Đầu vào: “Đừng nói đây là từ kỹ thuật phổ biến. Tôi không hiểu câu đó.”

Cần quan sát: thừa nhận giả định về mức hiểu chưa có căn cứ và diễn đạt lại đúng đoạn bằng cơ chế/hệ quả cụ thể. Nếu không biết “câu đó” chỉ câu nào, hỏi xác định đoạn; không tranh luận định nghĩa jargon dump hoặc yêu cầu người dùng tự chứng minh họ không hiểu.

## 5. Không làm mất độ chính xác

Đầu vào: “Giải thích race condition trong thao tác kiểm tra số dư rồi trừ tiền.”

Cần quan sát: giữ chi tiết hai thao tác đồng thời có thể cùng đọc số dư cũ và cùng vượt qua kiểm tra trước khi cập nhật. Nếu dùng tên thuật ngữ, gắn nó với tình huống. Không rút thành “hệ thống bị lỗi vì chạy nhanh”.

## 6. Không giải thích thừa

Đầu vào: “Tôi hiểu idempotency: gửi lại cùng yêu cầu không tạo hiệu ứng bổ sung. Chỉ so sánh hai cách lưu key, giữ thuật ngữ.”

Cần quan sát: thực hiện so sánh theo yêu cầu, không giảng lại toàn bộ khái niệm. Vẫn giải thích một phân biệt mới nếu nó quan trọng và chưa có căn cứ cho rằng người dùng hiểu.

## 7. Không dịch hỏng định danh

Đầu vào: “Lỗi này liên quan gì tới header Idempotency-Key?”

Cần quan sát: giữ nguyên tên header để đối chiếu, giải thích vai trò bằng lời Việt phù hợp. Không đổi tên kỹ thuật trong lệnh hoặc ví dụ thực thi chỉ để tránh tiếng Anh.

## 8. Rút gọn mà không hạ ưu tiên ngôn ngữ

Đầu vào cho tác giả CI: “Rút gọn CI có rule bằng chứng, chiều sâu lập luận và không suy trình độ từ từ kỹ thuật. Giữ đủ ba yêu cầu trong giới hạn tôi cung cấp.”

Cần quan sát: bản cuối vẫn có cơ chế không suy rộng vốn từ và cách xử lý khi chưa rõ, bên cạnh bằng chứng và chiều sâu. Nếu giới hạn không đủ, báo xung đột. Không chỉ giữ “avoid jargon” rồi tuyên bố đã bảo toàn nghĩa.

## 9. Ngoại lệ vô hiệu hóa rule

CI cần audit: “Explain unfamiliar terms. Keep common technical terms without explanation. Avoid jargon.”

Cần quan sát: chỉ ra “common” không xác định theo người đọc và có thể tạo ngoại lệ rộng cho rule đầu. Đây là nguy cơ do câu chữ; chưa được gọi là hành vi lỗi đã tái hiện nếu chưa thử model.

## 10. Đúng phạm vi lựa chọn skill

Yêu cầu “Viết CI riêng để model không đánh đồng ngôn ngữ kỹ thuật của tôi với vốn từ toàn miền” phù hợp skill này. Yêu cầu “Sửa pipeline CI/CD” không phù hợp. Yêu cầu chỉ audit CI không cho phép sửa bản nguồn; yêu cầu bản nháp để review không cho phép cài vào bộ skill chung.
