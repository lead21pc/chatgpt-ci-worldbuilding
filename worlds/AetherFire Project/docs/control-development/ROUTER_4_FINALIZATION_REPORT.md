# Hoàn thiện AetherFire Source Router 4.0

> Trạng thái: hoàn tất tệp điều khiển cục bộ để người dùng duyệt và thử trong môi trường Project tách biệt. Chưa cài vào ChatGPT Project, chưa sửa lore hoặc gói nguồn. Commit/push repository không triển khai control vào Project.

## Đầu vào và ranh giới

- Đã đọc đầy đủ AetherFire CI/AetherFire_CI_version_v3.0.md. Đây là tệp final local, không mang trạng thái PROPOSAL. Việc nó có trong kho không chứng minh nội dung đã cài vào ChatGPT Project.
- Đã đọc đủ tám tài liệu trong AetherFire_Router_4_Proposal/ tại gốc dự án. Đường dẫn ghi trong yêu cầu, New CI and Router/AetherFire_Router_4_Proposal/, hiện không tồn tại; không tạo bản sao hay di chuyển tài liệu.
- Đã đọc Router 3.2 để so hồi quy và kiểm tra hook phạm vi/phụ thuộc của năm overlay hiện hành. Router 3.2 không được dùng làm mẫu cấu trúc bắt buộc.
- Tác vụ chỉ tạo Anti-Drift Source/AetherFire_Anti_Drift_Source_Router_v4.0.md và báo cáo này. Không thay CI 3.0, Router 3.2, overlay, 00-92, builder, source lore hay Project upload.

## Quy tắc đã đưa vào Router final

| Nguồn thiết kế | Quy tắc vận hành đã nhập |
| --- | --- |
| ROUTER_4_ARCHITECTURE | CI 3.0 ở cấp trên; route pass, bootstrap, Module Gate, source load, reconciliation, overlay, execution và pre-response check. Router không tự chọn CI. |
| MODULE_HEADER_CONTRACT | Module ID, runtime role, scope, authority/owner boundary, mode và hard requires; header chỉ định tuyến, không tự phong canon. Index status là kết quả kiểm tra, không là lời tự khai của header. |
| MODULE_DISCOVERY_AND_CATALOG | Ưu tiên catalog dẫn xuất trong 00; không giả định backend liệt kê toàn bộ tệp. Catalog không cấp quyền, không là dependency graph. Thiếu catalog hiện tại thì dùng danh sách nguồn sẵn trong 00 làm đường tương thích FULL_FILE, không bịa module ID. |
| MODULE_GATE_FAILURE_MODEL | Chặn theo đúng phần phụ thuộc; node không chắc thì đọc full; nguồn quyết định hoặc hard module thiếu thì SOURCE_LOAD_BLOCKED; SOURCE_LOAD_PARTIAL chỉ cho gap thứ cấp thật sự không đổi kết luận. |
| MIGRATION_FROM_ROUTER_3_2 | Giữ quyền nguồn, cách ly lịch sử, trạng thái mở, reconciliation và overlay gate; bỏ numeric CI resolver cùng bảng tuyến lore cố định. |
| NEW_MODULE_ONBOARDING_TEST | Contract cho module mới: header hợp lệ, admission có thẩm quyền, catalog/package cập nhật; Router core không cần nhánh mới. |
| PROJECT_RUNTIME_SHADOW_TEST | Không tự nhận VERIFIED_MODULE_CLOSURE từ parser local hoặc snippet; cần bằng chứng Project thật sự nạp đủ ngữ cảnh, node và dependency. |
| PLAIN_LANGUAGE_EXPLANATION | Giữ ranh giới dễ hiểu giữa header, catalog, Module Gate và hai cấp dependency; không nhập văn bản giải thích dành cho người dùng vào control file. |

## Nội dung chỉ giữ làm tài liệu phát triển

Fixture A-E, lịch sử di trú chi tiết, ngưỡng thử nghiệm, kế hoạch paired/shadow test, chi phí token, phương án builder và quyết định triển khai không nằm trong Router final. Tám tài liệu đề xuất vẫn là design history, test specification và audit evidence cục bộ; Project runtime không cần đọc chúng để thực hiện Router 4.0.

## Đối chiếu hồi quy với Router 3.2

| Bất biến | Kết quả trong 4.0 |
| --- | --- |
| Route trước execution; route không tạo kết luận | Giữ rõ ở mục 1. |
| Thứ tự đọc khác thứ tự quyền nguồn; nguồn mới không tự thành canon | Giữ ở mục 1, 3 và 6. |
| Old-canon quarantine; UNKNOWN/OPEN/DEFERRED/CONFLICTED | Giữ ở mục 6; thiếu nguồn không có historical hoặc memory fallback. |
| Reconciliation trước execution; 91 quyết định phải được đọc | Giữ ở mục 6; 91 FULL_FILE trong giai đoạn đầu. |
| Overlay đúng scope, phụ thuộc bắc cầu, không vượt CI/Router | Giữ ở mục 7; overlay được kích hoạt luôn FULL_FILE. |
| SOURCE_LOAD_BLOCKED và SOURCE_LOAD_PARTIAL giới hạn hẹp | Giữ ở mục 2, 5, 6 và 8. |
| Tách các chủ sở hữu xuyên miền | Module Gate bắt đọc mọi controlling owner materially affected. |
| Router tự tìm CI phiên bản cao nhất | Loại bỏ. Router yêu cầu CI 3.0 đã được cài ở cấp trên. |
| Bảng lore 10/20/30/... cố định trong Router | Loại bỏ. Nguồn hiện tại đi qua chỉ mục 00 theo FULL_FILE; module tương lai qua header/catalog. |
| Mọi routed source bắt buộc full-file tuyệt đối | Chuyển thành FULL_FILE mặc định; chỉ cho NODE_OR_FULL khi closure thực sự được review và nạp đủ. |

## Kiểm tra và giới hạn

- Kiểm tra tĩnh xác nhận file final có đủ tên gate, hai cấp dependency, hai load mode, ba bootstrap/evidence control 00/91/92, pre-response receipt, cùng trạng thái SOURCE_LOAD_BLOCKED và SOURCE_LOAD_PARTIAL. Không phát hiện dòng có khoảng trắng thừa ở cuối.
- Bộ kiểm tra control-regressions ở chế độ chỉ đọc chọn CI v3.0 và Router v4.0 theo số phiên bản cục bộ, nhưng kết quả tổng là BLOCKED, không chạy mô hình. Lý do cụ thể: CI v3.0 ghi tiêu đề ChatGPT 8.7, còn runner đòi dạng khai báo ChatGPT v8.7. Đây là chênh lệch giữa bộ chọn/kiểm tra cũ với cặp control mới; không được diễn giải là Router đã vượt hồi quy. Không sửa CI hoặc runner ngoài phạm vi.
- Việc đặt Router v4.0 đúng đường dẫn được yêu cầu làm bộ chọn số phiên bản cục bộ nhìn thấy nó. Điều đó không cài nó vào ChatGPT Project; trạng thái control đang cài ở Project chưa được xác minh.
- Chưa có catalog module thực trong 00, module lore có header, Project retrieval trace, phép thử node closure, hay paired semantic result. Vì vậy đường hiện khả dụng trong package cũ chỉ là legacy indexed FULL_FILE; NODE_OR_FULL chưa được xác minh để kích hoạt.
- Cần một task riêng để kiểm byte của CI 3.0 đã cài, dùng một snapshot nguồn/controls nhất quán, thử trong Project shadow, xử lý bộ kiểm tra cục bộ và quyết định triển khai. Không dùng structural check thay bằng chứng runtime.

## Tệp đầu ra

Anti-Drift Source/AetherFire_Anti_Drift_Source_Router_v4.0.md

- Kích thước: 14,750 byte.
- SHA-256: FF94C87AEED6956662B1BDAB74B5DC276ED559CCC490428F7BFBAD5339EDFA53.
- Trạng thái: FINAL LOCAL CONTROL FILE, sẵn sàng cho người dùng duyệt và một lượt Project shadow deployment được phê duyệt riêng; không phải control đã kích hoạt.
