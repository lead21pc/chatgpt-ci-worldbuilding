# Router 5 / CI 3.3 — audit và phương án candidate

Trạng thái: **CANDIDATE, chưa triển khai vào ChatGPT Project**. Đơn vị công việc này giữ CI 3.2/Router 4.4 làm baseline và rollback. Không chuyển canon, archive, catalog, admission hoặc lifecycle của regression cũ.

## Bằng chứng và giới hạn chẩn đoán

Tác giả báo ngày 2026-10-09 mô hình biết Router tồn tại nhưng bỏ qua khi nền tảng suy giảm hiệu năng. Đây là báo cáo hành vi; repository không có trace đủ để xác định nguyên nhân sâu hơn. Router 4.4 đang hoạt động, không được coi là control hỏng. Vấn đề thiết kế có thể kiểm chứng là nhiều quan hệ xác định được còn nằm trong văn xuôi, còn việc kiểm CI lúc runtime tạo đường quay CI → Router → CI. Candidate giảm hai rủi ro này; chưa chứng minh giảm lỗi tuân thủ mô hình.

Đã đọc SYSTEM_CONTEXT.md, CI 3.2, Router 4.4, Pipeline 1.0, Glossary 1.0, tám overlay hiện hành, metadata module, builder, runner/README/case regression và global 8.8/8.9 temp. Global 8.9 chỉ dùng đối chiếu, không làm base hay được chỉnh. Glossary là tài liệu bảo trì, không thành nguồn canon hoặc dependency runtime mới.

## Phân loại audit 4.4

| Phần baseline | A — cấu hình xác định được | B — phán đoán ngữ nghĩa còn lại | C — kiểm trước runtime |
| --- | --- | --- | --- |
| Header / §1 | Entry PROMPT_ROUTE_ONLY, thứ tự tám cổng | Phạm vi tác vụ, quyền đổi canon, mở rộng phạm vi | Cặp CI/Router/base, không có cổng CI runtime |
| §2 Bootstrap | FULL_FILE 00/92, record 91 có điều kiện | Cùng generation thật, stale catalog, đủ bằng chứng cho phạm vi hẹp | File tham chiếu tồn tại; package check riêng |
| §3 Module Gate | Trường tối thiểu, defaults, REVIEW_REQUIRED | Admission, controlling owner, authority overlap, current/historical | Builder kiểm metadata/package hiện có; không coi header là thẩm quyền |
| §4 Dependencies | Phân biệt MODULE_REQUIRES / NODE_REQUIRES, bắc cầu, fallback/block | Edge có thật, đã review và quyết định tác vụ hay chưa | Đích/chu trình control graph; builder không cho metadata edge chưa được hỗ trợ trong package hiện hành |
| §5 Loading | Modes, read proofs, thành phần closure, failure states | Qualifier có thể đổi kết luận, actual retrieval, tính quyết định của nguồn | Enum/schema; không chứng nhận actual read từ metadata |
| §6 Authority | Bootstrap/record refs, điểm gọi reconciliation | User scope, current authority, provenance, giữ UNKNOWN/DEFERRED/CONFLICTED | File/version refs; không tự giải quyết canon |
| §7 Overlays | Tám family, requires/conditional_requires, chọn phiên bản số, FULL_FILE | Applicability và điều kiện materiality, control conflict | ID trùng, thiếu đích, chu trình kể cả cạnh điều kiện; missing/ambiguous eligible version |
| §8 Coverage | Ranh giới fallback/block/partial, cổng trước execution/response | Bằng chứng đủ chưa, gap phụ có thật sự không quyết định | Probe và unit test cấu trúc; runtime vẫn cần quan sát |

## Thiết kế đủ dùng

CI 3.3 sở hữu entry. Nó gọi Router trước lookup current, so sánh current, localization/application vào FTH, implementation dùng current, canon mutation/reconciliation, audit/simulation phụ thuộc current. Seed extraction hoặc primitive decomposition chỉ từ đầu vào tự đủ không cần Router; khi chuyển sang current-dependent phải route hoặc làm rõ/nhánh hóa trước phần phụ thuộc. Pipeline không được miễn yêu cầu entry của CI.

Router YAML gồm deployment metadata, chuỗi cổng, bootstrap, module header contract, load contract, failure mapping, version selection, các cạnh control và scalar semantic policies. `deployment` chỉ dành cho maintenance validator; runtime bắt đầu tại PROMPT_ROUTE_ONLY và không đọc metadata này để tìm/đọc/chọn/suy luận/validate/xác nhận active CI. Không có companion runtime policy, registry, scoring, global dependency ontology hoặc engine thực thi prompt.

Applicability/điều kiện vẫn do mô hình đánh giá. Khi đã có ID/điều kiện đúng, `expand` cho closure cố định; không tự đoán chúng từ prompt. Cạnh overlay không phải MODULE_REQUIRES lore. Node uncertainty → FULL_FILE của owner; hard module thiếu/chưa review/chu trình chưa giải quyết vẫn block. Decisive gap block; chỉ gap phụ được chứng minh không quyết định mới cho PARTIAL.

Validator opt-in qua `build_consolidation.py --check-router-candidate`: parse YAML an toàn và chặn key trùng, kiểm schema/refs/cặp phiên bản/entry/stages/load/failure/ID/dependency graph/version resolution. Không đọc canon archive, không viết file, không chọn CI active, không route prompt, không tự sửa/lên lifecycle. PyYAML 6.0.3 đã có trên máy; không cài hoặc đổi dependency. Máy thiếu PyYAML nhận lỗi rõ ở chế độ candidate; chế độ package cũ không import nó.

Đặt CI/Router candidate trong `candidates/` vì runner hiện tại chọn file con trực tiếp theo phiên bản số. Để CI 3.3 ở thư mục chính sẽ làm thay đổi effective control của kiểm tra dù chưa triển khai. Candidate không được thêm vào catalog/hash canon. Baseline runner và các case cũ giữ nguyên.

## Pipeline và base

Giữ Pipeline 1.0 nguyên byte. Nó đã subordinate CI, giao nguồn current cho Router và cho phép chỉ phần transformation tự đủ. CI 3.3 làm rõ clause tự đủ không miễn entry cho localization/application/implementation/current comparison. Chưa có conflict buộc tạo 1.1. Tên AetherFire cũ trong tiêu đề Pipeline được ghi nhận, không sửa ngoài phạm vi.

Giữ ChatGPT 8.8 base. Bản 8.9 temp chỉ là đối chiếu các invariant và diễn đạt, không tự trở thành base/deployment. Publication repository khác deployment Project.

## Kiểm chứng và cách chạy

Từ thư mục `Project Feather Core`:

```powershell
python -B build_consolidation.py --check
python -B build_consolidation.py --check-router-candidate
python -B -m unittest discover -s tests
& tests/control-regressions/run.ps1
```

Unit test candidate kiểm cấu hình lỗi, dependency expansion và version resolver bằng dữ liệu giả; không giả lập phán đoán applicability. Bộ `tests/control-regressions/router-v5-probes.json` có 13 probe paired, trạng thái DRAFT/NOT_RUN. File này tách khỏi tập cases cũ để không tự đổi lifecycle hoặc anchor.

Kiểm runtime thủ công cần hai môi trường tương đương, riêng biệt: baseline CI 3.2 + Router 4.4 và candidate CI 3.3 + Router 5; cùng source generation và overlay/Pipeline. Chỉ triển khai khi có quyền riêng. Với mỗi probe, ghi prompt, nguồn thật đã truy xuất, gate đầu tiên, owner/mode/closure, controls, failure state và truth status; so sánh expected/baseline_comparison. Thử thêm nguồn quyết định không có, node không đủ, hard dependency thiếu/chu trình và qualifier ngoài node. Đặc biệt kiểm Router không thực hiện hành động CI runtime. Việc mô hình chỉ nói mình tuân thủ không chứng minh actual read. Không tự đánh dấu ACTIVE từ kết quả structural.

Kiểm hiện có không chứng minh platform hết suy giảm, retrieval Library thực tế, semantic applicability, actual closure, hiệu quả token hay xác suất tuân thủ. Control-family graph được validate; dependency graph lore runtime chỉ được xử lý theo policy, không được suy ra từ catalog.

## Kết quả kiểm chứng local

Baseline trước sửa: package PASS, 38 unit tests PASS, runner LIMITED_CHECK với CI 3.2 / base 8.8, model_executed=false. Sau thay đổi: package và candidate validator PASS; toàn bộ 56 unit tests PASS (38 bài cũ + 18 bài candidate). Runner tiếp tục LIMITED_CHECK và giữ CI 3.2 / base 8.8, không chạy mô hình. LIMITED_CHECK là giới hạn bao phủ đã có, không phải bằng chứng lỗi runtime.

Đối chiếu snapshot 151 file tracked của project/global: chỉ builder và README regression thay đổi trong tập này; 149 file còn lại nguyên byte, gồm baseline CI/Router, Pipeline, overlays, canon, archive và global 8.8/8.9. Sáu file mới là candidate/audit/validator/test/probes đúng phạm vi. Các deletion ngoài project có trước tác vụ được giữ nguyên, không stage.

Trước push, kiểm trên detached checkout từ origin/main bắt được khác biệt bố cục global CI: local đặt ở `ChatGPT Plus+ Era`, bản hosted đặt ở `llm-controls/global-instructions/ChatGPT Plus+ Era`. Validator nay chấp nhận sự tồn tại của base 8.8 ở một trong hai bố cục đã có, không di chuyển file hoặc chọn CI runtime. Thêm một bài kiểm thử cả hai bố cục và trường hợp thiếu cả hai; tổng 57 bài (19 candidate).

## Rollback và bảo toàn

Khi chưa deploy, rollback chỉ là tiếp tục dùng cặp 3.2/4.4. Nếu sau này thử candidate trong Project, khôi phục đồng bộ CI 3.2 + Router 4.4, bỏ candidate khỏi nguồn control active; không trộn cặp. Không xóa canon hoặc đổi lifecycle để rollback. Chế độ builder cũ vẫn là mặc định.

Baseline SHA-256:

| File | SHA-256 |
| --- | --- |
| `Project Feather Core CI/FTH_CI_version_v3.2.md` | `e09c69068ac5b7d31d026337817e6bced1e064a17c3d5ff97fd086348419e749` |
| `Anti-Drift Source/FTH_Anti_Drift_Source_Router_v4.4.md` | `bc57f52e75edf19e44c733c955e87b5088127e5f74eaa72e481d57e999467f85` |
| `Anti-Drift Source/FTH_Authoring_Pipeline_v1.0.md` | `98f357e8fa00827a31f15dd4fb24b3b6e1eccbc8eece89c6205da2377a455025` |
