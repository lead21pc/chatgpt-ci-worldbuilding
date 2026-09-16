# Ca review skill

Các ký hiệu A/B/C và quy tắc dưới đây là dữ liệu giả để thử quy trình, không phải lore AetherFire. Đây chưa phải kết quả chạy model. Đánh giá theo đầu ra và nguồn thực tế, không chấm chỉ bằng việc nhắc lại nhãn.

1. **Đọc lại mỗi lượt.** User chỉ định A.md và B.md; giữa hai lượt nội dung B thay đổi. Đạt khi đọc lại cả hai và dùng nội dung mới. Không đạt nếu chỉ dựa vào tóm tắt trước.
2. **Nguồn bị cắt/thiếu.** B chỉ đọc được phần đầu. Đạt khi đọc tiếp hoặc báo phần chưa đọc, không chứng nhận toàn bộ không conflict.
3. **Conflict thực sự.** A cho phép thao tác P trong điều kiện X; B cấm P trong chính điều kiện X. Đạt khi dẫn hai vị trí, xác định cùng phạm vi và báo mâu thuẫn; không tự ưu tiên B do tên mới hơn.
4. **Khác thời kỳ.** A nói quy tắc có hiệu lực trước T; B mô tả sau một thay đổi đã được chốt tại T. Đạt khi ghi thay thế lịch sử, không thổi phồng thành conflict hiện hành.
5. **Unknown không phải phủ định.** A không xác lập ánh xạ giữa hai trục; B viết hai trục không bao giờ kết hợp. Đạt khi phát hiện bước phủ định thiếu căn cứ, không tự khẳng định chúng kết hợp được.
6. **Hoãn chưa phải giải quyết.** User hoãn một conflict về P; B mới xóa nó khỏi danh sách. Đạt khi giữ ID, tình trạng conflict còn tồn tại và quyết định hoãn; không đánh dấu RESOLVED.
7. **Hệ quả gián tiếp.** B bỏ điều kiện X của P, nhưng kết luận Q trong file liên quan vẫn dựa vào X. Đạt khi truy đúng phụ thuộc và báo Q cần xem lại, không chỉ báo diff ở P.
8. **Bao phủ hai chiều.** B vừa thêm một quyền hạn chưa có nguồn vừa làm mất ngoại lệ của A. Đạt khi báo cả phần thêm và phần mất. Với nhiều lỗi độc lập, không dừng ở top 5; có thể gộp biểu hiện trùng nguyên nhân và giữ đủ vị trí.
9. **Kiểm chính file tạo sau chốt.** A là mốc, B là đề xuất; user chỉ chốt một phần B để tạo C. C thực tế vô tình chứa phần B chưa được chốt. Đạt khi đọc lại C, đối chiếu quyết định và phát hiện phần thêm; không dùng audit B làm chứng nhận cho C.
10. **Không dùng nhầm mốc cũ.** Sau khi C đã được tạo, kiểm và chốt, user đưa D. Đạt khi đọc C và D, dùng C làm mốc; A/B chỉ là lịch sử hoặc nguồn còn hiệu lực ngoài phạm vi thay thế. Nếu C không truy cập được, báo thiếu nguồn thay vì âm thầm quay về A.
11. **Chốt theo phạm vi.** User chốt thay đổi ở file kinh tế, chưa chốt file thời gian. Đạt khi chuyển mốc cho kinh tế và giữ mốc còn hiệu lực cho thời gian; không áp quyết định lên toàn project.
12. **Retcon có thẩm quyền.** User xác nhận B thay A cho quy tắc P. Đạt khi ghi SUPERSEDED cho khác biệt đã giải quyết, giữ nguồn gốc và kiểm các hệ quả phụ thuộc; không tiếp tục báo P như conflict đang mở.
13. **CI không phải nguồn lore.** Một file điều hướng hành vi chứa ví dụ khác bản canon đã chốt. Đạt khi phân biệt vai trò, có thể báo hướng dẫn lệch nguồn nhưng không sửa canon để khớp ví dụ.
14. **Chỉ audit.** User yêu cầu kiểm tra, chưa cho sửa. Đạt khi xuất phát hiện và đề xuất; nguồn giữ nguyên. Đồng ý một cách xử lý sau đó chỉ cho phép thực hiện đúng phần đã chốt.
15. **Bản chốt có câu hỏi mở.** User chấp nhận C với một unknown và một conflict được hoãn. Đạt khi C/hồ sơ giữ cả hai, không đưa một nhánh còn tranh chấp thành tiền đề chắc chắn và không tuyên bố mọi mâu thuẫn đã hết.
16. **Chống kết luận logic giả.** Nguồn có hai lớp canon hoặc cơ chế hư cấu khác đời thực. Đạt khi kiểm theo quy tắc nội tại và phạm vi nguồn, không tự coi sự khác đời thực là lỗi hoặc dùng genealogy suy ra sở hữu hiện tại.
17. **Nhận diện package trước khi chọn mốc.** User chỉ định thư mục AetherFire Project có index, manifest, reconciliation record, build script và Source_Archive. Đạt khi đọc metadata điều phối trước, phân loại input/output/excluded source rồi mới chọn file canon liên quan; không coi mọi file root hoặc tên `CURRENT` là bằng chứng đủ về quyền ưu tiên.
18. **Không sửa generated output trực tiếp.** User chốt một thay đổi cho file `*_CURRENT.md`, nhưng file đó do build script sinh. Đạt khi biểu diễn thay đổi trong nguồn mới được bảo toàn và/hoặc logic build/reconciliation đã duyệt rồi regenerate; không vá trực tiếp output để thay đổi biến mất ở lần build sau.
19. **Fresh deterministic verification.** Sau cập nhật package, generated Markdown đọc có vẻ đúng nhưng manifest cũ hoặc rebuild cho byte khác. Đạt khi không báo hoàn tất, dẫn mismatch, kiểm phạm vi thay đổi và chỉ chuyển mốc sau khi manifest cùng rebuild cô lập đều khớp và audit ngữ nghĩa đạt.
20. **Nguồn excluded vẫn excluded.** Một file anti-drift hoặc provenance-only nằm trong Source_Archive nhưng index/manifest ghi không import. Đạt khi archive presence không bị hiểu thành canon input và build không nhập file đó nếu chưa có quyết định rõ; nếu user chốt đổi phạm vi, ghi quyết định rồi cập nhật package và reconciliation tương ứng.
