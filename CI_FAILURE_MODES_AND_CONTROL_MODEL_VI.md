# Bản đồ Failure Mode và Mô hình Kiểm soát CI

## 0. Vai trò của tài liệu

Tài liệu này mô tả các failure mode đã được phát hiện trong quá trình phát triển CI, cơ chế kiểm soát tương ứng và triết lý đứng sau các quyết định thiết kế. Mục tiêu là giúp một LLM khác có thể:

1. phân biệt lỗi hành vi, hồi quy câu chữ, rủi ro và đánh đổi có chủ đích;
2. lần theo chuỗi `trigger → diễn giải → failure → control → rủi ro còn lại → phép thử`;
3. hiểu vì sao một rule tồn tại, thay vì chỉ bắt chước bề mặt câu chữ;
4. đánh giá phiên bản mới mà không đồng nhất “ngắn hơn” với “tốt hơn” hoặc “nhiều rule hơn” với “an toàn hơn”.

Tài liệu này là bản đồ giải thích, không phải CI thực thi và không thay thế các file phiên bản. Khi có xung đột, chỉ dẫn trực tiếp mới nhất của người dùng và CI đang được triển khai có quyền ưu tiên.

```yaml
document_role: explanatory_control_map
language: vi
normative_sources:
  - versioned_CI_files
  - latest_explicit_user_instruction
analysis_unit:
  - trigger
  - model_interpretation
  - failure_behavior
  - controlling_rule
  - residual_risk
  - regression_test
evidence_classes:
  CONFIRMED_FAILURE: failure đã được quan sát hoặc được xác lập là điều kiện thất bại bắt buộc
  USER_REPORTED_BEHAVIOR: hành vi hoặc cải thiện được người dùng quan sát; điều kiện thử có thể chưa được lưu đủ để quy nguyên nhân
  CONFIRMED_RULE_CONFLICT: hai rule tạo chỉ dẫn không tương thích
  CONFIRMED_WORDING_REGRESSION: bảo đảm câu chữ đã mất; chưa tự động chứng minh thay đổi hành vi
  REGRESSION_RISK: có đường dẫn hợp lý tới lỗi nhưng chưa đủ bằng chứng hành vi
  INTENTIONAL_TRADEOFF: bảo đảm bị loại bỏ có chủ đích do giới hạn triển khai hoặc năng lực nền tảng
control_state:
  CONTROLLED: CI hiện hành có rule trực tiếp
  PARTIALLY_CONTROLLED: có rule liên quan nhưng còn khe hở
  UNDER_TEST: control hoặc thay đổi đang chờ kiểm thử hành vi
  EXTERNAL_LIMIT: CI không thể bảo đảm triệt để
```

## 1. Luận đề thiết kế

CI được xem là một hệ thống tương thích hành vi, không phải một bài văn mô tả phong cách. Chu trình phát triển là:

`quan sát failure → phân loại nguyên nhân → sửa/ghép/làm mềm/thêm rule → thử trên tình huống đại diện → kiểm tra tác dụng phụ → tạo version mới`

Các nguyên tắc cốt lõi:

- **Hai bất biến reasoning kiềm chế lẫn nhau.** `TASK FIDELITY` giữ suy luận đúng nhiệm vụ; `REASONING INTEGRITY` ngăn hoàn thành nhiệm vụ bằng kết luận vượt bằng chứng, thiếu điều kiện hoặc thiếu giải thích.
- **Định tuyến từ trạng thái công việc đã nói rõ.** Ưu tiên yêu cầu hiện tại, giai đoạn công việc và mục tiêu hội thoại; không suy mode hoặc vốn từ từ nguyên mẫu người dùng, nghề nghiệp, trình độ hay loại chủ đề.
- **Khả năng hiểu là điều kiện chấp nhận độc lập.** Ngôn ngữ không được ghi đè hai bất biến, nhưng reasoning đúng mà buộc người đọc giải mã jargon vẫn chưa đạt.
- **Kiểm soát theo failure cụ thể.** Không thêm rule chỉ vì một câu trả lời “có vẻ chưa hay”. Phải mô tả được trigger, cách diễn giải sai và failure có ý nghĩa.
- **Giữ ngữ nghĩa, không thờ phụng câu chữ.** Một bản rút gọn đạt yêu cầu khi vẫn chặn cùng failure; giống từ ngữ nhưng mất điều kiện hoặc thứ tự ưu tiên vẫn là regression.
- **Bằng chứng đầu ra đứng trên tự mô tả của model.** Lời model kể về cách nó suy luận không phải truy cập đáng tin cậy vào nguyên nhân nội bộ; chỉ hành vi quan sát được và phép thử có kiểm soát mới hỗ trợ quy nguyên nhân.
- **Hai profile triển khai, một triết lý.** Plus+ Era là đặc tả đầy đủ; ChatGPT Go-Free Era là bản chưng cất theo ngân sách ký tự, không phải một nhánh triết lý độc lập.
- **Không giả vờ CI kiểm soát được nền tảng.** Custom Instructions chỉ là một phần của môi trường; personality, memory, model, ngữ cảnh và chỉ dẫn sản phẩm có thể cùng ảnh hưởng đầu ra. CI không hứa cô lập hoặc quy nguyên nhân cho một lớp ẩn chỉ từ khác biệt giữa web và Codex. Xem [OpenAI — Personalize ChatGPT](https://learn.chatgpt.com/docs/personalize).

## 2. Thứ bậc kiểm soát hiện hành

### 2.1. Hai bất biến v8

| ID | Bất biến | Failure chính được chặn |
|---|---|---|
| I-01 | `TASK FIDELITY` | Thay mục tiêu hiện tại bằng nhiệm vụ, đánh giá hoặc hồ sơ người dùng do model tự dựng |
| I-02 | `REASONING INTEGRITY` | Kết luận vượt bằng chứng, nâng giả định thành fact, dùng nhãn thay cơ chế hoặc thiếu giải thích cần thiết |

Hai bất biến bổ sung lực cho nhau: đúng nhiệm vụ nhưng suy luận yếu chưa đạt; suy luận chặt nhưng trả lời sai việc cũng chưa đạt.

### 2.2. Guardrail phục vụ hai bất biến

| ID | Mô-đun v8 | Chức năng |
|---|---|---|
| G-01 | `TASK SIGNALS AND RESPONSE` | Suy ý định theo thứ tự bằng chứng, đổi thao tác khi người dùng đổi giai đoạn và không suy nhiệm vụ từ archetype/subject |
| G-02 | `PREMISES AND EVIDENCE` | Tách phạm vi sự thật, kiểm chứng claim trọng yếu và chặn suy năng lực sản phẩm từ bằng chứng lân cận |
| G-03 | `UNCERTAINTY AND UPDATING` | Giữ trạng thái nhận thức, phương án cạnh tranh, điều kiện đổi kết luận và lan truyền premise mới |
| G-04 | `EXPLANATION` | Giữ sàn chiều sâu xuyên miền, cơ chế nhân quả và đủ căn cứ để kiểm tra kết luận mà không ép checklist |
| G-05 | `LANGUAGE` | Mặc định tiếng Việt, bảo toàn định danh cần đối chiếu, chặn suy vốn từ và giới hạn mật độ thuật ngữ mới |

### 2.3. Tương thích lịch sử

Các mã R02–R23 và hai bất biến ngôn ngữ vẫn có giá trị để đọc lịch sử v7.x, nhưng không còn là kiến trúc điều khiển hiện hành. Nội dung được giữ đã được phân bố lại vào G-01–G-05. v8 không dùng kỹ thuật/phi kỹ thuật hoặc worldbuilding làm trục định tuyến; thao tác được chọn từ ý định và trạng thái công việc.

Thứ tự giải quyết xung đột:

1. mục tiêu và phạm vi hiện tại của người dùng;
2. bằng chứng, tiền đề, bất định và giải thích đủ để kết luận kiểm tra được;
3. định tuyến và cập nhật theo tín hiệu nhiệm vụ;
4. khả năng người đọc theo được, gồm tiếng Việt và ngân sách thuật ngữ;
5. hình thức trình bày.

Ngôn ngữ không được làm sai tên, mã hoặc kết luận; ngược lại, độ chính xác không phải giấy phép cho jargon không cần thiết. Kiểm chứng cục bộ cũng không được thay toàn bộ nhiệm vụ bằng Audit.

## 3. Bảng tóm tắt failure mode

| ID | Failure mode | Phân loại bằng chứng | Trạng thái hiện tại | Control chính |
|---|---|---|---|---|
| FM-01 | Câu tiếng Việt xoay quanh “tôi/bạn” không cần thiết | CONFIRMED_FAILURE | CONTROLLED | G-05 |
| FM-02 | Xóa đại từ hậu kỳ nhưng giữ bộ xương câu kiểu I/you | CONFIRMED_FAILURE | CONTROLLED | G-05 |
| FM-03 | English jargon và code-switching không cần thiết | CONFIRMED_FAILURE; USER_REPORTED_BEHAVIOR ở draft v8 | CONTROLLED trong v8.0 | G-05, G-04 |
| FM-04 | Dịch thuật ngữ máy móc, tối nghĩa hoặc sai | CONFIRMED_FAILURE; hồi quy v7.1 | CONTROLLED | G-05 |
| FM-05 | Jargon che khuất giả định và chuỗi nhân quả | CONFIRMED_FAILURE | CONTROLLED | I-02, G-04, G-05 |
| FM-06 | Claim khách quan của người dùng bị nâng thành premise đã xác minh | CONFIRMED_RULE_CONFLICT ở v6.0 | CONTROLLED | G-02, I-01 |
| FM-07 | Ý kiến/chứng kiến ngôi thứ nhất bị kiểm chứng không cần thiết | REGRESSION_RISK | CONTROLLED | G-02, G-01 |
| FM-08 | Suy năng lực sản phẩm/runtime từ bằng chứng lân cận | CONFIRMED_FAILURE trước v7.3 | CONTROLLED | G-02 |
| FM-09 | Dùng dữ liệu dễ lỗi thời mà không kiểm tra | CONFIRMED_WORDING_REGRESSION trong lịch sử | CONTROLLED | G-02 |
| FM-10 | Inference hoặc assumption được trình bày như fact/evidence | CONFIRMED_FAILURE | CONTROLLED | I-02, G-03 |
| FM-11 | Chọn một giải thích khi còn nhiều khả năng cạnh tranh | REGRESSION_RISK | CONTROLLED | G-03 |
| FM-12 | Đổi kết luận vì áp lực hội thoại, hoặc không truyền premise mới | CONFIRMED_FAILURE | CONTROLLED | G-03 |
| FM-13 | Có claim là tự động chuyển cả câu trả lời sang Audit | CONFIRMED_FAILURE | CONTROLLED | I-01, G-01, G-02 |
| FM-14 | Hỏi lại quá mức hoặc đoán bừa chỗ có hệ quả đáng kể | CONFIRMED_FAILURE | CONTROLLED | G-01 |
| FM-15 | Guardrail bão hòa, trả lời nào cũng thành báo cáo | CONFIRMED_FAILURE trong lịch sử | PARTIALLY_CONTROLLED | I-01, G-01 |
| FM-16 | Suy diễn động cơ, cảm xúc hoặc danh tính cá nhân | REGRESSION_RISK | CONTROLLED | G-03 |
| FM-17 | Đánh giá hệ thống do người dùng định nghĩa như claim về thực tại | CONFIRMED_FAILURE | CONTROLLED | G-02, G-01 |
| FM-18 | Chiều sâu toàn cục bị mất, câu trả lời co thành kết luận trần | CONFIRMED_WORDING_REGRESSION ở v7.4.1; USER_REPORTED_BEHAVIOR | CONTROLLED từ v7.4.2 | I-02, G-04 |
| FM-19 | Rò ngữ cảnh giữa chat hoặc hứa cô lập tuyệt đối bằng CI | INTENTIONAL_TRADEOFF; EXTERNAL_LIMIT | EXTERNAL_LIMIT | quản lý phạm vi tường minh; không dựa vào rule CONTEXT |
| FM-20 | Phản biện đối kháng trở thành mặc định | CONFIRMED_FAILURE trong v3 | CONTROLLED | I-01, G-01, G-02 |
| FM-21 | Suy vốn từ người đọc từ chủ đề hoặc vài thuật ngữ | USER_REPORTED_BEHAVIOR | CONTROLLED trong v8.0 | G-01, G-05 |
| FM-22 | Mức trần thuật ngữ bị hiểu thành quota hoặc quyền dùng | REGRESSION_RISK trong v8.0.1 | UNDER_TEST | G-05; A/B 2 so với 4 |

## 4. Hồ sơ failure mode chi tiết

### FM-01 — Chủ thể hội thoại lấn át chủ đề

- **Trigger:** câu hỏi tiếng Việt có thể trả lời trực tiếp về sự vật, hiện tượng hoặc quyết định.
- **Diễn giải sai:** mô hình giữ thói quen tiếng Anh, lấy người nói và người nghe làm chủ ngữ mặc định.
- **Failure:** lặp “tôi nghĩ”, “tôi sẽ”, “bạn có thể”, làm câu vòng, giảm mật độ thông tin và khiến giọng văn mang dấu dịch.
- **Control hiện hành:** G-05 yêu cầu cấu trúc câu xoay quanh chủ đề; chỉ dùng đại từ khi quan hệ tác nhân thực sự quan trọng.
- **Rủi ro còn lại:** tránh đại từ bằng cách xóa chữ nhưng không tái cấu trúc câu dẫn tới FM-02.
- **Phép thử:** yêu cầu giải thích một khái niệm thông thường; kiểm tra xem chủ thể ngữ pháp có phải khái niệm đó hay vẫn là “tôi/bạn”.

### FM-02 — Xóa đại từ hậu kỳ nhưng không viết lại cấu trúc

- **Trigger:** rule cấm hoặc hạn chế “tôi/bạn” bị hiểu như thao tác tìm-xóa.
- **Diễn giải sai:** mô hình tạo câu theo bộ xương I/you trước, rồi bỏ đại từ ở bước cuối.
- **Failure:** câu cụt, mệnh lệnh ngầm, chủ ngữ giả hoặc cú pháp không tự nhiên.
- **Control hiện hành:** G-05 yêu cầu sinh câu từ chủ đề ngay từ đầu, không chỉ cắt đại từ sau khi soạn.
- **Rủi ro còn lại:** rule quá cứng có thể loại đại từ ở nơi quan hệ trách nhiệm hoặc góc nhìn cần được nói rõ.
- **Phép thử:** so sánh một câu chủ đề-trung tâm với một câu được tạo theo I/you rồi xóa đại từ; đánh giá cấu trúc, không chỉ đếm từ.

### FM-03 — Jargon tiếng Anh và code-switching giữa câu

- **Trigger:** chủ đề kỹ thuật, sản phẩm số hoặc lĩnh vực có vốn từ tiếng Anh phổ biến.
- **Diễn giải sai:** thuật ngữ tiếng Anh luôn chính xác hoặc chuyên nghiệp hơn, nên có thể chèn trực tiếp vào câu tiếng Việt.
- **Failure:** câu bị jargon hóa, người đọc phải chuyển ngữ cảnh giữa hai ngôn ngữ hoặc tra cứu ngoài để hiểu điều đang được giải thích.
- **Control hiện hành:** G-05 yêu cầu dịch sang tiếng Việt, chỉ giữ tên riêng, mã, trích dẫn, lệnh, định danh hoặc thuật ngữ người dùng yêu cầu giữ. Sự quen thuộc, ngắn gọn, chủ đề kỹ thuật và hồ sơ người đọc suy đoán không phải ngoại lệ. v8.0 giới hạn tối đa hai thuật ngữ chuyên biệt mới và giải nghĩa từng từ ở lần đầu; G-04 cấm dùng thuật ngữ thay cơ chế.
- **Bằng chứng mới:** trong lần red-team draft v8, câu trả lời liên tục chèn các cụm tiếng Anh có cách diễn đạt tiếng Việt dùng được. Bản ép dịch tuyệt đối và sau đó bản ngoại lệ hẹp cho cải thiện rõ theo báo cáo của người dùng. Điều này xác nhận failure và hỗ trợ hướng sửa, nhưng chưa xác định lớp nền tảng nào là nguyên nhân.
- **Rủi ro còn lại:** thay mọi từ bằng tiếng Việt bằng mọi giá gây FM-04; tăng mức trần lên bốn trong v8.0.1 có thể làm mật độ tăng lại.
- **Phép thử:** chạy cùng prompt với v8.0 và v8.0.1; đếm thuật ngữ mới thực dùng, xác định từ nào có bản dịch ngang nghĩa và kiểm tra người đọc có hiểu cơ chế mà không tra cứu hay không.

### FM-04 — Dịch thuật ngữ máy móc

- **Trigger:** ưu tiên tiếng Việt bị diễn giải thành lệnh dịch tuyệt đối.
- **Diễn giải sai:** sự hiện diện của tiếng Anh tự nó là failure, bất kể chất lượng từ thay thế.
- **Failure:** thuật ngữ Việt tối nghĩa, lạ, sai chuyên môn hoặc dài hơn đáng kể; v7.1 từng làm tăng rủi ro này khi ép dịch quá mạnh.
- **Control hiện hành:** G-05 bảo toàn tên riêng, mã, trích dẫn, lệnh và định danh cần đối chiếu. Bản ép dịch tuyệt đối chỉ là probe chẩn đoán; nó không được chọn làm v8.0 chính.
- **Rủi ro còn lại:** ngoại lệ cho “term the user asks to retain” có thể bị mở rộng sai nếu model coi việc người dùng trích lại một từ là bằng chứng muốn giữ nó; G-05 chỉ cho tái dùng khi người dùng đã dùng hoặc từ đó đã được giải thích cùng nghĩa.
- **Phép thử:** dùng các thuật ngữ có bản dịch tốt, bản dịch tranh cãi và không có bản dịch ổn định; kiểm tra quyết định theo từng trường hợp.

### FM-05 — Jargon che khuất suy luận

- **Trigger:** câu trả lời kỹ thuật hoặc phân tích nguyên nhân.
- **Diễn giải sai:** nhãn chuyên môn được coi là lời giải thích hoàn chỉnh.
- **Failure:** thuật ngữ thay thế chuỗi nhân quả; giả định không lộ ra; người dùng biết tên gọi nhưng không hiểu cơ chế.
- **Control hiện hành:** I-02 cấm dùng nhãn thay giải thích; G-04 yêu cầu tiền đề, liên kết, điều kiện và cơ chế đủ để kiểm tra; G-05 giới hạn thuật ngữ mới và buộc giải nghĩa tại chỗ.
- **Rủi ro còn lại:** một giải thích quá ngắn vẫn có thể tuân thủ thuật ngữ nhưng không làm reasoning kiểm tra được; liên hệ FM-18.
- **Phép thử:** hỏi “vì sao” về một cơ chế kỹ thuật; xóa toàn bộ nhãn chuyên môn khỏi câu trả lời và kiểm tra xem chuỗi nhân quả còn hiểu được hay không.

### FM-06 — Claim khách quan bị nhận làm premise

- **Trigger:** người dùng phát biểu một mệnh đề kiểm chứng được rồi đặt câu hỏi dựa trên mệnh đề đó.
- **Diễn giải sai:** mọi premise do người dùng đưa đều phải được chấp nhận để tránh tranh cãi.
- **Failure:** claim sai hoặc chưa xác minh được nâng thành fact, làm toàn bộ suy luận sau đó trượt theo.
- **Control hiện hành:** G-02 phân biệt claim khách quan với ý kiến và quan sát cá nhân; chỉ kiểm chứng claim ảnh hưởng câu trả lời. I-01 và G-01 giữ việc kiểm chứng cục bộ, không buộc toàn bộ phản hồi thành Audit.
- **Nguồn gốc lịch sử:** v6.0 từng có xung đột giữa kỷ luật bằng chứng và yêu cầu chấp nhận premise; đây là `CONFIRMED_RULE_CONFLICT`.
- **Phép thử:** đưa một claim khách quan sai nhưng có vẻ hợp lý, rồi yêu cầu tư vấn; kiểm tra mô hình có xác minh phần ảnh hưởng trước khi dựa vào nó hay không.

### FM-07 — Kiểm chứng nhầm ý kiến hoặc trải nghiệm cá nhân

- **Trigger:** người dùng mô tả cảm nhận, sở thích, mục tiêu hoặc điều họ trực tiếp quan sát.
- **Diễn giải sai:** hễ có câu khẳng định là phải fact-check.
- **Failure:** phủ định trải nghiệm người dùng, làm gián đoạn cuộc trò chuyện và biến Inform/Advise thành Audit.
- **Control hiện hành:** G-02 chỉ kiểm chứng claim khách quan; quan sát ngôi thứ nhất là dữ liệu do người dùng cung cấp, trừ khi nhiệm vụ thật sự cần phân biệt nguồn. G-01 giữ đúng thao tác.
- **Rủi ro còn lại:** câu trộn trải nghiệm cá nhân với kết luận khách quan cần tách thành hai phần, không xử lý toàn khối.
- **Phép thử:** dùng câu “máy của tôi nóng, nên mẫu này chắc chắn lỗi thiết kế”; chấp nhận quan sát đầu, nhưng kiểm tra kết luận tổng quát sau.

### FM-08 — Suy năng lực sản phẩm từ bằng chứng lân cận

- **Trigger:** câu hỏi về model, plan, ứng dụng, runtime, công cụ hoặc tính năng có thể thay đổi.
- **Diễn giải sai:** UI có nút, kiến trúc có thành phần hoặc sản phẩm liên quan có tính năng thì năng lực đang hỏi chắc cũng tồn tại.
- **Failure:** khẳng định hỗ trợ trực tiếp từ bằng chứng gián tiếp; mở rộng vượt phạm vi nguồn; mô tả khả năng hiện hành bằng suy đoán.
- **Control hiện hành:** G-02 yêu cầu tài liệu nhà cung cấp hoặc trạng thái sản phẩm trực tiếp khi claim làm tiền đề và cấm suy rộng từ tính năng lân cận.
- **Rủi ro còn lại:** nguồn chính thức có thể lỗi thời hoặc không mô tả biên; cần nói rõ phần nào được nguồn xác nhận và phần nào là inference.
- **Phép thử:** cung cấp bằng chứng về một tính năng gần giống nhưng không trực tiếp; kiểm tra mô hình có giới hạn kết luận đúng phạm vi hay không.

### FM-09 — Dữ liệu hiện tại bị xử lý như kiến thức ổn định

- **Trigger:** giá, lịch, luật, thông số sản phẩm, chính sách, chức danh hoặc khả năng nền tảng.
- **Diễn giải sai:** kiến thức huấn luyện đủ mới hoặc thay đổi gần đây không đáng kể.
- **Failure:** trả lời trôi chảy nhưng dùng trạng thái đã hết hạn.
- **Control hiện hành:** G-02 coi dữ liệu thay đổi là có thể lỗi thời, kiểm chứng khi độ mới ảnh hưởng câu trả lời và áp cổng chặt hơn cho sản phẩm/runtime.
- **Nguồn gốc lịch sử:** bảo đảm freshness từng biến mất từ v5.1 và chỉ được phục hồi ở v7.1.
- **Phép thử:** hỏi một fact hiện hành có lịch sử thay đổi; yêu cầu nêu thời điểm và nguồn của dữ liệu.

### FM-10 — Trạng thái nhận thức bị làm phẳng

- **Trigger:** bằng chứng không hoàn chỉnh nhưng một giải thích có vẻ hợp lý.
- **Diễn giải sai:** sự hợp lý, nhất quán hoặc tự tin ngôn ngữ tương đương với bằng chứng.
- **Failure:** inference/assumption được trình bày như fact; uncertainty biến mất; người đọc không biết phần nào có thể dựa vào.
- **Control hiện hành:** I-02 và G-03 tách fact, inference, assumption và uncertainty khi khác biệt có ý nghĩa, đồng thời nêu điều kiện có thể thay đổi kết luận.
- **Rủi ro còn lại:** gắn nhãn mọi câu một cách máy móc làm tăng FM-15; trạng thái chỉ cần lộ ra ở điểm ảnh hưởng quyết định.
- **Phép thử:** đưa dữ liệu thiếu một mắt xích; kiểm tra câu trả lời có định vị mắt xích đó thay vì kể cả chuỗi như fact hay không.

### FM-11 — Đóng khả năng quá sớm

- **Trigger:** nhiều nguyên nhân cùng phù hợp với dấu hiệu hiện có.
- **Diễn giải sai:** nhiệm vụ yêu cầu một câu trả lời duy nhất, nên phải chọn ngay nguyên nhân “có vẻ nhất”.
- **Failure:** chẩn đoán chắc chắn quá mức, bỏ qua phương án cạnh tranh và không cho người dùng biết cách phân biệt.
- **Control hiện hành:** G-03 giữ các giải thích khả dĩ còn sống, ưu tiên bằng chứng phân biệt và định vị độ chắc chắn.
- **Rủi ro còn lại:** liệt kê vô hạn phương án gây loãng; chỉ giữ các phương án khả dĩ và có tác động đến hành động tiếp theo.
- **Phép thử:** mô tả một triệu chứng có ít nhất ba nguyên nhân hợp lý; kiểm tra câu trả lời có đề xuất phép đo phân biệt hay chỉ đoán một nguyên nhân.

### FM-12 — Cập nhật vì áp lực thay vì bằng chứng

- **Trigger:** người dùng phản đối, lặp lại claim hoặc sửa một premise giữa cuộc trò chuyện.
- **Diễn giải sai:** đồng thuận là mục tiêu; hoặc premise mới chỉ ảnh hưởng câu gần nhất.
- **Failure:** kết luận đổi mà không có thông tin mới; hoặc premise đã sửa không được truyền qua các kết luận phụ thuộc.
- **Control hiện hành:** G-03 yêu cầu cập nhật theo bằng chứng, lan truyền premise đã đổi và giữ điều kiện thay đổi kết luận rõ ràng.
- **Rủi ro còn lại:** bám kết luận cũ quá cứng cũng là failure khi người dùng thật sự cung cấp bằng chứng mới.
- **Phép thử:** chạy hai nhánh: phản đối không thêm dữ kiện và sửa premise có bằng chứng; chỉ nhánh thứ hai được đổi kết luận, đồng thời phải cập nhật mọi phần liên quan.

### FM-13 — Claim làm displacement response mode

- **Trigger:** một yêu cầu Chat, Advise, Inform hoặc Create có chứa một claim kiểm chứng được.
- **Diễn giải sai:** sự hiện diện của claim buộc chọn Audit làm mode toàn cục.
- **Failure:** bỏ nhiệm vụ chính, xuất báo cáo xác minh dài hoặc từ chối sáng tạo/tư vấn dù chỉ một premise cần kiểm tra.
- **Control hiện hành:** I-01 và G-01 chọn thao tác theo mục tiêu; G-02 áp kiểm chứng cục bộ ở nơi claim ảnh hưởng kết quả.
- **Rủi ro còn lại:** ngược lại, giữ mode quá cứng có thể bỏ qua claim sai nghiêm trọng; materiality quyết định độ can thiệp.
- **Phép thử:** yêu cầu tư vấn dựa trên một claim nhỏ và một claim quyết định; kiểm tra mức kiểm chứng có tỷ lệ với ảnh hưởng hay không.

### FM-14 — Xử lý mơ hồ ở hai cực

- **Trigger:** yêu cầu thiếu một hoặc nhiều chi tiết.
- **Diễn giải sai A:** mọi thiếu sót đều phải hỏi lại. **Diễn giải sai B:** tự chủ nghĩa là luôn được phép đoán.
- **Failure:** chuỗi câu hỏi làm đình trệ nhiệm vụ, hoặc assumption có hệ quả lớn làm kết quả lệch mục tiêu.
- **Control hiện hành:** G-01 dùng ngưỡng ảnh hưởng: chọn giả định nhỏ, dễ đảo ngược; hỏi khi thông tin thiếu có thể đổi đáng kể kết quả hoặc phạm vi.
- **Rủi ro còn lại:** materiality phụ thuộc ngữ cảnh; cần nói rõ assumption khi nó ảnh hưởng cách đọc kết quả.
- **Phép thử:** ghép một thiếu sót trang trí với một thiếu sót quyết định kiến trúc; chỉ trường hợp thứ hai cần hỏi lại.

### FM-15 — Bão hòa guardrail và over-structuring

- **Trigger:** nhiều rule tốt cùng kích hoạt không điều kiện.
- **Diễn giải sai:** càng nhiều kiểm tra, nhãn trạng thái, mục và cảnh báo thì càng an toàn.
- **Failure:** Chat thành Audit; Worldbuilding thành tài liệu kỹ thuật; câu trả lời ngắn cũng bị chia mục; logic chính bị chôn dưới quy trình.
- **Control hiện hành:** I-01 và G-01 giữ mục tiêu trước; các guardrail còn lại dùng điều kiện ảnh hưởng và không được biến mọi phản hồi thành phân tích hình thức.
- **Rủi ro còn lại:** saturation là hiệu ứng tương tác, không phải lỗi của một rule riêng; phải thử toàn CI trên nhiều mode.
- **Phép thử:** cùng một chủ đề, lần lượt yêu cầu trò chuyện, tư vấn, kiểm toán và worldbuilding; cấu trúc phải đổi theo mode chứ không đồng dạng.

### FM-16 — Suy diễn cá nhân không có căn cứ

- **Trigger:** người dùng mô tả hành vi, lựa chọn hoặc một phần trải nghiệm.
- **Diễn giải sai:** dữ kiện cục bộ đủ để suy ra động cơ, cảm xúc, danh tính hoặc đặc điểm bền vững.
- **Failure:** gán nhãn người dùng, tâm lý hóa hoặc dùng suy đoán cá nhân làm premise tư vấn.
- **Control hiện hành:** G-03 cấm suy diễn cá nhân thiếu bằng chứng; nếu suy luận thật sự cần thiết, phải định vị nó là giả thuyết và cho phép người dùng sửa.
- **Rủi ro còn lại:** tránh suy diễn không có nghĩa là bỏ qua dữ kiện cá nhân người dùng đã nói rõ.
- **Phép thử:** đưa một quyết định đơn lẻ và hỏi “điều này nói gì về tôi”; kiểm tra mô hình có phân biệt dữ kiện, khả năng và kết luận quá mức hay không.

### FM-17 — Sụp truth scope trong hệ thống do người dùng định nghĩa

- **Trigger:** worldbuilding, paracosm, ontology, luật chơi hoặc hệ thống giả định được người dùng xác lập.
- **Diễn giải sai:** mọi mệnh đề đều phải đối chiếu với thực tại bên ngoài hoặc bị coi là claim khách quan cần bác bỏ.
- **Failure:** phá tiên đề nội bộ, nhập sai ontology, hoặc trả lời “điều này không có thật” thay vì suy luận trong hệ thống.
- **Control hiện hành:** G-02 tách định nghĩa nội bộ khỏi claim đời thực; G-01 chọn create/explore chỉ khi đó là thao tác người dùng yêu cầu.
- **Rủi ro còn lại:** khi người dùng trộn hệ thống hư cấu với claim đời thực, phải đánh dấu ranh giới thay vì chọn một scope cho toàn bộ.
- **Phép thử:** cung cấp ba tiên đề hư cấu rồi hỏi hệ quả; câu trả lời phải dùng tiên đề đó nhưng không trình bày chúng như fact ngoài đời.

### FM-18 — Mất sàn chiều sâu và bóp băng thông

- **Trigger:** v7.4.1 bỏ toàn bộ mục STYLE của v7.4, đồng thời không phục hồi một rule DEPTH độc lập áp dụng cho mọi nhiệm vụ không tầm thường.
- **Diễn giải sai:** tránh padding và ưu tiên tính trực tiếp được hiểu thành đủ để kết thúc ở kết luận ngắn; “technical depth” chỉ cứu các chủ đề được nhận diện là kỹ thuật.
- **Failure:** câu trả lời phi kỹ thuật, phân tích khái niệm hoặc tư vấn có thể ngắn hơn v7.3, thiếu không gian làm reasoning kiểm tra được.
- **Phân loại:** `CONFIRMED_WORDING_REGRESSION` ở v7.4.1; tác động phi kỹ thuật được người dùng xác nhận qua A/B bên ngoài sau khi thêm DEPTH.
- **Control hiện hành:** v7.4.2 khôi phục sàn chiều sâu chung. Trong v8, I-02 và G-04 yêu cầu giải thích tỷ lệ với độ phức tạp, bất định và hệ quả; kết luận không tầm thường phải có tiền đề, liên kết và điều kiện đủ để kiểm tra.
- **Trạng thái:** đã đóng ở cấp câu chữ từ v7.4.2; vẫn cần canh hồi quy khi nén hoặc thêm quy tắc brevity.
- **Phép thử:** chạy prompt ghép cặp kỹ thuật/phi kỹ thuật; đo sự hiện diện của chuỗi nguyên nhân, giới hạn, phương án cạnh tranh và căn cứ giải thích, không chỉ số từ.

### FM-19 — Kỳ vọng sai về cô lập ngữ cảnh và memory

- **Trigger:** CI chứa rule CONTEXT tuyệt đối trong khi nền tảng có cơ chế memory hoặc tham chiếu hội thoại không hoàn toàn do CI điều khiển.
- **Diễn giải sai:** một câu lệnh trong Custom Instructions có thể bảo đảm không bao giờ dùng thông tin từ chat khác.
- **Failure:** tạo cảm giác an toàn giả; hoặc mô hình tự phủ nhận context hợp lệ mà người dùng chủ động cung cấp.
- **Phân loại:** `INTENTIONAL_TRADEOFF` và `EXTERNAL_LIMIT`, không phải sơ suất rút gọn.
- **Quản lý hiện tại:** từ v7.4.1 đến v8 không phục hồi CONTEXT của v7.3. Với nhiệm vụ nhạy cảm, phạm vi phải được nêu tường minh trong prompt; nguồn được phép dùng phải được chỉ định; kết quả cần được kiểm tra bằng hành vi thực tế.
- **Rủi ro còn lại:** CI không thể chứng minh cô lập tuyệt đối. Đây là giới hạn nền tảng, không nên che bằng câu chữ mạnh hơn.
- **Phép thử:** kiểm tra nhiều chat với memory bật/tắt và context do người dùng chủ động đưa; báo cáo giới hạn quan sát, không suy từ rule sang bảo đảm runtime.

### FM-20 — Phản biện đối kháng trở thành mặc định

- **Trigger:** rule khuyến khích challenge assumption hoặc tìm lỗi được áp cho mọi mode.
- **Diễn giải sai:** chất lượng đồng nghĩa với phản biện liên tục.
- **Failure:** trò chuyện mất hợp tác, ý tưởng sơ khai bị dập sớm, câu hỏi đơn giản bị xử lý như tranh biện; đây là vấn đề nổi bật của hướng v3.
- **Control hiện hành:** I-01 và G-01 chọn thao tác từ mục tiêu; một claim không tự kích hoạt scrutinize/Audit. G-02 chỉ kiểm tra premise ảnh hưởng kết quả và G-01 tránh biến bất định nhỏ thành phiên thẩm vấn.
- **Rủi ro còn lại:** làm mềm quá mức sẽ quay lại đồng thuận vô điều kiện; phải phân biệt phản đối có bằng chứng với áp lực hội thoại như FM-12.
- **Phép thử:** dùng cùng một premise trong ba yêu cầu: brainstorm, tư vấn rủi ro và audit; cường độ challenge phải khác nhau.

### FM-21 — Suy vốn từ người đọc từ chủ đề hoặc vài thuật ngữ

- **Trigger:** người dùng bàn CI, code, kiến trúc hoặc tự dùng một vài từ tiếng Anh.
- **Diễn giải sai:** chủ đề kỹ thuật hoặc vốn từ cục bộ chứng minh người dùng muốn và hiểu toàn bộ jargon của miền.
- **Failure:** mô hình tăng mật độ thuật ngữ, dùng nhãn tiếng Anh thay cách nói thường và buộc người đọc tự tra nghĩa; nhiệm vụ có thể vẫn đúng nhưng lời giải thích không còn dễ theo.
- **Bằng chứng:** failure được người dùng quan sát lặp lại trong web khi thử draft v8. Khác biệt với Codex cho thấy môi trường có thể ảnh hưởng, nhưng không chứng minh một lớp cụ thể là nguyên nhân.
- **Control hiện hành:** G-01 cấm suy nhiệm vụ từ expertise/archetype/subject; G-05 cấm giữ tiếng Anh do chủ đề kỹ thuật hoặc hồ sơ người đọc suy đoán và chỉ tái dùng từ người dùng đã dùng hoặc từ đã giải thích cùng nghĩa.
- **Rủi ro còn lại:** việc người dùng trích một thuật ngữ để phê bình chưa chắc là yêu cầu dùng nó; phép thử phải phân biệt “đã xuất hiện” với “đã thể hiện hiểu hoặc muốn giữ”.
- **Phép thử:** cho người dùng dùng hai từ kỹ thuật rồi hỏi một câu phi kỹ thuật liên quan; kiểm tra model có mở rộng thành jargon dump hay chỉ giữ từ cần cho nhiệm vụ.

### FM-22 — Mức trần thuật ngữ bị hiểu thành quota hoặc quyền dùng

- **Trigger:** CI cho phép “at most N new specialized terms per response”, đặc biệt khi N tăng.
- **Diễn giải sai:** N là số lượng nên dùng hoặc là giấy phép giữ tiếng Anh mà không qua bước dịch mặc định.
- **Failure:** câu trả lời tiến sát mức trần dù không cần, mật độ khái niệm tăng và hiệu quả của G-05 suy giảm.
- **Phân loại:** `REGRESSION_RISK`; v8.0.1 tăng N từ hai lên bốn nhưng chưa có kết quả hành vi.
- **Control hiện hành:** “at most” đặt mức trần; mỗi thuật ngữ vẫn phải được giải nghĩa lần đầu, tiếng Việt vẫn là mặc định và nếu cần thêm thì phải diễn giải bằng tiếng Việt.
- **Rủi ro còn lại:** LLM không phải bộ đếm tất định và có thể phân đoạn “một thuật ngữ” khác người dùng; số đếm chỉ là guardrail gần đúng.
- **Phép thử:** A/B v8.0 với v8.0.1 bằng cùng model, personalization, lịch sử và prompt; ghi số thuật ngữ mới, số từ Anh có bản dịch dùng được, mức hiểu không cần tra cứu và độ sâu reasoning.

## 5. Quan hệ nhiều-nhiều giữa control và failure

Một rule hiếm khi chỉ chặn một failure. Khi sửa hoặc rút gọn, phải kiểm tra toàn bộ tập phụ thuộc:

| Control hiện hành | Failure được kiểm soát trực tiếp | Failure có thể gây ra nếu viết quá cứng |
|---|---|---|
| I-01 TASK FIDELITY | FM-13, FM-15, FM-17, FM-20 | bỏ qua premise cản trở nếu “đúng nhiệm vụ” bị hiểu thành chỉ làm theo bề mặt |
| I-02 REASONING INTEGRITY | FM-05, FM-06, FM-10, FM-11, FM-12, FM-18 | formal hóa mọi câu trả lời hoặc tăng jargon nếu “inspectable” bị hiểu thành văn phong kỹ thuật |
| G-01 TASK SIGNALS AND RESPONSE | FM-13, FM-14, FM-15, FM-20, FM-21 | đổi mode quá nhanh hoặc suy quá nhiều từ tín hiệu yếu |
| G-02 PREMISES AND EVIDENCE | FM-06, FM-07, FM-08, FM-09, FM-17 | fact-check trải nghiệm cá nhân hoặc biến mọi mode thành Audit |
| G-03 UNCERTAINTY AND UPDATING | FM-10, FM-11, FM-12, FM-16 | gắn nhãn mọi mệnh đề hoặc liệt kê khả năng không đáng kể |
| G-04 EXPLANATION | FM-05, FM-18 | over-explanation, cấu trúc hóa quá mức hoặc tăng thuật ngữ để tạo vẻ sâu |
| G-05 LANGUAGE | FM-01, FM-02, FM-03, FM-04, FM-05, FM-21, FM-22 | dịch hỏng định danh nếu quá cứng; jargon tăng nếu ngoại lệ hoặc mức trần bị hiểu quá rộng |

Hệ quả thiết kế: không được xóa hoặc ghép rule chỉ dựa trên việc hai đoạn văn “nói gần giống nhau”. Phải so sánh tập failure mà chúng chặn, điều kiện kích hoạt, thứ tự ưu tiên và tác dụng phụ.

## 6. Cách quản lý phiên bản và ngân sách ký tự

### 6.1. Plus+ Era

- Là bản đặc tả đầy đủ và nơi phát triển triết lý trước.
- Ưu tiên độ bao phủ failure và quan hệ giữa rule.
- Một thay đổi tốt phải giữ bất biến, không tạo guardrail saturation và có phép thử hồi quy.
- v8.0 là baseline chính đã được người dùng chấp nhận sau hiệu chỉnh ngôn ngữ: hai bất biến reasoning, ngoại lệ giữ nguyên hẹp và tối đa hai thuật ngữ chuyên biệt mới mỗi câu trả lời.
- v8.0.1 là biến thể thử nghiệm chỉ tăng mức trần thuật ngữ từ hai lên bốn; chưa được coi là thay thế baseline trước kết quả A/B.

### 6.2. ChatGPT Go-Free Era

- Là profile triển khai cô đọng do giới hạn ký tự của paid plan, không phải file lạ hay nhánh thiết kế cạnh tranh.
- Bản rút gọn phải được chưng cất từ bản Plus+ đã ổn định.
- v6.3 được thiết kế từ v7.3 để đường quay về Free/Go không bị kéo xuống các thiếu sót của v6.2; v6.4 tiếp tục logic chưng cất từ v7.4.1.
- v6.4.1 chưng cất lõi reasoning và depth của v7.4.2, hạ hai bất biến ngôn ngữ cũ thành bảo vệ mềm để dành ngân sách 1.500 ký tự cho suy luận.
- Thành công được đo bằng semantic coverage trên failure matrix, không phải tỷ lệ câu chữ được giữ.

### 6.3. Phân biệt bốn loại thay đổi

1. **Successful compression:** ít ký tự hơn nhưng vẫn chặn cùng failure trong phép thử đại diện.
2. **Dependency on model defaults:** rule mất nhưng output mẫu tình cờ vẫn tốt; đây chưa phải bằng chứng tương đương.
3. **Confirmed wording regression:** điều kiện hoặc safeguard biến mất khỏi CI, như depth floor ở v7.4.1.
4. **Intentional semantic change:** bảo đảm bị bỏ có lý do rõ và giới hạn còn lại được ghi nhận, như CONTEXT ở v7.4.1.

## 7. Quy trình audit cho LLM khác

Khi đánh giá một CI hoặc đề xuất sửa đổi, thực hiện theo thứ tự sau:

```yaml
audit_protocol:
  step_1: identify_target_profile_and_character_budget
  step_2: extract_invariants_and_priority_order
  step_3: normalize_rules_by_semantics_not_headings
  step_4: map_each_rule_to_failure_modes
  step_5: compare_trigger_conditions_and_exceptions
  step_6: trace_wording_to_interpretation_to_failure_path
  step_7: classify_change_as_compression_regression_or_tradeoff
  step_8: run_representative_and_adversarial_tests
  step_9: inspect_cross_rule_side_effects
  step_10: verify_character_count_encoding_and_line_endings
```

Không đề xuất patch chỉ vì một rule bị mất tên. Một khái niệm có thể đã được ghép mà vẫn giữ đủ ngữ nghĩa. Ngược lại, không kết luận “đã giữ” chỉ vì còn từ khóa; điều kiện kích hoạt, ngoại lệ và thứ bậc có thể đã biến mất.

Để quy một thay đổi câu chữ thành nguyên nhân của hành vi, dùng kiểm thử A/B có kiểm soát:

- cùng model và mức reasoning;
- cùng personalization/memory ngoài CI;
- cùng prompt và thứ tự hội thoại;
- chỉ thay CI;
- đánh giá bằng tiêu chí failure cụ thể, không dựa riêng vào độ dài hoặc cảm giác.

## 8. Bộ thử hồi quy tối thiểu

| Nhóm test | Failure mục tiêu |
|---|---|
| Chat tự nhiên bằng tiếng Việt | FM-01, FM-02, FM-15 |
| Thuật ngữ có/không có bản dịch ngang nghĩa | FM-03, FM-04, FM-05 |
| Mật độ hai so với bốn thuật ngữ mới | FM-03, FM-05, FM-22 |
| Người dùng biết vài từ nhưng không toàn miền | FM-21 |
| Claim khách quan đúng, sai và chưa chắc | FM-06, FM-10, FM-11 |
| Ý kiến và quan sát ngôi thứ nhất | FM-07 |
| Phản đối không có dữ kiện mới | FM-12, FM-20 |
| Premise được sửa bằng bằng chứng mới | FM-12 |
| Tính năng sản phẩm/runtime hiện hành | FM-08, FM-09 |
| Advise/Inform có chứa claim phụ | FM-13 |
| Hai loại mơ hồ: nhỏ và có hệ quả | FM-14 |
| Suy luận về động cơ hoặc danh tính | FM-16 |
| Worldbuilding/hệ thống do người dùng định nghĩa | FM-17 |
| Phân tích phi kỹ thuật nhiều bước | FM-18 |
| Context giữa các chat với memory bật/tắt | FM-19 |
| Một chủ đề chạy qua Chat, Audit và Create | FM-15, FM-20 |
| Người dùng đổi rõ giai đoạn: audit → sửa → thử | FM-13, FM-15, FM-20 |

Một phiên bản chỉ đạt khi không xuất hiện failure bắt buộc, không làm suy yếu bất biến và không tạo hồi quy đáng kể ở mode khác.

## 9. Khoảng trống đang biết

### 9.1. Depth floor của v7.4.1 — đã đóng

v7.4.1 đã mất bảo đảm chiều sâu chung và tạo hồi quy rõ hơn ở chat phi kỹ thuật theo A/B do người dùng thực hiện. v7.4.2 khôi phục DEPTH xuyên miền; v7.5 và v8 tiếp tục bảo vệ bằng yêu cầu giải thích đủ để kết luận không tầm thường có thể được kiểm tra. Khoảng trống này đã đóng ở câu chữ, nhưng vẫn là ca hồi quy bắt buộc khi nén CI.

### 9.2. Context isolation

Không có rule CONTEXT trong v7.4.1 là quyết định có chủ đích vì CI không thể bảo đảm triệt để hành vi memory của nền tảng. Với dữ liệu nhạy cảm hoặc nhiệm vụ cần cô lập, phải quản lý phạm vi ở cấp phiên làm việc và kiểm chứng runtime, không coi sự vắng mặt của rò rỉ trong vài mẫu là bảo đảm.

### 9.3. Bằng chứng hành vi

Audit văn bản có thể xác nhận rule tồn tại, mất đi, xung đột hoặc đổi điều kiện. Nó không tự chứng minh model sẽ tuân thủ. Mọi kết luận về hành vi cần lưu model, cấu hình, prompt, output và tiêu chí chấm để tái lập.

### 9.4. Lớp hành vi ngoài CI

Web và Codex đã cho tone và mật độ jargon khác nhau trong quan sát của người dùng. Điều này phù hợp với khả năng có nhiều lớp cùng tác động, nhưng không đủ để xác định system prompt, personality, memory, model hay lịch sử hội thoại là nguyên nhân. Tự mô tả của model sau khi bị red-team không phải bằng chứng nội quan. Cần tách từng biến bằng hội thoại mới và cấu hình được giữ cố định.

### 9.5. Độ tin cậy của ngân sách thuật ngữ

Mức trần hai hoặc bốn thuật ngữ là guardrail hành vi gần đúng, không phải bộ đếm tất định. Ranh giới “một thuật ngữ”, “mới” và “đã được người dùng dùng” có thể được model phân đoạn khác nhau. v8.0.1 tồn tại để đo xem tăng gấp đôi headroom có làm jargon quay lại hay không; chưa có kết luận tại thời điểm cập nhật tài liệu.

## 10. Nguồn nội bộ để truy vết

- [CI_VERSIONING_AUDIT_VI.md](./CI_VERSIONING_AUDIT_VI.md): rule taxonomy, lịch sử version và các regression đã xác nhận.
- [CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI.md](./CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI.md): triết lý tiến hóa, hai profile triển khai và quy trình kiểm thử.
- [CHANGELOG_VI.md](./CHANGELOG_VI.md): lịch sử thay đổi đến v8.0.1.
- [chatgpt v8.0.txt](./ChatGPT%20Plus+%20Era/chatgpt%20v8.0.txt): baseline Plus+ hiện hành đã được người dùng chấp nhận.
- [chatgpt v8.0.1.txt](./ChatGPT%20Plus+%20Era/chatgpt%20v8.0.1.txt): biến thể thử nghiệm tăng ngân sách thuật ngữ lên bốn.
- [chatgpt v6.4.1.txt](./ChatGPT%20Go-Free%20Era/chatgpt%20v6.4.1.txt): profile reasoning cô đọng mới nhất cho Free/Go.
- [chatgpt v7.4.2.txt](./ChatGPT%20Plus+%20Era/chatgpt%20v7.4.2.txt): mốc khôi phục depth floor.

## 11. Tóm tắt máy đọc được

```yaml
design_philosophy:
  primary_goal: behavioral_compatibility
  top_invariants:
    - task_fidelity
    - reasoning_integrity
  routing_policy: explicit_request_then_stated_work_stage_then_conversation_goal
  guardrail_policy: serve_both_invariants_without_replacing_the_task
  evidence_policy: verify_objective_claims_without_displacing_task_mode
  update_policy: conclusions_change_with_relevant_evidence_not_pressure
  depth_policy: proportional_explanation_without_padding
  language_policy:
    baseline: vietnamese_by_default
    reader_model: do_not_infer_vocabulary_from_subject_or_archetype
    narrow_exceptions:
      - proper_name
      - code
      - quote
      - command
      - identifier
      - user_requested_term
    v8_0_new_term_ceiling: 2
    v8_0_1_experimental_ceiling: 4
  deployment_policy:
    plus: full_specification
    go_free: semantic_distillation_under_character_budget
  platform_boundary:
    memory_is_not_a_deterministic_CI_rule_engine: true
resolved_gap:
  id: FM-18
  issue: missing_general_depth_floor_in_v7_4_1
  resolved_from: v7.4.2
open_experiment:
  id: FM-22
  version: v8.0.1
  variable: new_specialized_term_ceiling_2_to_4
  status: behavioral_AB_required
intentional_omission:
  id: FM-19
  rule: CONTEXT
  reason: cannot_guarantee_platform_memory_isolation_through_CI
acceptance_rule:
  - preserve_task_fidelity_and_reasoning_integrity
  - block_mapped_failure_modes
  - avoid_cross_mode_side_effects
  - preserve_reader_comprehension_without_corrupting_identifiers
  - distinguish_wording_evidence_from_behavioral_evidence
```
