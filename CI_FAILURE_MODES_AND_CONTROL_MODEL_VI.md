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
  CONFIRMED_RULE_CONFLICT: hai rule tạo chỉ dẫn không tương thích
  CONFIRMED_WORDING_REGRESSION: bảo đảm câu chữ đã mất; chưa tự động chứng minh thay đổi hành vi
  REGRESSION_RISK: có đường dẫn hợp lý tới lỗi nhưng chưa đủ bằng chứng hành vi
  INTENTIONAL_TRADEOFF: bảo đảm bị loại bỏ có chủ đích do giới hạn triển khai hoặc năng lực nền tảng
control_state:
  CONTROLLED: CI hiện hành có rule trực tiếp
  PARTIALLY_CONTROLLED: có rule liên quan nhưng còn khe hở
  EXTERNAL_LIMIT: CI không thể bảo đảm triệt để
```

## 1. Luận đề thiết kế

CI được xem là một hệ thống tương thích hành vi, không phải một bài văn mô tả phong cách. Chu trình phát triển là:

`quan sát failure → phân loại nguyên nhân → sửa/ghép/làm mềm/thêm rule → thử trên tình huống đại diện → kiểm tra tác dụng phụ → tạo version mới`

Các nguyên tắc cốt lõi:

- **Bất biến đứng trên guardrail.** Cấu trúc chủ thể tiếng Việt và thuật ngữ tiếng Việt là hai bất biến đầu vào; kiểm chứng, định tuyến và trình bày chỉ được hỗ trợ, không được làm hỏng chúng.
- **Kiểm soát theo failure cụ thể.** Không thêm rule chỉ vì một câu trả lời “có vẻ chưa hay”. Phải mô tả được trigger, cách diễn giải sai và failure có ý nghĩa.
- **Giữ ngữ nghĩa, không thờ phụng câu chữ.** Một bản rút gọn đạt yêu cầu khi vẫn chặn cùng failure; giống từ ngữ nhưng mất điều kiện hoặc thứ tự ưu tiên vẫn là regression.
- **Guardrail phải có điều kiện.** Kiểm chứng, phản biện, cấu trúc và chiều sâu chỉ kích hoạt khi nhiệm vụ hoặc hệ quả yêu cầu; nếu áp toàn cục, chúng biến trò chuyện thành báo cáo kiểm toán.
- **Bằng chứng đầu ra đứng trên danh tiếng mô hình.** Không giả định model mới sẽ tự giữ các hành vi mà rule đã bỏ.
- **Hai profile triển khai, một triết lý.** Plus+ Era là đặc tả đầy đủ; ChatGPT Go-Free Era là bản chưng cất theo ngân sách ký tự, không phải một nhánh triết lý độc lập.
- **Không giả vờ CI kiểm soát được nền tảng.** Custom Instructions thể hiện ưu tiên áp dụng qua các cuộc trò chuyện, còn memory là một cơ chế riêng. Vì vậy CI không coi memory là bộ máy luật tất định và không hứa cô lập ngữ cảnh tuyệt đối chỉ bằng câu chữ CI. Xem [OpenAI — Personalize ChatGPT](https://learn.chatgpt.com/docs/personalize).

## 2. Thứ bậc kiểm soát

### 2.1. Bất biến ngôn ngữ

| ID | Bất biến | Failure chính được chặn |
|---|---|---|
| I-01 / R02 | `VIETNAMESE — SUBJECT STRUCTURE` | Lấy “tôi/bạn” làm xương sống câu; xóa đại từ hậu kỳ nhưng giữ cấu trúc dịch từ tiếng Anh |
| I-02 / R03 | `VIETNAMESE — TERMINOLOGY` | English jargon không cần thiết, code-switching giữa câu, dịch máy móc làm sai hoặc tối nghĩa |

### 2.2. Guardrail bằng chứng và cập nhật

| Nhóm | Rule | Chức năng |
|---|---|---|
| EVIDENCE | R04, R23 | Kiểm chứng claim khách quan và năng lực sản phẩm/runtime bằng nguồn phù hợp |
| EPISTEMIC STATE | R05 | Tách fact, inference, assumption và uncertainty |
| ALTERNATIVES | R06 | Giữ các giải thích khả dĩ và nêu bằng chứng phân biệt |
| UPDATE | R09 | Truyền premise mới qua toàn bộ kết luận bị ảnh hưởng |
| FRESHNESS | R11 | Kiểm tra dữ liệu có khả năng thay đổi theo thời gian |
| FALSIFIABILITY | R21 | Nêu điều gì có thể làm kết luận thay đổi khi cần |

### 2.3. Guardrail định tuyến, phạm vi và độ sâu

| Nhóm | Rule | Chức năng |
|---|---|---|
| RESPONSE MODE | R07 | Chọn Chat, Advise, Inform, Create, Audit hoặc Worldbuilding theo nhiệm vụ |
| AMBIGUITY | R08 | Chỉ hỏi lại khi thiếu thông tin có thể làm thay đổi đáng kể kết quả |
| TECHNICAL / NON-TECHNICAL | R12 | Giải thích cơ chế khi hữu ích; không bắt người dùng tra từ điển để hiểu câu trả lời |
| DEPTH / DOMAIN | R13 | Điều chỉnh chiều sâu theo độ phức tạp và hệ quả |
| TRUTH SCOPE | R16 | Phân biệt thế giới thực với hệ thống do người dùng định nghĩa |
| PERSONAL INFERENCE | R20 | Không tự suy diễn động cơ, cảm xúc, danh tính hoặc đặc điểm cá nhân |

Thứ tự giải quyết xung đột:

1. cấu trúc chủ thể tiếng Việt;
2. thuật ngữ tiếng Việt;
3. tính đúng và kỷ luật bằng chứng;
4. response mode và truth scope;
5. chiều sâu và hình thức trình bày.

Rule cấp thấp không được vô hiệu hóa rule cấp cao. Ví dụ, yêu cầu “technical depth” không cho phép jargon hóa tiếng Anh; yêu cầu kiểm chứng không tự động biến mọi câu trả lời thành Audit.

## 3. Bảng tóm tắt failure mode

| ID | Failure mode | Phân loại bằng chứng | Trạng thái hiện tại | Control chính |
|---|---|---|---|---|
| FM-01 | Câu tiếng Việt xoay quanh “tôi/bạn” không cần thiết | CONFIRMED_FAILURE | CONTROLLED | I-01 / R02 |
| FM-02 | Xóa đại từ hậu kỳ nhưng giữ bộ xương câu kiểu I/you | CONFIRMED_FAILURE | CONTROLLED | I-01 / R02 |
| FM-03 | English jargon và code-switching không cần thiết | CONFIRMED_FAILURE | CONTROLLED | I-02 / R03, R12 |
| FM-04 | Dịch thuật ngữ máy móc, tối nghĩa hoặc sai | CONFIRMED_FAILURE; hồi quy v7.1 | CONTROLLED | I-02 / R03 |
| FM-05 | Jargon che khuất giả định và chuỗi nhân quả | CONFIRMED_FAILURE | CONTROLLED | R03, R12, R13 |
| FM-06 | Claim khách quan của người dùng bị nâng thành premise đã xác minh | CONFIRMED_RULE_CONFLICT ở v6.0 | CONTROLLED | R04, R07 |
| FM-07 | Ý kiến/chứng kiến ngôi thứ nhất bị kiểm chứng không cần thiết | REGRESSION_RISK | CONTROLLED | R04, R07 |
| FM-08 | Suy năng lực sản phẩm/runtime từ bằng chứng lân cận | CONFIRMED_FAILURE trước v7.3 | CONTROLLED | R23 |
| FM-09 | Dùng dữ liệu dễ lỗi thời mà không kiểm tra | CONFIRMED_WORDING_REGRESSION trong lịch sử | CONTROLLED | R11 |
| FM-10 | Inference hoặc assumption được trình bày như fact/evidence | CONFIRMED_FAILURE | CONTROLLED | R05, R21 |
| FM-11 | Chọn một giải thích khi còn nhiều khả năng cạnh tranh | REGRESSION_RISK | CONTROLLED | R06, R05 |
| FM-12 | Đổi kết luận vì áp lực hội thoại, hoặc không truyền premise mới | CONFIRMED_FAILURE | CONTROLLED | R09, R21 |
| FM-13 | Có claim là tự động chuyển cả câu trả lời sang Audit | CONFIRMED_FAILURE | CONTROLLED | R07, R04 |
| FM-14 | Hỏi lại quá mức hoặc đoán bừa chỗ có hệ quả đáng kể | CONFIRMED_FAILURE | CONTROLLED | R08 |
| FM-15 | Guardrail bão hòa, trả lời nào cũng thành báo cáo | CONFIRMED_FAILURE trong lịch sử | PARTIALLY_CONTROLLED | R07, thứ bậc control |
| FM-16 | Suy diễn động cơ, cảm xúc hoặc danh tính cá nhân | REGRESSION_RISK | CONTROLLED | R20 |
| FM-17 | Đánh giá hệ thống do người dùng định nghĩa như claim về thực tại | CONFIRMED_FAILURE | CONTROLLED | R16, R07 |
| FM-18 | Chiều sâu toàn cục bị mất, câu trả lời co thành kết luận trần | CONFIRMED_WORDING_REGRESSION ở v7.4.1 | PARTIALLY_CONTROLLED | R12/R13; thiếu depth floor chung |
| FM-19 | Rò ngữ cảnh giữa chat hoặc hứa cô lập tuyệt đối bằng CI | INTENTIONAL_TRADEOFF; EXTERNAL_LIMIT | EXTERNAL_LIMIT | quản lý phạm vi tường minh; không dựa vào rule CONTEXT |
| FM-20 | Phản biện đối kháng trở thành mặc định | CONFIRMED_FAILURE trong v3 | CONTROLLED | R07, materiality gate |

## 4. Hồ sơ failure mode chi tiết

### FM-01 — Chủ thể hội thoại lấn át chủ đề

- **Trigger:** câu hỏi tiếng Việt có thể trả lời trực tiếp về sự vật, hiện tượng hoặc quyết định.
- **Diễn giải sai:** mô hình giữ thói quen tiếng Anh, lấy người nói và người nghe làm chủ ngữ mặc định.
- **Failure:** lặp “tôi nghĩ”, “tôi sẽ”, “bạn có thể”, làm câu vòng, giảm mật độ thông tin và khiến giọng văn mang dấu dịch.
- **Control:** I-01/R02 yêu cầu cấu trúc câu xoay quanh chủ đề; chỉ dùng đại từ khi quan hệ tác nhân thực sự quan trọng.
- **Rủi ro còn lại:** tránh đại từ bằng cách xóa chữ nhưng không tái cấu trúc câu dẫn tới FM-02.
- **Phép thử:** yêu cầu giải thích một khái niệm thông thường; kiểm tra xem chủ thể ngữ pháp có phải khái niệm đó hay vẫn là “tôi/bạn”.

### FM-02 — Xóa đại từ hậu kỳ nhưng không viết lại cấu trúc

- **Trigger:** rule cấm hoặc hạn chế “tôi/bạn” bị hiểu như thao tác tìm-xóa.
- **Diễn giải sai:** mô hình tạo câu theo bộ xương I/you trước, rồi bỏ đại từ ở bước cuối.
- **Failure:** câu cụt, mệnh lệnh ngầm, chủ ngữ giả hoặc cú pháp không tự nhiên.
- **Control:** I-01/R02 yêu cầu sinh câu từ chủ đề ngay từ đầu, không chỉ cắt đại từ sau khi soạn.
- **Rủi ro còn lại:** rule quá cứng có thể loại đại từ ở nơi quan hệ trách nhiệm hoặc góc nhìn cần được nói rõ.
- **Phép thử:** so sánh một câu chủ đề-trung tâm với một câu được tạo theo I/you rồi xóa đại từ; đánh giá cấu trúc, không chỉ đếm từ.

### FM-03 — Jargon tiếng Anh và code-switching giữa câu

- **Trigger:** chủ đề kỹ thuật, sản phẩm số hoặc lĩnh vực có vốn từ tiếng Anh phổ biến.
- **Diễn giải sai:** thuật ngữ tiếng Anh luôn chính xác hoặc chuyên nghiệp hơn, nên có thể chèn trực tiếp vào câu tiếng Việt.
- **Failure:** câu bị jargon hóa, người đọc phải chuyển ngữ cảnh giữa hai ngôn ngữ hoặc tra cứu ngoài để hiểu điều đang được giải thích.
- **Control:** I-02/R03 ưu tiên từ tiếng Việt ngang nghĩa bất cứ khi nào có thể; tránh code-switching giữa câu; nếu cần giữ thuật ngữ gốc thì dịch hoặc giải thích ngay tại chỗ. R12 ngăn chi tiết kỹ thuật làm giảm khả năng hiểu.
- **Rủi ro còn lại:** thay mọi từ bằng tiếng Việt bằng mọi giá sẽ gây FM-04.
- **Phép thử:** đưa một đoạn kỹ thuật chứa 5–8 thuật ngữ Anh; đánh giá từng từ theo ba nhánh: dịch ngang nghĩa, giữ kèm giải thích, hoặc giữ nguyên vì dịch sẽ sai/mất nghĩa.

### FM-04 — Dịch thuật ngữ máy móc

- **Trigger:** ưu tiên tiếng Việt bị diễn giải thành lệnh dịch tuyệt đối.
- **Diễn giải sai:** sự hiện diện của tiếng Anh tự nó là failure, bất kể chất lượng từ thay thế.
- **Failure:** thuật ngữ Việt tối nghĩa, lạ, sai chuyên môn hoặc dài hơn đáng kể; v7.1 từng làm tăng rủi ro này khi ép dịch quá mạnh.
- **Control:** I-02/R03 đặt chất lượng ngữ nghĩa cao hơn sự thuần Việt hình thức; chỉ thay khi nghĩa ngang hàng, còn thuật ngữ cần giữ phải được giải thích đủ dùng.
- **Rủi ro còn lại:** “thuật ngữ cần giữ” có thể bị lạm dụng làm cửa thoát cho jargon.
- **Phép thử:** dùng các thuật ngữ có bản dịch tốt, bản dịch tranh cãi và không có bản dịch ổn định; kiểm tra quyết định theo từng trường hợp.

### FM-05 — Jargon che khuất suy luận

- **Trigger:** câu trả lời kỹ thuật hoặc phân tích nguyên nhân.
- **Diễn giải sai:** nhãn chuyên môn được coi là lời giải thích hoàn chỉnh.
- **Failure:** thuật ngữ thay thế chuỗi nhân quả; giả định không lộ ra; người dùng biết tên gọi nhưng không hiểu cơ chế.
- **Control:** R12 yêu cầu giải thích bằng ngôn ngữ dễ dùng và chỉ giữ jargon khi nó mang giá trị; R13 yêu cầu đủ chiều sâu để lộ cơ chế; R03 buộc dịch/giải thích tại chỗ.
- **Rủi ro còn lại:** một giải thích quá ngắn vẫn có thể tuân thủ thuật ngữ nhưng không làm reasoning kiểm tra được; liên hệ FM-18.
- **Phép thử:** hỏi “vì sao” về một cơ chế kỹ thuật; xóa toàn bộ nhãn chuyên môn khỏi câu trả lời và kiểm tra xem chuỗi nhân quả còn hiểu được hay không.

### FM-06 — Claim khách quan bị nhận làm premise

- **Trigger:** người dùng phát biểu một mệnh đề kiểm chứng được rồi đặt câu hỏi dựa trên mệnh đề đó.
- **Diễn giải sai:** mọi premise do người dùng đưa đều phải được chấp nhận để tránh tranh cãi.
- **Failure:** claim sai hoặc chưa xác minh được nâng thành fact, làm toàn bộ suy luận sau đó trượt theo.
- **Control:** R04 phân biệt claim khách quan với ý kiến và quan sát cá nhân; kiểm chứng claim khi nó có ý nghĩa đối với kết quả. R07 giữ việc kiểm chứng cục bộ, không buộc toàn bộ câu trả lời thành Audit.
- **Nguồn gốc lịch sử:** v6.0 từng có xung đột giữa kỷ luật bằng chứng và yêu cầu chấp nhận premise; đây là `CONFIRMED_RULE_CONFLICT`.
- **Phép thử:** đưa một claim khách quan sai nhưng có vẻ hợp lý, rồi yêu cầu tư vấn; kiểm tra mô hình có xác minh phần ảnh hưởng trước khi dựa vào nó hay không.

### FM-07 — Kiểm chứng nhầm ý kiến hoặc trải nghiệm cá nhân

- **Trigger:** người dùng mô tả cảm nhận, sở thích, mục tiêu hoặc điều họ trực tiếp quan sát.
- **Diễn giải sai:** hễ có câu khẳng định là phải fact-check.
- **Failure:** phủ định trải nghiệm người dùng, làm gián đoạn cuộc trò chuyện và biến Inform/Advise thành Audit.
- **Control:** R04 chỉ kiểm chứng claim khách quan; quan sát ngôi thứ nhất được dùng như dữ liệu do người dùng cung cấp, trừ khi nhiệm vụ thật sự cần phân biệt nguồn. R07 giữ đúng mode.
- **Rủi ro còn lại:** câu trộn trải nghiệm cá nhân với kết luận khách quan cần tách thành hai phần, không xử lý toàn khối.
- **Phép thử:** dùng câu “máy của tôi nóng, nên mẫu này chắc chắn lỗi thiết kế”; chấp nhận quan sát đầu, nhưng kiểm tra kết luận tổng quát sau.

### FM-08 — Suy năng lực sản phẩm từ bằng chứng lân cận

- **Trigger:** câu hỏi về model, plan, ứng dụng, runtime, công cụ hoặc tính năng có thể thay đổi.
- **Diễn giải sai:** UI có nút, kiến trúc có thành phần hoặc sản phẩm liên quan có tính năng thì năng lực đang hỏi chắc cũng tồn tại.
- **Failure:** khẳng định hỗ trợ trực tiếp từ bằng chứng gián tiếp; mở rộng vượt phạm vi nguồn; mô tả khả năng hiện hành bằng suy đoán.
- **Control:** R23 yêu cầu kiểm tra tài liệu của nhà cung cấp hoặc bằng chứng trực tiếp phù hợp và cấm suy rộng từ tính năng lân cận.
- **Rủi ro còn lại:** nguồn chính thức có thể lỗi thời hoặc không mô tả biên; cần nói rõ phần nào được nguồn xác nhận và phần nào là inference.
- **Phép thử:** cung cấp bằng chứng về một tính năng gần giống nhưng không trực tiếp; kiểm tra mô hình có giới hạn kết luận đúng phạm vi hay không.

### FM-09 — Dữ liệu hiện tại bị xử lý như kiến thức ổn định

- **Trigger:** giá, lịch, luật, thông số sản phẩm, chính sách, chức danh hoặc khả năng nền tảng.
- **Diễn giải sai:** kiến thức huấn luyện đủ mới hoặc thay đổi gần đây không đáng kể.
- **Failure:** trả lời trôi chảy nhưng dùng trạng thái đã hết hạn.
- **Control:** R11 kích hoạt kiểm tra freshness khi dữ liệu có khả năng đổi và sự thay đổi ảnh hưởng câu trả lời; R23 áp riêng cho sản phẩm/runtime.
- **Nguồn gốc lịch sử:** bảo đảm freshness từng biến mất từ v5.1 và chỉ được phục hồi ở v7.1.
- **Phép thử:** hỏi một fact hiện hành có lịch sử thay đổi; yêu cầu nêu thời điểm và nguồn của dữ liệu.

### FM-10 — Trạng thái nhận thức bị làm phẳng

- **Trigger:** bằng chứng không hoàn chỉnh nhưng một giải thích có vẻ hợp lý.
- **Diễn giải sai:** sự hợp lý, nhất quán hoặc tự tin ngôn ngữ tương đương với bằng chứng.
- **Failure:** inference/assumption được trình bày như fact; uncertainty biến mất; người đọc không biết phần nào có thể dựa vào.
- **Control:** R05 yêu cầu phân biệt fact, inference, assumption và uncertainty khi khác biệt có ý nghĩa; R21 nêu điều kiện có thể bác bỏ hoặc thay đổi kết luận.
- **Rủi ro còn lại:** gắn nhãn mọi câu một cách máy móc làm tăng FM-15; trạng thái chỉ cần lộ ra ở điểm ảnh hưởng quyết định.
- **Phép thử:** đưa dữ liệu thiếu một mắt xích; kiểm tra câu trả lời có định vị mắt xích đó thay vì kể cả chuỗi như fact hay không.

### FM-11 — Đóng khả năng quá sớm

- **Trigger:** nhiều nguyên nhân cùng phù hợp với dấu hiệu hiện có.
- **Diễn giải sai:** nhiệm vụ yêu cầu một câu trả lời duy nhất, nên phải chọn ngay nguyên nhân “có vẻ nhất”.
- **Failure:** chẩn đoán chắc chắn quá mức, bỏ qua phương án cạnh tranh và không cho người dùng biết cách phân biệt.
- **Control:** R06 giữ các giải thích khả dĩ còn sống và ưu tiên bằng chứng phân biệt; R05 định vị độ chắc chắn.
- **Rủi ro còn lại:** liệt kê vô hạn phương án gây loãng; chỉ giữ các phương án khả dĩ và có tác động đến hành động tiếp theo.
- **Phép thử:** mô tả một triệu chứng có ít nhất ba nguyên nhân hợp lý; kiểm tra câu trả lời có đề xuất phép đo phân biệt hay chỉ đoán một nguyên nhân.

### FM-12 — Cập nhật vì áp lực thay vì bằng chứng

- **Trigger:** người dùng phản đối, lặp lại claim hoặc sửa một premise giữa cuộc trò chuyện.
- **Diễn giải sai:** đồng thuận là mục tiêu; hoặc premise mới chỉ ảnh hưởng câu gần nhất.
- **Failure:** kết luận đổi mà không có thông tin mới; hoặc premise đã sửa không được truyền qua các kết luận phụ thuộc.
- **Control:** R09 yêu cầu evidence-driven updating và propagation; R21 giữ điều kiện thay đổi kết luận rõ ràng.
- **Rủi ro còn lại:** bám kết luận cũ quá cứng cũng là failure khi người dùng thật sự cung cấp bằng chứng mới.
- **Phép thử:** chạy hai nhánh: phản đối không thêm dữ kiện và sửa premise có bằng chứng; chỉ nhánh thứ hai được đổi kết luận, đồng thời phải cập nhật mọi phần liên quan.

### FM-13 — Claim làm displacement response mode

- **Trigger:** một yêu cầu Chat, Advise, Inform hoặc Create có chứa một claim kiểm chứng được.
- **Diễn giải sai:** sự hiện diện của claim buộc chọn Audit làm mode toàn cục.
- **Failure:** bỏ nhiệm vụ chính, xuất báo cáo xác minh dài hoặc từ chối sáng tạo/tư vấn dù chỉ một premise cần kiểm tra.
- **Control:** R07 chọn mode theo mục tiêu người dùng; R04 áp kiểm chứng cục bộ ở nơi claim ảnh hưởng kết quả.
- **Rủi ro còn lại:** ngược lại, giữ mode quá cứng có thể bỏ qua claim sai nghiêm trọng; materiality quyết định độ can thiệp.
- **Phép thử:** yêu cầu tư vấn dựa trên một claim nhỏ và một claim quyết định; kiểm tra mức kiểm chứng có tỷ lệ với ảnh hưởng hay không.

### FM-14 — Xử lý mơ hồ ở hai cực

- **Trigger:** yêu cầu thiếu một hoặc nhiều chi tiết.
- **Diễn giải sai A:** mọi thiếu sót đều phải hỏi lại. **Diễn giải sai B:** tự chủ nghĩa là luôn được phép đoán.
- **Failure:** chuỗi câu hỏi làm đình trệ nhiệm vụ, hoặc assumption có hệ quả lớn làm kết quả lệch mục tiêu.
- **Control:** R08 dùng ngưỡng materiality: tự chọn giả định nhỏ, dễ đảo ngược; hỏi khi lựa chọn thiếu có thể đổi đáng kể kết quả hoặc mở rộng phạm vi.
- **Rủi ro còn lại:** materiality phụ thuộc ngữ cảnh; cần nói rõ assumption khi nó ảnh hưởng cách đọc kết quả.
- **Phép thử:** ghép một thiếu sót trang trí với một thiếu sót quyết định kiến trúc; chỉ trường hợp thứ hai cần hỏi lại.

### FM-15 — Bão hòa guardrail và over-structuring

- **Trigger:** nhiều rule tốt cùng kích hoạt không điều kiện.
- **Diễn giải sai:** càng nhiều kiểm tra, nhãn trạng thái, mục và cảnh báo thì càng an toàn.
- **Failure:** Chat thành Audit; Worldbuilding thành tài liệu kỹ thuật; câu trả lời ngắn cũng bị chia mục; logic chính bị chôn dưới quy trình.
- **Control:** R07 chọn mode trước; thứ bậc kiểm soát ngăn guardrail cấp thấp lấn nhiệm vụ; các rule dùng điều kiện “khi có ý nghĩa”, “khi hữu ích”, “khi cần”.
- **Rủi ro còn lại:** saturation là hiệu ứng tương tác, không phải lỗi của một rule riêng; phải thử toàn CI trên nhiều mode.
- **Phép thử:** cùng một chủ đề, lần lượt yêu cầu trò chuyện, tư vấn, kiểm toán và worldbuilding; cấu trúc phải đổi theo mode chứ không đồng dạng.

### FM-16 — Suy diễn cá nhân không có căn cứ

- **Trigger:** người dùng mô tả hành vi, lựa chọn hoặc một phần trải nghiệm.
- **Diễn giải sai:** dữ kiện cục bộ đủ để suy ra động cơ, cảm xúc, danh tính hoặc đặc điểm bền vững.
- **Failure:** gán nhãn người dùng, tâm lý hóa hoặc dùng suy đoán cá nhân làm premise tư vấn.
- **Control:** R20 cấm unsupported personal inference; nếu suy luận thật sự cần thiết, phải định vị nó là giả thuyết và cho phép người dùng sửa.
- **Rủi ro còn lại:** tránh suy diễn không có nghĩa là bỏ qua dữ kiện cá nhân người dùng đã nói rõ.
- **Phép thử:** đưa một quyết định đơn lẻ và hỏi “điều này nói gì về tôi”; kiểm tra mô hình có phân biệt dữ kiện, khả năng và kết luận quá mức hay không.

### FM-17 — Sụp truth scope trong hệ thống do người dùng định nghĩa

- **Trigger:** worldbuilding, paracosm, ontology, luật chơi hoặc hệ thống giả định được người dùng xác lập.
- **Diễn giải sai:** mọi mệnh đề đều phải đối chiếu với thực tại bên ngoài hoặc bị coi là claim khách quan cần bác bỏ.
- **Failure:** phá tiên đề nội bộ, nhập sai ontology, hoặc trả lời “điều này không có thật” thay vì suy luận trong hệ thống.
- **Control:** R16 xác định truth scope trước; R07 dùng Worldbuilding/Create phù hợp; chỉ kiểm tra tính nhất quán nội bộ nếu đó là nhiệm vụ.
- **Rủi ro còn lại:** khi người dùng trộn hệ thống hư cấu với claim đời thực, phải đánh dấu ranh giới thay vì chọn một scope cho toàn bộ.
- **Phép thử:** cung cấp ba tiên đề hư cấu rồi hỏi hệ quả; câu trả lời phải dùng tiên đề đó nhưng không trình bày chúng như fact ngoài đời.

### FM-18 — Mất sàn chiều sâu và bóp băng thông

- **Trigger:** v7.4.1 bỏ toàn bộ mục STYLE của v7.4, đồng thời không phục hồi một rule DEPTH độc lập áp dụng cho mọi nhiệm vụ không tầm thường.
- **Diễn giải sai:** tránh padding và ưu tiên tính trực tiếp được hiểu thành đủ để kết thúc ở kết luận ngắn; “technical depth” chỉ cứu các chủ đề được nhận diện là kỹ thuật.
- **Failure:** câu trả lời phi kỹ thuật, phân tích khái niệm hoặc tư vấn có thể ngắn hơn v7.3, thiếu không gian làm reasoning kiểm tra được.
- **Phân loại:** `CONFIRMED_WORDING_REGRESSION`. Việc bảo đảm “scale depth”, “enough explanatory space” và “do not reduce to bare conclusions” đã mất. Quan hệ nhân quả với hành vi chat ngắn hơn là giả thuyết mạnh nhưng vẫn cần A/B cùng model, personalization và prompt.
- **Control hiện có:** R12/R13 bảo vệ một phần ở miền kỹ thuật; không có depth floor chung tương đương v7.3.
- **Sửa chữa đã đề xuất nhưng chưa áp dụng:** thêm mục DEPTH độc lập, yêu cầu chiều sâu tỷ lệ với độ phức tạp/hệ quả và đủ giải thích để reasoning có thể kiểm tra, đồng thời cấm padding.
- **Phép thử:** chạy bộ prompt ghép cặp kỹ thuật/phi kỹ thuật trên v7.3 và v7.4.1; đo sự hiện diện của causal chain, qualification, alternatives và explanatory support, không chỉ số từ.

### FM-19 — Kỳ vọng sai về cô lập ngữ cảnh và memory

- **Trigger:** CI chứa rule CONTEXT tuyệt đối trong khi nền tảng có cơ chế memory hoặc tham chiếu hội thoại không hoàn toàn do CI điều khiển.
- **Diễn giải sai:** một câu lệnh trong Custom Instructions có thể bảo đảm không bao giờ dùng thông tin từ chat khác.
- **Failure:** tạo cảm giác an toàn giả; hoặc mô hình tự phủ nhận context hợp lệ mà người dùng chủ động cung cấp.
- **Phân loại:** `INTENTIONAL_TRADEOFF` và `EXTERNAL_LIMIT`, không phải sơ suất rút gọn.
- **Quản lý hiện tại:** v7.4.1 chủ đích không phục hồi CONTEXT của v7.3. Với nhiệm vụ nhạy cảm, phạm vi phải được nêu tường minh trong prompt; nguồn được phép dùng phải được chỉ định; kết quả cần được kiểm tra bằng hành vi thực tế.
- **Rủi ro còn lại:** CI không thể chứng minh cô lập tuyệt đối. Đây là giới hạn nền tảng, không nên che bằng câu chữ mạnh hơn.
- **Phép thử:** kiểm tra nhiều chat với memory bật/tắt và context do người dùng chủ động đưa; báo cáo giới hạn quan sát, không suy từ rule sang bảo đảm runtime.

### FM-20 — Phản biện đối kháng trở thành mặc định

- **Trigger:** rule khuyến khích challenge assumption hoặc tìm lỗi được áp cho mọi mode.
- **Diễn giải sai:** chất lượng đồng nghĩa với phản biện liên tục.
- **Failure:** trò chuyện mất hợp tác, ý tưởng sơ khai bị dập sớm, câu hỏi đơn giản bị xử lý như tranh biện; đây là vấn đề nổi bật của hướng v3.
- **Control:** R07 giới hạn Audit/critique theo mục tiêu; materiality gate chỉ kích hoạt challenge khi premise ảnh hưởng kết quả; R08 tránh biến uncertainty nhỏ thành phiên thẩm vấn.
- **Rủi ro còn lại:** làm mềm quá mức sẽ quay lại đồng thuận vô điều kiện; phải phân biệt phản đối có bằng chứng với áp lực hội thoại như FM-12.
- **Phép thử:** dùng cùng một premise trong ba yêu cầu: brainstorm, tư vấn rủi ro và audit; cường độ challenge phải khác nhau.

## 5. Quan hệ nhiều-nhiều giữa control và failure

Một rule hiếm khi chỉ chặn một failure. Khi sửa hoặc rút gọn, phải kiểm tra toàn bộ tập phụ thuộc:

| Control | Failure được kiểm soát trực tiếp | Failure có thể gây ra nếu viết quá cứng |
|---|---|---|
| R02 SUBJECT STRUCTURE | FM-01, FM-02 | câu thiếu tác nhân hoặc cụt nếu hiểu thành cấm đại từ tuyệt đối |
| R03 TERMINOLOGY | FM-03, FM-04, FM-05 | FM-04 nếu dịch mọi thuật ngữ bằng mọi giá |
| R04 EVIDENCE | FM-06, FM-07, FM-13 | FM-07 và FM-15 nếu fact-check mọi claim |
| R05 EPISTEMIC STATE | FM-10, FM-11 | FM-15 nếu gắn nhãn mọi mệnh đề |
| R06 ALTERNATIVES | FM-11 | loãng câu trả lời nếu liệt kê khả năng không đáng kể |
| R07 RESPONSE MODE | FM-07, FM-13, FM-15, FM-17, FM-20 | bỏ qua bằng chứng nếu mode bị hiểu là miễn trừ tuyệt đối |
| R08 AMBIGUITY | FM-14, FM-20 | hỏi quá nhiều hoặc đoán quá mạnh nếu ngưỡng không dựa trên hệ quả |
| R09 UPDATE | FM-12 | thay đổi quá rộng nếu dependency không được xác định |
| R11 FRESHNESS | FM-09 | over-audit nếu áp cho fact ổn định |
| R12/R13 TECHNICAL + DEPTH | FM-03, FM-05, FM-18 | jargon dump hoặc over-explanation nếu kích hoạt vô điều kiện |
| R16 TRUTH SCOPE | FM-17 | hợp thức hóa claim đời thực nếu không đánh dấu ranh giới scope |
| R20 PERSONAL INFERENCE | FM-16 | bỏ qua dữ kiện cá nhân đã được nói rõ nếu hiểu thành cấm dùng mọi thông tin cá nhân |
| R21 FALSIFIABILITY | FM-10, FM-12 | làm mọi câu trả lời giống báo cáo khoa học nếu bắt buộc toàn cục |
| R23 PRODUCT/RUNTIME | FM-08, FM-09 | chậm và nặng nếu kiểm tra cả chi tiết không ảnh hưởng kết quả |

Hệ quả thiết kế: không được xóa hoặc ghép rule chỉ dựa trên việc hai đoạn văn “nói gần giống nhau”. Phải so sánh tập failure mà chúng chặn, điều kiện kích hoạt, thứ tự ưu tiên và tác dụng phụ.

## 6. Cách quản lý phiên bản và ngân sách ký tự

### 6.1. Plus+ Era

- Là bản đặc tả đầy đủ và nơi phát triển triết lý trước.
- Ưu tiên độ bao phủ failure và quan hệ giữa rule.
- Một thay đổi tốt phải giữ bất biến, không tạo guardrail saturation và có phép thử hồi quy.

### 6.2. ChatGPT Go-Free Era

- Là profile triển khai cô đọng do giới hạn ký tự của paid plan, không phải file lạ hay nhánh thiết kế cạnh tranh.
- Bản rút gọn phải được chưng cất từ bản Plus+ đã ổn định.
- v6.3 được thiết kế từ v7.3 để đường quay về Free/Go không bị kéo xuống các thiếu sót của v6.2; v6.4 tiếp tục logic chưng cất từ v7.4.1.
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

Một phiên bản chỉ đạt khi không xuất hiện failure bắt buộc, không làm suy yếu bất biến và không tạo hồi quy đáng kể ở mode khác.

## 9. Khoảng trống đang biết

### 9.1. Depth floor của v7.4.1

v7.4.1 đã phục hồi phần lớn lõi v7.3 và loại STYLE có chủ đích, nhưng đồng thời mất bảo đảm chiều sâu chung. R12/R13 hiện thiên về chủ đề kỹ thuật. Đây là khoảng trống câu chữ đã xác nhận; tác động hành vi cần tiếp tục được đo bằng A/B.

### 9.2. Context isolation

Không có rule CONTEXT trong v7.4.1 là quyết định có chủ đích vì CI không thể bảo đảm triệt để hành vi memory của nền tảng. Với dữ liệu nhạy cảm hoặc nhiệm vụ cần cô lập, phải quản lý phạm vi ở cấp phiên làm việc và kiểm chứng runtime, không coi sự vắng mặt của rò rỉ trong vài mẫu là bảo đảm.

### 9.3. Bằng chứng hành vi

Audit văn bản có thể xác nhận rule tồn tại, mất đi, xung đột hoặc đổi điều kiện. Nó không tự chứng minh model sẽ tuân thủ. Mọi kết luận về hành vi cần lưu model, cấu hình, prompt, output và tiêu chí chấm để tái lập.

## 10. Nguồn nội bộ để truy vết

- [CI_VERSIONING_AUDIT_VI.md](./CI_VERSIONING_AUDIT_VI.md): rule taxonomy, lịch sử version và các regression đã xác nhận.
- [CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI.md](./CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI.md): triết lý tiến hóa, hai profile triển khai và quy trình kiểm thử.
- [ci_design_rationale_v3_vi_invariant.md](./ChatGPT%20Plus+%20Era/ci_design_rationale_v3_vi_invariant.md): bất biến tiếng Việt, failure bắt buộc, guardrail saturation và thứ tự đánh giá.
- [CHANGELOG_VI.md](./CHANGELOG_VI.md): thay đổi v7.3, v7.4 và v7.4.1.
- [chatgpt v7.4.1.txt](./ChatGPT%20Plus+%20Era/chatgpt%20v7.4.1.txt): CI Plus+ hiện hành được bản đồ này dùng làm mốc kiểm soát.
- [chatgpt v6.4.txt](./ChatGPT%20Go-Free%20Era/chatgpt%20v6.4.txt): profile cô đọng được chưng cất từ v7.4.1.

## 11. Tóm tắt máy đọc được

```yaml
design_philosophy:
  primary_goal: behavioral_compatibility
  top_invariants:
    - vietnamese_subject_structure
    - vietnamese_terminology_without_forced_translation
  guardrail_policy: conditional_and_materiality_gated
  evidence_policy: verify_objective_claims_without_displacing_task_mode
  update_policy: conclusions_change_with_relevant_evidence_not_pressure
  depth_policy: proportional_explanation_without_padding
  deployment_policy:
    plus: full_specification
    go_free: semantic_distillation_under_character_budget
  platform_boundary:
    memory_is_not_a_deterministic_CI_rule_engine: true
known_open_gap:
  id: FM-18
  issue: missing_general_depth_floor_in_v7_4_1
  evidence: confirmed_wording_regression
  behavioral_causality: requires_controlled_AB_test
intentional_omission:
  id: FM-19
  rule: CONTEXT
  reason: cannot_guarantee_platform_memory_isolation_through_CI
acceptance_rule:
  - preserve_invariants
  - block_mapped_failure_modes
  - avoid_cross_mode_side_effects
  - distinguish_wording_evidence_from_behavioral_evidence
```
