---
name: artifact-source-archive
description: Tạo artifact mới bằng cách đối chiếu, sao chép hoặc thay thế file cũ; sau khi kiểm chứng bản mới, tự chuyển nguồn cũ vào source_archive trong phạm vi tác vụ, tìm thư mục không phân biệt hoa/thường. Nguồn đã lưu chỉ đọc và không được dùng lại nếu người dùng chưa yêu cầu cụ thể. Không kích hoạt cho tác vụ chỉ đọc, audit hoặc sửa tại chỗ không tạo bản thay thế.
---

# Lưu nguồn cũ sau khi tạo artifact mới

Áp dụng khi tạo artifact mới từ file cũ để đối chiếu, sao chép hoặc làm bản tiền nhiệm. Chuyển các file cũ thuộc tác vụ vào archive sau khi bản mới hoàn tất và được kiểm chứng; giữ bản mới ở vị trí làm việc. Chỉ dẫn cụ thể của người dùng về nguồn, đích và việc giữ bản cũ có ưu tiên cao hơn skill.

Skill này chỉ sở hữu thao tác lưu file, hash và tính chỉ đọc. Skill chuyên môn xác định nguồn nào được phép chuyển, ý nghĩa provenance/canon và quyết định thay thế; không suy canon từ archive. `project-git-workflow` sở hữu mọi thao tác Git và binding. Audit/planning chỉ đọc không chuyển file dù skill archive được chọn cùng lúc.

## Xác định nguồn và đích

- Ghi rõ file nguồn cũ, artifact mới, thư mục gốc của tác vụ và phạm vi bản mới thay thế. Không gom các file khác chỉ vì cùng thư mục hoặc có tên gần giống.
- Chỉ chuyển bản tiền nhiệm hoặc file tham chiếu cũ thuộc phạm vi lưu trữ đã yêu cầu. Không chuyển template, thư viện, asset hoặc nguồn dùng chung còn là phụ thuộc hoạt động của bản mới hay tác vụ khác. Nếu chưa rõ việc chuyển có làm mất nguồn đang cần hay không, giữ file và hỏi đúng phần chưa rõ.
- Tìm thư mục có tên bằng `source_archive` với phép so sánh không phân biệt hoa/thường. `Source_Archive`, `SOURCE_ARCHIVE` và `source_archive` là cùng một tên cho mục đích này; giữ nguyên cách viết của thư mục đang có.
- Bắt đầu từ thư mục chứa nguồn cũ, rồi xét từng thư mục cha đến thư mục gốc tác vụ đã xác định. Chỉ liệt kê tên thư mục con trực tiếp ở mỗi mức; dùng archive gần nhất. Không quét toàn máy hoặc đọc nội dung archive để tìm đích.
- Nếu không có archive trong phạm vi này, tạo `source_archive` cạnh nguồn cũ. Nếu có nhiều thư mục khớp ở cùng mức hoặc một file chiếm tên đó, báo và xác định đích trước khi chuyển; không tùy ý chọn hay ghi đè.
- Nếu nguồn đã nằm trong archive, giữ nguyên nó. Quyền đọc nguồn archive không tự cho phép sửa hoặc chuyển nó ra thành nguồn hoạt động.

## Tạo, kiểm chứng và chuyển

1. Đọc các nguồn đang được phép dùng; tạo bản mới ở đường dẫn khác, giữ nguyên file nguồn trong lúc tạo. Tuân thủ quy tắc Git của tác vụ khi có sửa repository.
2. Kiểm chứng artifact đã ghi ra đĩa: nội dung theo yêu cầu, định dạng mở được, các kiểm tra liên quan đạt, các liên kết hoặc phụ thuộc còn hoạt động. Nếu bản mới lỗi hoặc chưa hoàn tất, giữ nguyên vị trí nguồn cũ.
3. Sau khi kiểm chứng đạt, tự thực hiện lưu trữ trong phạm vi đã xác định; không hỏi lại quyền chuyển mà người dùng đã cấp qua quy tắc này. Kiểm tra tham chiếu hoạt động tới nguồn cũ trước khi chuyển; nếu việc sửa tham chiếu sẽ vượt phạm vi tác vụ, giữ nguồn và báo phần cần quyết định.
4. Giữ byte-exact nội dung nguồn cũ. Ghi SHA-256 trước chuyển và kiểm SHA-256 ở đích sau chuyển. Kiểm tra đường dẫn tuyệt đối đã resolve nằm trong nguồn/đích được phép; không đi qua symlink hoặc junction sang thư mục ngoài phạm vi.
5. Không ghi đè file archive trùng tên. Nếu tên đích đã tồn tại, tạo tên không trùng bằng hậu tố thời gian và bộ đếm khi cần; giữ phần mở rộng. Không tự xóa hay gộp bản đã có, kể cả hash giống nhau.
6. Chỉ bỏ bản cũ khỏi vị trí làm việc sau khi bản archive được xác nhận đúng hash. Dùng thao tác file với đường dẫn literal; nếu thao tác thất bại, giữ các bản còn lại và báo trạng thái thực tế. Không xóa thư mục nguồn hoặc file không thuộc tác vụ.
7. Kiểm lại artifact mới và tham chiếu chịu ảnh hưởng sau chuyển. Báo đường dẫn bản mới, nguồn đã chuyển, đích archive, kết quả kiểm chứng và phần còn bị chặn nếu có.

## Archive chỉ đọc và không hoạt động

- Đây là ranh giới hành vi, không phải yêu cầu đổi ACL hay thuộc tính read-only của hệ điều hành. Cho phép thêm nguồn cũ mới vào archive theo quy trình trên; không sửa, chuẩn hóa, đổi tên hoặc xóa các file đã lưu trước đó nếu chưa có yêu cầu rõ.
- Không dùng nội dung archive làm nguồn mặc định, fallback, tiền đề, mốc hiện hành, đầu vào build hoặc căn cứ khôi phục nội dung đã thay thế. Không tự đọc lại nó ở lượt sau; việc bản mới thiếu dữ kiện không mở quyền dùng archive.
- Chỉ đọc hoặc sử dụng nguồn archive khi người dùng chỉ định rõ file, nhóm nguồn hoặc phạm vi lịch sử cần đối chiếu/khôi phục. Yêu cầu chung như “tiếp tục”, “kiểm tra lại” hoặc “tạo bản mới” không tự cấp quyền dùng archive.
- Yêu cầu đối chiếu lịch sử chỉ cấp quyền trong tác vụ đó; không tái kích hoạt bản cũ. Chỉ khôi phục nó thành nguồn hoạt động khi người dùng yêu cầu rõ việc khôi phục và phạm vi thay thế.
- Khi cần dữ kiện chỉ có trong archive nhưng chưa có quyền sử dụng, nêu dữ kiện còn thiếu và hỏi quyền cho đúng nguồn; không âm thầm dùng trí nhớ của nguồn cũ để vượt ranh giới này.
