# Quy trình cho gói AetherFire Project

Dùng reference này khi cần chọn mốc package, sửa/regenerate/chứng nhận gói, hoặc khi metadata package ảnh hưởng trực tiếp tới kết luận. Với LOOKUP hẹp, chỉ đọc metadata tối thiểu để tìm đúng nguồn hiện hành; không chạy workflow package đầy đủ.

Dùng reference này khi target nằm trong package có đủ `00_AETHERFIRE_CONSOLIDATION_INDEX.md`, `MANIFEST.md`, `build_consolidation.ps1` và `Source_Archive/`. Đây là lớp kiểm soát cách tạo tài liệu, không phải nguồn lore mới.

## 1. Preflight và vai trò

Trước khi chọn mốc, đề xuất sửa, hoặc chứng nhận package:

1. Đọc index để biết reading order, domain boundaries và source bị loại trừ.
2. Đọc manifest để phân biệt generated outputs với archived source snapshot và ghi hash ban đầu.
3. Đọc phần liên quan của reconciliation record để biết quyết định, unresolved item và provenance đang có hiệu lực.
4. Đọc đầy đủ file canon/source thuộc phạm vi audit. Chỉ đọc toàn build script khi cần sửa package, xác minh nguồn tạo output hoặc truy một phép biến đổi; không dùng tên file hay logic build làm bằng chứng canon.

`Source_Archive/` lưu đầu vào byte-exact, nhưng việc một file có trong archive không chứng minh nó được import hoặc có quyền canon. File root `*_CURRENT.md`, index, reconciliation record và manifest là output của package khi build script tạo chúng. Xác minh vai trò bằng nội dung hiện hành thay vì suy từ tên.

## 2. Lập kế hoạch thay đổi

Trước thay đổi nhiều domain, thay đổi build pipeline hoặc retcon có hệ quả chéo, trình bày một kế hoạch ngắn gồm:

- quyết định đã được người dùng chốt và phạm vi thay thế;
- nguồn mới hoặc phép reconciliation cần thêm;
- generated outputs dự kiến đổi;
- invariants và unresolved items phải giữ;
- kiểm tra package và kiểm tra ngữ nghĩa sẽ chạy.

Không cần một planning skill riêng cho audit đơn giản. Kế hoạch không mở rộng quyền sửa ngoài quyết định đã chốt.

## 3. Cập nhật package sau phê duyệt

1. Ghi nhận hash/status trước thay đổi và danh sách file được phép tác động.
2. Không sửa archived source cũ tại chỗ. Khi người dùng cung cấp hoặc chốt nguồn mới, lưu nó thành file mới byte-exact với tên không trùng.
3. Cập nhật build/reconciliation tối thiểu để nhập đúng phần đã duyệt. Giữ source excluded hoặc provenance-only ngoài current canon nếu chưa có quyết định đổi vai trò.
4. Chạy build script từ project root để regenerate toàn bộ output và manifest.
5. Đọc lại generated output thực tế, index, reconciliation record và manifest có liên quan. Đối chiếu hai chiều với quyết định, mốc cũ và nguồn còn hiệu lực.
6. Không chuyển mốc nếu còn thay đổi ngoài phạm vi, nội dung được duyệt bị thiếu, unresolved item bị xóa, source excluded bị nhập ngoài ý muốn hoặc package không tái lập được.

Nếu kiến trúc package đã thay đổi có thẩm quyền, làm theo kiến trúc hiện hành và ghi rõ khác biệt; không biến tên file cụ thể trong reference này thành canon bất biến.

## 4. Cổng xác minh trước khi báo hoàn tất

Chạy `scripts/verify_aetherfire_package.ps1` từ skill này với đường dẫn package. Script chỉ đọc package thật, rebuild trong thư mục tạm và xóa bản tạm sau khi so sánh.

Ví dụ:

```powershell
& '<skill-root>\scripts\verify_aetherfire_package.ps1' -ProjectRoot '<AetherFire Project path>'
```

Kết quả `PASS` chỉ chứng minh:

- các file được manifest liệt kê tồn tại và đúng SHA-256;
- inventory Markdown của Source_Archive khớp manifest;
- rebuild cô lập tạo lại generated outputs và manifest byte-identical;
- các source đang được khai báo excluded mặc định không bị build script đọc trực tiếp.

Nó không chứng minh canon đúng, reconciliation hợp lệ hoặc LLM sẽ tuân thủ. Sau script vẫn phải:

- đọc và audit ngữ nghĩa generated output;
- đối chiếu yêu cầu/decision checklist từng mục;
- kiểm nguồn ngoài phạm vi không đổi;
- ghi rõ phần chưa kiểm và mọi UNKNOWN/DEFERRED còn lại.

Nếu source excluded được người dùng cho phép nhập về sau, truyền danh sách exclusion hiện hành bằng `-ExpectedExcludedSource` hoặc cập nhật verifier cùng quyết định package; không giữ mặc định cũ trái canon.
