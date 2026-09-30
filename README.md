> [!IMPORTANT]
> **LLM / agent readers:** Read [`SYSTEM_CONTEXT.md`](./SYSTEM_CONTEXT.md) **before** analyzing this repository's architecture, project relationships, or authoring workflow. This is a personal, non-commercial worldbuilding hobby ecosystem; its three fiction projects are independent paracosms, and repository-visible state is not the full live/runtime/internal state.

# ChatGPT CI Versioning Audit & Changelog

Kho lưu trữ này ghi lại quá trình thiết kế, kiểm toán và version hóa **Custom Instructions (CI) cho ChatGPT**. `CI` ở đây có nghĩa là *Custom Instructions*, không phải Continuous Integration.

Mục tiêu chính là lưu được cả lịch sử thay đổi lẫn lý do thiết kế: một rule xuất hiện để chặn failure mode nào, điều kiện nào kích hoạt nó, bản vá nào đã tạo hồi quy và kết quả nào mới chỉ đạt kiểm tra cấu trúc thay vì được chứng minh bằng hành vi thực tế.

## Cảnh báo: đây không phải bộ cài đặt

**Repo này không cài đặt, kích hoạt, chèn hoặc tự động áp dụng bất kỳ chỉ dẫn nào vào ChatGPT, tài khoản hay thiết bị.** Các file chỉ là văn bản nghiên cứu, phiên bản thử nghiệm và tài liệu tham khảo.

Không có phiên bản nào được bảo đảm phù hợp cho mọi model, sản phẩm, tài khoản hoặc cách sử dụng. Hành vi thực tế còn có thể chịu ảnh hưởng của model, system instructions, personality, memory, lịch sử hội thoại, giới hạn gói và thay đổi từ nền tảng.

Nếu sao chép, chỉnh sửa hoặc sử dụng bất kỳ CI nào trong repo, **người dùng tự chịu trách nhiệm và tự chấp nhận rủi ro**. Hãy đọc changelog, kiểm tra giới hạn ký tự, thử trong hội thoại có kiểm soát và giữ bản cũ để quay lại. Việc một file đạt kiểm tra độ dài, encoding hoặc cấu trúc không chứng minh model sẽ tuân thủ nó.

> **English notice:** This repository does not install or automatically apply any instructions. Its files are research artifacts and experimental configurations. Copy, adapt, or use them at your own risk.

## Repo chứa những gì?

- [`ChatGPT Plus+ Era`](./ChatGPT%20Plus+%20Era/) — các bản CI đầy đủ cho ngân sách ký tự lớn hơn; đây là nơi kiến trúc và guardrail thường được phát triển trước.
- [`ChatGPT Go-Free Era`](./ChatGPT%20Go-Free%20Era/) — các bản chưng cất cho ngân sách ngắn hơn, ưu tiên giữ semantics cốt lõi thay vì sao chép nguyên văn bản đầy đủ.
- [`CHANGELOG_VI.md`](./CHANGELOG_VI.md) và [`CHANGELOG.md`](./CHANGELOG.md) — lịch sử thay đổi bằng tiếng Việt và tiếng Anh.
- [`CI_VERSIONING_AUDIT_VI.md`](./CI_VERSIONING_AUDIT_VI.md) — kiểm toán lineage, thay đổi rule và regression qua các phiên bản.
- [`CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI.md`](./CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI.md) — triết lý kiến trúc và quan hệ giữa hai mục tiêu triển khai.
- [`CI_FAILURE_MODES_AND_CONTROL_MODEL_VI.md`](./CI_FAILURE_MODES_AND_CONTROL_MODEL_VI.md) — bản đồ `trigger → diễn giải sai → failure → control → rủi ro còn lại → phép thử`.
- [`Project CI`](./Project%20CI/) — CI chuyên biệt theo project. Chúng có phạm vi riêng và không mặc định được gộp vào global CI.
- [`AetherFire Project`](./AetherFire%20Project/) — dữ liệu và tài liệu hợp nhất của một project worldbuilding dùng cùng phương pháp kiểm soát phạm vi; không phải phần mặc định của global CI.

## Cách đọc trạng thái một phiên bản

Repo phân biệt rõ:

- **Kiểm tra cấu trúc:** độ dài, encoding, xuống dòng, phạm vi diff và sự hiện diện của rule.
- **Bằng chứng hành vi:** đầu ra quan sát được trong phép thử có kiểm soát.
- **Báo cáo của người dùng:** bằng chứng thực tế có giá trị, nhưng có thể chưa cô lập hết model, cấu hình, memory và lịch sử chat.
- **Rủi ro hồi quy:** đường dẫn thất bại hợp lý từ câu chữ, chưa đồng nghĩa failure đã tái hiện.

Một version mới là một giả thuyết hành vi có thể kiểm thử, không phải tuyên bố rằng mọi model sẽ phản hồi giống nhau.

## Quy trình sử dụng được khuyến nghị

1. Đọc changelog và failure model trước khi chọn version.
2. Chỉ sao chép đúng file CI mà bạn chủ động muốn thử; không coi toàn repo là một gói cấu hình.
3. Giữ model, cài đặt, memory và prompt kiểm thử ổn định khi so sánh A/B.
4. Thử cả chat mới lẫn hội thoại dài vì một số failure chỉ xuất hiện khi ngữ cảnh tích lũy.
5. Lưu bản CI trước đó để có thể rollback ngay khi xuất hiện hồi quy.

## Tính độc lập và giới hạn

Đây là repo nghiên cứu cá nhân, không phải dự án chính thức của OpenAI và không đại diện cho bảo đảm của ChatGPT. Tài liệu giải thích thiết kế không tự động có hiệu lực như instructions; chỉ nội dung thực sự được người dùng đưa vào trường Custom Instructions mới trở thành một phần của cấu hình do người dùng kiểm soát, trong phạm vi nền tảng cho phép.
