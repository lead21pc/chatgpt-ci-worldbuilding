# The Academy — Current Repository State

**Trạng thái:** snapshot điều hướng của repository.  
**Vai trò:** chỉ ra nguồn hiện hành cần đọc. File này không tự tạo canon và không thắng nguồn được liên kết nếu có xung đột.

## 1. Lớp điều khiển

- CI hiện hành trong repository: [The_Academy_CI_v2.0.md](The_Academy_CI_v2.0.md)
- Router hiện hành trên `main`: [The_Academy_Source_Router_v1.0.md](The_Academy_Source_Router_v1.0.md)
- Anti-drift kernel đang thử nghiệm trên nhánh tái cấu trúc: [The_Academy_Anti_Drift_Kernel.md](../../12_ANTI_DRIFT/The_Academy_Anti_Drift_Kernel.md)

Trạng thái nạp các file này vào ChatGPT Project runtime vẫn `UNVERIFIED`.

## 2. Kiến trúc The Academy

### V1.5

Nguồn baseline hiện hành trên `main`:

- [The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md](../../02_ACADEMY_ARCHITECTURE/V1_5/The_Academy_V1_5_Architecture_Baseline_Anti_Drift.md)
- [The_Academy_V1_5_Architecture_Handoff.md](../../02_ACADEMY_ARCHITECTURE/V1_5/The_Academy_V1_5_Architecture_Handoff.md)

Nguồn tái cấu trúc vòng 1 trên branch hiện tại:

- [The_Academy_V1_5_Architecture.md](../../02_ACADEMY_ARCHITECTURE/V1_5/The_Academy_V1_5_Architecture.md)

V1.5 vẫn là miền nhân quả thể chế trước tốt nghiệp và kết thúc ở return to origin theo các nguồn đã xác nhận.

### V2

Nguồn phương pháp hiện có:

- [Narrative Engine — Core Design Philosophy.md](../Narrative%20Engine%20%E2%80%94%20Core%20Design%20Philosophy.md)

Một nguồn kiến trúc V2 riêng chưa được tạo trong vòng 1 này.

### V2.5 / Academy Revise

V2.5 hiện là hướng làm việc đã từng được ghi trong baseline V1.5. Trong kế hoạch tái cấu trúc, nó sẽ được tách thành một **working branch** riêng để tránh bị đọc như nấc kế tiếp bắt buộc của một version ladder.

File branch riêng chưa được tạo trong vòng 1 này.

## 3. HIP

Nguồn chính:

- [Historical_Influence_Potential.md](../../01_HIP/Historical_Influence_Potential.md)

HIP là cổng đánh giá mở; tiêu chí đến từ context và HIP không tự bảo đảm outcome lịch sử.

## 4. Engine và mode hiện đã xác nhận trong repository

| Hạng mục | Trạng thái hiện hành | Nguồn dẫn |
| --- | --- | --- |
| Chaos | Canon Specification v3 là bản chính thức | [Chaos v3](../../04_NARRATIVE_ENGINES/Chaos/Chaos_Engine_Canon_Specification_v3.md) |
| Sloth | Mode V2 | [Authorial Decisions](../../The_Academy_Authorial_Decisions_2026-09-28.md) |
| Wrath | Mode V2 | [Authorial Decisions](../../The_Academy_Authorial_Decisions_2026-09-28.md) |
| Chaos | Mode V2 | [Authorial Decisions](../../The_Academy_Authorial_Decisions_2026-09-28.md) |
| Lust | Thuộc V1.5; chi tiết institutional role/interface/authority còn source-bound | [Lust Working Draft](../../03_V1_5_INSTITUTIONAL_ENGINES/Lust/Lust_Working_Draft.md) |
| Greed Governor | Responsibility | [Authorial Decisions](../../The_Academy_Authorial_Decisions_2026-09-28.md) |

Các nhãn này không cấp cùng architecture, capability hoặc authority cho các engine khác.

## 5. Provenance và nguồn cũ

- [engine genealogy](../../06_ENGINE_GENEALOGY/engine_genealogy_and_development_updated.md) mô tả lịch sử hình thành; genealogy không tự tạo current hierarchy.
- [source_archive](../../source_archive/README.md) giữ nguồn cũ và bản nháp để truy vết; archive không tự vô hiệu hóa dữ kiện trong nguồn và cũng không kích hoạt lại version cũ.
- [The_Academy_Authorial_Decisions_2026-09-28.md](../../The_Academy_Authorial_Decisions_2026-09-28.md) ghi các xác nhận tác giả đã externalize tại thời điểm đó.

## 6. Quy tắc đọc snapshot

Nếu file này và nguồn được liên kết bất đồng:

```text
repair CURRENT STATE
≠ use CURRENT STATE to override scoped source
```

Snapshot này tồn tại để giảm chi phí tìm nguồn, không phải để tạo thêm một tầng thẩm quyền.
