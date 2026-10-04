---
name: ci-language-calibration
description: Soạn, sửa, rút gọn hoặc audit Custom Instructions (CI) có yêu cầu về ngôn ngữ, jargon và mức hiểu của người đọc; bảo toàn các yêu cầu này ngang hàng với yêu cầu reasoning. Không dùng cho CI/CD hoặc tự động áp lên mọi câu trả lời thông thường.
---

# CI language calibration

## Mục tiêu và phạm vi

Khi thiết kế Custom Instructions, xem khả năng người dùng theo được lời giải thích là điều kiện chấp nhận độc lập, ngang hàng với tính đúng đắn, bằng chứng và chất lượng lập luận. Một bản CI bảo toàn reasoning nhưng làm mất yêu cầu ngôn ngữ vẫn chưa đạt. Ngang hàng không có nghĩa ưu tiên sự dễ đọc hơn tính chính xác hoặc chia đều số ký tự cho các nhóm rule.

Skill này hướng dẫn tác giả CI; hành vi mong muốn ở model đích phải được viết thành rule trong CI. Không giả định model đích có quyền truy cập skill này. Không cài skill, sửa CI khác hoặc cập nhật bộ skill chung ngoài phạm vi được người dùng yêu cầu. Với yêu cầu chỉ audit, báo phát hiện và đề xuất, không sửa file.

## Căn cứ để đánh giá người đọc

- Phân biệt độ phổ biến của thuật ngữ trong một miền với bằng chứng người dùng hiểu khái niệm cụ thể đó. Độ phổ biến có thể giúp chọn cách gọi, không đủ để kết luận không cần giải thích.
- Không suy rộng từ nghề nghiệp, cách nói kỹ thuật, một vài thuật ngữ người dùng sử dụng, hoặc việc họ không hỏi lại sang vốn hiểu biết của toàn miền. Việc trích dẫn từ trong log hoặc câu trả lời trước cũng không chứng minh họ hiểu từ đó.
- Dựa vào chỉ dẫn trực tiếp và cách người dùng giải thích hoặc vận dụng khái niệm trong ngữ cảnh. Bằng chứng hiểu một khái niệm chỉ hỗ trợ giả định tương ứng, không phải một nhãn trình độ cố định.
- Khi chưa rõ, dùng câu giải thích ngắn tại nơi khái niệm ảnh hưởng đến ý nghĩa hoặc quyết định; không mặc định người dùng là người mới và không hỏi trình độ liên tục. Chỉ hỏi khi sự khác biệt về đối tượng đọc sẽ làm thay đổi đáng kể bản CI và ngữ cảnh chưa đủ.

## Biến yêu cầu thành rule có thể kiểm tra

Đọc yêu cầu, CI nguồn và các ví dụ được cung cấp. Phân biệt điều người dùng đã nêu với giả thuyết của tác giả; không tự áp một định nghĩa cố định về “jargon dump”. Ghi lại ngắn gọn vấn đề, hành vi cần có và điều phải tránh khi sửa. Không đòi hỏi người dùng định nghĩa đầy đủ thuật ngữ này trước khi có thể giúp.

Khi có liên quan đến yêu cầu, viết rule để model đích:

1. Kiểm tra căn cứ cho giả định người đọc hiểu một từ hoặc khái niệm quan trọng; không miễn giải thích chỉ vì nó “phổ biến trong kỹ thuật”.
2. Chọn giữ thuật ngữ, giải thích tại chỗ hoặc dùng diễn đạt thông thường theo độ chính xác và nhu cầu trong ngữ cảnh. Không dịch máy móc mọi từ sang tiếng Việt. Giữ đúng tên API, định danh, lệnh và nhãn cần đối chiếu.
3. Nêu ý nghĩa trong tình huống đang bàn và nối các ý thành lời giải thích. Mở rộng chữ viết tắt, thêm ngoặc định nghĩa hoặc liệt kê một bảng từ vựng chưa đủ nếu người đọc vẫn phải tự suy ra quan hệ, nguyên nhân hoặc hệ quả.
4. Giữ chiều sâu lập luận, điều kiện và các phân biệt cần thiết. Giảm gánh nặng ngôn ngữ bằng cách giải thích rõ, không bằng cách cắt mất nội dung quyết định kết luận.
5. Khi người dùng báo khó hiểu hoặc jargon dump, xem lại cả lựa chọn từ, mật độ khái niệm, các bước nối ý và giả định về người đọc. Dùng phản hồi cụ thể để sửa lời giải thích; không bảo vệ bản cũ bằng lý do thuật ngữ thông dụng. Nếu nguyên nhân chưa rõ, phân biệt giả thuyết với kết luận và chỉ hỏi phần còn cần thiết.
6. Tránh giải thích lại những khái niệm người dùng đã thể hiện hiểu hoặc yêu cầu giữ nguyên, trừ khi nghĩa đang dùng khác hoặc có dấu hiệu hiểu lệch. Không biến rule thành nghĩa vụ định nghĩa mọi từ ở mọi lượt.

Không yêu cầu model công khai chuỗi suy nghĩ nội bộ. Có thể yêu cầu kết quả kiểm tra, căn cứ ngắn gọn và bản diễn đạt đã sửa.

## Khi sửa hoặc rút gọn CI

Xác định các ràng buộc ngôn ngữ và reasoning cần bảo toàn trước khi nén. Kiểm tra tương tác với rule brevity, technical terminology, depth và audience; một rule “giữ từ phổ biến” không được vô hiệu hóa yêu cầu cân nhắc người đọc.

Nén ví dụ, tiêu đề và câu trùng trước khi làm yếu điều kiện hoặc ngoại lệ. Không thay toàn bộ cơ chế bằng “tránh jargon”, “viết rõ ràng” hoặc “định nghĩa thuật ngữ lần đầu”. Không mặc định dành ngân sách cho reasoning rồi coi ngôn ngữ là phần có thể bỏ.

Nếu có giới hạn ký tự/byte hoặc yêu cầu bảo toàn nguyên văn, kiểm tra đúng đơn vị và định dạng được yêu cầu. Nếu không thể đáp ứng đồng thời các ràng buộc, nêu xung đột và đưa phương án để người dùng chọn; không âm thầm hạ ưu tiên một nhóm. Không nhập giới hạn của phiên bản CI khác vào tác vụ hiện tại.

## Kiểm tra và bàn giao

Đọc [các ca kiểm tra](references/review-cases.md) khi review bản CI hoàn chỉnh hoặc sửa cơ chế của skill. Chọn các ca đúng phạm vi, gồm cả trường hợp cần giải thích và trường hợp không nên giải thích thừa.

Đối chiếu từng yêu cầu quan trọng với câu rule thực sự có trong bản cuối và tìm ngoại lệ có thể vô hiệu hóa nó. Báo ngắn gọn: yêu cầu nào được bảo toàn, xung đột nào còn lại, đã kiểm tra cấu trúc hay đã thử hành vi thực tế. Với phát hiện, chỉ ra câu chữ → tình huống kích hoạt → cách hiểu có thể xảy ra → hệ quả; không gọi một khả năng là lỗi hành vi đã được chứng minh.

Nếu thử hành vi, dùng cùng tình huống đầu vào và ghi lại CI, model/cấu hình có thể xác định cùng đầu ra quan sát được. Một bản CI qua kiểm tra câu chữ không chứng minh model sẽ tuân thủ. Không tự tổ chức thử nghiệm bên ngoài phạm vi hoặc công bố PASS hành vi khi chưa chạy.
